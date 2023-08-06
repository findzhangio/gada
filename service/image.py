from fastapi import HTTPException, status
import crud
import schemas
from common.stable_diffusion_client import sd_webui_client


def generate_and_store_image(prompt, db):
    generated_prompt = sd_webui_client.txt2img(prompt)
    if not generated_prompt:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to generate prompt")

        # 构建模型数据
    prompt_data = schemas.StableDiffusionPromptCreate(subject=prompt, prompt_content=generated_prompt)

    # 使用CRUD操作存储提示
    return crud.create_prompt(db=db, prompt=prompt_data)
