# api/v1/endpoints/image_tasks.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from celery_app import task_generate_and_store_image
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


# 定义一个post请求，路由为/image_tasks/，并返回一个ImageTask类型的响应
@router.post("/image_tasks/", response_model=schemas.ImageTask)
async def create_image_task(task: schemas.ImageTaskCreate, db: Session = Depends(get_db)):
    # 循环添加task.count个任务，并将图像任务添加到数据库
    for _ in range(task.count):
        # 启动一个任务，并将图像任务添加到数据库
        task_generate_and_store_image.delay(task.sd_var_id, task.sd_prompt_id)
    # 返回创建的ImageTask
    return crud.create_image_task(task=task, db=db)


# 获取图片生成任务列表
@router.get("/image_tasks/", response_model=schemas.ImageTasksList)
def list_image_tasks(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    total = crud.get_image_task_total(db)
    # 计算跳过的数量
    skip = (page - 1) * page_size
    # 计算每页的数量
    limit = page_size
    # 返回图片任务列表
    data = crud.get_image_tasks(db, skip=skip, limit=limit)
    return {"total": total, "data": data}


# 返回图片生成任务详情
@router.get("/image_tasks/{task_id}/", response_model=schemas.ImageTask)
def get_image_task(task_id: int, db: Session = Depends(get_db)):
    # 根据任务ID查询任务
    db_task = crud.get_image_task(db, task_id=task_id)
    # 如果查询不到任务，抛出HTTPException，状态码为404，详情为"ImageTask not found"
    if db_task is None:
        raise HTTPException(status_code=404, detail="ImageTask not found")
    # 返回查询到的任务
    return db_task
