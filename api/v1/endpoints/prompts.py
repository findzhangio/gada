from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.prompt import generate_and_store_prompt
from fastapi import HTTPException

import crud
import database
import schemas

router = APIRouter()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/prompts/", response_model=schemas.StableDiffusionPrompt)
def create_prompt(content, db: Session = Depends(get_db)):
    return generate_and_store_prompt(db=db, content=content)


@router.get("/prompts/", response_model=list[schemas.StableDiffusionPrompt])
def list_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_prompts(db, skip=skip, limit=limit)


@router.get("/prompts/{prompt_id}/", response_model=schemas.StableDiffusionPrompt)
def get_prompt(prompt_id: int, db: Session = Depends(get_db)):
    db_prompt = crud.get_prompt(db, prompt_id=prompt_id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt
