# service/image_schemas.py
from fastapi import HTTPException, status
import crud
from db import database
import schemas
from os import environ
from common.stable_diffusion_client import sd_webui_client, openpose
from common.tencent_cos import tencent_cos_client
from utils.image_handler import save_img
from log import logger


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_and_store_image(prompt_id, sd_var_id, db):
    image_cache_path = environ.get('IMAGE_CACHE_PATH', './tmp/')
    cos_path = environ.get('COS_IMAGE_PATH', '/sd/')
    sd_prompt = crud.get_prompt(db, prompt_id)
    if not sd_prompt:
        raise ValueError("Prompt not found")
    sd_vars = crud.get_var(db, sd_var_id)
    if not sd_vars:
        raise ValueError("SD Vars not found")
    controlnet_list = []
    if sd_vars.controlnet_units == "openpose":
        file = sd_vars.controlnet_units.get("file")
        pose = openpose(file)
        controlnet_list.append(pose)

    # Generate image
    generated_image = sd_webui_client.txt2img(
        prompt=sd_prompt.prompt_content,
        negative_prompt=sd_vars.negative_prompt,
        steps=sd_vars.steps,
        sampler_name=sd_vars.sampler_name,
        width=sd_vars.width,
        height=sd_vars.height,
        cfg_scale=sd_vars.cfg_scale,
        enable_hr=sd_vars.enable_hr,
        hr_scale=sd_vars.hr_scale,
        hr_upscaler=sd_vars.hr_upscaler,
        hr_second_pass_steps=sd_vars.hr_second_pass_steps,
        hr_resize_x=sd_vars.hr_resize_x,
        hr_resize_y=sd_vars.hr_resize_y,
        denoising_strength=sd_vars.denoising_strength,
        controlnet_units=controlnet_list
    )
    if not generated_image:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to generate prompt")

    #保存图片
    file_name = save_img(generated_image.image)

    print(generated_image.info)

    #上传文件至cos
    local_file = image_cache_path + file_name
    cos_file = cos_path + file_name
    logger.debug("local_file: %s; cos_file: %s", local_file, cos_file)
    resp = tencent_cos_client.upload_file(local_file=local_file, cos_path=cos_file)
    #判断是否上传成功，如失败raise抛出异常
    print(resp)

    # 构建模型数据
    db_generated_image = schemas.ImageCreate(sd_prompt_id=prompt_id, sd_var_id=sd_var_id, file_name=file_name, cos_path=cos_path)

    return crud.create_image(db=db, image=db_generated_image)
