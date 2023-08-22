from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.prompt import generate_and_store_prompt
from fastapi import HTTPException

import crud
from db import database
import schemas

router = APIRouter()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 定义一个post请求，请求路径为/prompts/，并且返回一个StableDiffusionPrompt类型的响应
@router.post("/prompts/", response_model=schemas.StableDiffusionPrompt)
def create_prompt(subject, db: Session = Depends(get_db)):
    # 调用generate_and_store_prompt函数，生成并存储prompt
    return generate_and_store_prompt(db=db, subject=subject)


@router.get("/prompts/", response_model=list[schemas.StableDiffusionPrompt])
def list_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 调用crud.get_prompts函数，获取prompt
    return crud.get_prompts(db, skip=skip, limit=limit)


@router.get("/prompts/{prompt_id}/", response_model=schemas.StableDiffusionPrompt)
def get_prompt(prompt_id: int, db: Session = Depends(get_db)):
    # 调用crud.get_prompt函数，获取prompt
    db_prompt = crud.get_prompt(db, prompt_id=prompt_id)
    # 如果prompt不存在，抛出HTTPException
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt


# 删除prompts
@router.delete("/prompts/{prompt_id}/", response_model=schemas.StableDiffusionPrompt)
def delete_prompt(prompt_id: int, db: Session = Depends(get_db)):
    # 根据提示ID查询prompts
    db_prompt = crud.get_prompt(db, prompt_id=prompt_id)
    # 如果prompts不存在，则抛出404错误
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    # 删除prompts
    crud.delete_prompt(db, prompt_id=prompt_id)
    # 返回prompts
    return db_prompt


# 更新prompts
@router.put("/prompts/{prompt_id}/", response_model=schemas.StableDiffusionPrompt)
def update_prompt(
        prompt_id: int,
        prompt_data: schemas.StableDiffusionPromptUpdate,
        db: Session = Depends(get_db)
):
    # 更新prompts
    db_prompt = crud.update_prompt(db, prompt_id, prompt_data)
    # 如果prompts不存在或更新失败，则抛出404错误
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found or update failed")
    # 返回prompts
    return db_prompt
