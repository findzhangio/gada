from sqlalchemy.orm import Session
import models
import schemas
from typing import Optional


# CRUD for Image
def get_image(db: Session, image_id: int) -> Optional[models.Image]:
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Image).offset(skip).limit(limit).all()


def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def delete_image(db: Session, image_id: int):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if image:
        db.delete(image)
        db.commit()


# CRUD for StableDiffusionPrompt
def get_prompt(db: Session, prompt_id: int):
    return db.query(models.StableDiffusionPrompt).filter(models.StableDiffusionPrompt.id == prompt_id).first()


def get_prompts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StableDiffusionPrompt).offset(skip).limit(limit).all()


def create_prompt(db: Session, prompt: schemas.StableDiffusionPromptCreate):
    db_prompt = models.StableDiffusionPrompt(**prompt.model_dump())
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt


# CRUD for StableDiffusionVar
def get_var(db: Session, var_id: int):
    return db.query(models.StableDiffusionVar).filter(models.StableDiffusionVar.id == var_id).first()


def get_vars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StableDiffusionVar).offset(skip).limit(limit).all()


def create_var(db: Session, var: schemas.StableDiffusionVarCreate):
    db_var = models.StableDiffusionVar(**var.model_dump())
    db.add(db_var)
    db.commit()
    db.refresh(db_var)
    return db_var


def update_var(db: Session, var_id: int, var_data: schemas.StableDiffusionVarUpdate):
    db_var = db.query(models.StableDiffusionVar).filter(models.StableDiffusionVar.id == var_id).first()
    if not db_var:
        return None  # or you can raise an exception if the item does not exist

    # Update attributes based on passed data
    for key, value in var_data.model_dump().items():
        setattr(db_var, key, value)

    db.commit()
    db.refresh(db_var)
    return db_var
