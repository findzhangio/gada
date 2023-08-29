# crud/image_crud.py
from sqlalchemy import desc
from sqlalchemy.orm import Session
import models
import schemas
from typing import Optional
from common.tencent_cos import tencent_cos_client


# CRUD for Image
def get_image(db: Session, image_id: int) -> Optional[models.Image]:
    # 根据id查询Image
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_images(db: Session, skip: int = 0, limit: int =10):
    # 返回查询到的图片
    # return db.query(models.Image).offset(skip).limit(limit).all()
    return db.query(models.Image).order_by(desc(models.Image.id)).offset(skip).limit(limit).all()


def get_image_total(db: Session) -> int:
    return db.query(models.Image).count()


def create_image(db: Session, image: schemas.ImageCreate):
    # 创建Image
    db_image = models.Image(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def delete_image(db: Session, image_id: int):
    # 开始数据库事务
    try:
        # 首先根据id查询出Image记录
        image = db.query(models.Image).filter(models.Image.id == image_id).first()

        if not image:
            return "Image not found"

        # 获取COS中的路径
        cos_path = image.cos_path  # 假设你的Image模型有一个存储COS路径的字段

        # 从COS中删除图片
        tencent_cos_client.delete_file(cos_path)

        # 从数据库中删除Image记录
        db.delete(image)
        db.commit()

    except Exception as e:
        # 如果发生错误，回滚数据库事务
        db.rollback()
        return False, str(e)

    return True, "Image deleted successfully"
