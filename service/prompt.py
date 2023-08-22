from fastapi import HTTPException, status
import crud
import schemas
from common.openai_client import openai_client


def generate_and_store_prompt(subject, db):
    generated_prompt = openai_client.generative_sd_prompt(subject)
    if not generated_prompt:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to generate prompt")

        # 构建模型数据
    prompt_data = schemas.StableDiffusionPromptCreate(subject=subject, prompt_content=generated_prompt)

    # 使用CRUD操作存储提示
    return crud.create_prompt(db=db, prompt=prompt_data)
