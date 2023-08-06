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


@router.post("/sd_vars/", response_model=schemas.StableDiffusionVar)
def create_sd_vars(sd_vars: schemas.StableDiffusionVarCreate, db: Session = Depends(get_db)):
    return crud.create_var(db, sd_vars)


@router.get("/sd_vars/", response_model=list[schemas.StableDiffusionVar])
def list_sd_vars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vars(db, skip=skip, limit=limit)


@router.get("/sd_vars/{var_id}/", response_model=schemas.StableDiffusionVar)
def get_sd_var(var_id: int, db: Session = Depends(get_db)):
    sd_vars = crud.get_var(db, var_id=var_id)
    if sd_vars is None:
        raise HTTPException(status_code=404, detail="SD Vars not found")
    return sd_vars


# @router.put("/sd_vars/{var_id}/", response_model=schemas.StableDiffusionVar)
# def update_sd_vars(var_id: int, sd_vars: schemas.StableDiffusionVar, db: Session = Depends(get_db)):
#     return crud.update_var(db, var_id=var_id, sd_vars=sd_vars)
