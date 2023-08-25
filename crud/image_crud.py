from sqlalchemy.orm import Session
import models
import schemas
from typing import Optional


# CRUD for Image
def get_image(db: Session, image_id: int) -> Optional[models.Image]:
    # 根据id查询Image
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_images(db: Session, skip: int = 0, limit: int =10):
    # 返回查询到的图片
    return db.query(models.Image).offset(skip).limit(limit).all()


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
    # 删除Image
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if image:
        db.delete(image)
        db.commit()