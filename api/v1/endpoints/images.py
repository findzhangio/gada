from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from service import image
import crud
from db import database
import schemas

# 定义路由
router = APIRouter()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 创建图像
@router.post("/images/", response_model=schemas.Image)
def create_image(prompt_id: int, sd_var_id: int, db: Session = Depends(get_db)):
    return image.generate_and_store_image(prompt_id=prompt_id, sd_var_id=sd_var_id, db=db)


# 查询图像列表
@router.get("/images/", response_model=list[schemas.Image])
def list_images(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    # 计算跳过的数量
    skip = (page - 1) * page_size
    # 计算每页的数量
    limit = page_size
    # 返回查询结果
    return crud.get_images(db=db, skip=skip, limit=limit)


# 查询图像
@router.get("/images/{image_id}/", response_model=schemas.StableDiffusionPrompt)
def get_image(image_id: int, db: Session = Depends(get_db)):
    # 根据图像id查询图像
    db_image = crud.get_image(db=db, image_id=image_id)
    # 如果查询不到图像，抛出404异常
    if db_image is None:
        raise HTTPException(status_code=404, detail="image not found")
    # 返回查询结果
    return db_image
