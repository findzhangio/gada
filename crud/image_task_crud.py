from sqlalchemy.orm import Session
from models import models
import schemas
from typing import Optional


# CRUD for ImageTask
def get_image_task(db: Session, task_id: int) -> Optional[models.ImageTask]:
    return db.query(models.ImageTask).filter(models.ImageTask.id == task_id).first()


def get_image_task_total(db: Session) -> int:
    return db.query(models.ImageTask).count()


def get_image_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ImageTask).offset(skip).limit(limit).all()


def create_image_task(db: Session, task: schemas.ImageTaskCreate):
    db_task = models.ImageTask(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
