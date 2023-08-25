from sqlalchemy.orm import Session
import models
import schemas


# CRUD for StableDiffusionPrompt
def get_prompt(db: Session, prompt_id: int):
    return db.query(models.StableDiffusionPrompt).filter(models.StableDiffusionPrompt.id == prompt_id).first()


def get_prompts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StableDiffusionPrompt).offset(skip).limit(limit).all()


def get_prompt_total(db: Session) -> int:
    return db.query(models.StableDiffusionPrompt).count()


def create_prompt(db: Session, prompt: schemas.StableDiffusionPromptCreate):
    db_prompt = models.StableDiffusionPrompt(**prompt.model_dump())
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt


def delete_prompt(db: Session, prompt_id: int):
    prompt = db.query(models.StableDiffusionPrompt).filter(models.StableDiffusionPrompt.id == prompt_id).first()
    if prompt:
        db.delete(prompt)
        db.commit()


def update_prompt(db: Session, prompt_id: int, prompt_data: schemas.StableDiffusionPromptUpdate):
    db_prompt = db.query(models.StableDiffusionPrompt).filter(models.StableDiffusionPrompt.id == prompt_id).first()
    if not db_prompt:
        return None  # or you can raise an exception if the item does not exist

    # Update attributes based on passed data
    for key, value in prompt_data.dict().items():
        setattr(db_prompt, key, value)

    db.commit()
    db.refresh(db_prompt)
    return db_prompt