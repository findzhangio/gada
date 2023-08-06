from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from fastapi import HTTPException

import crud
import database
import schemas
from utils import image_handler

router = APIRouter()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/images/", response_model=schemas.Image)
def create_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = image_handler.save_image(file)  # 存储图片并获取存储路径
    return crud.create_image(db=db, image=schemas.ImageCreate(file_name=file.filename), file_path=file_path)


@router.get("/images/", response_model=list[schemas.Image])
def list_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_images(db, skip=skip, limit=limit)


@router.get("/images/{image_id}/", response_model=schemas.StableDiffusionPrompt)
def get_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="image not found")
    return db_image
