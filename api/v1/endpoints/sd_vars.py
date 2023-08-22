from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

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


# 创建SD变量
@router.post("/sd_vars/", response_model=schemas.StableDiffusionVar)
def create_sd_vars(sd_vars: schemas.StableDiffusionVarCreate, db: Session = Depends(get_db)):
    # 调用crud的create_var函数，创建SD变量
    return crud.create_var(db, sd_vars)


# 查询SD变量
@router.get("/sd_vars/", response_model=list[schemas.StableDiffusionVar])
def list_sd_vars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # 调用crud的get_vars函数，查询SD变量
    return crud.get_vars(db, skip=skip, limit=limit)


# 根据ID查询SD变量
@router.get("/sd_vars/{var_id}/", response_model=schemas.StableDiffusionVar)
def get_sd_var(var_id: int, db: Session = Depends(get_db)):
    # 调用crud的get_var函数，根据ID查询SD变量
    sd_vars = crud.get_var(db, var_id=var_id)
    # 如果查询不到SD变量，抛出HTTPException
    if sd_vars is None:
        raise HTTPException(status_code=404, detail="SD Vars not found")
    return sd_vars


# 更新SD变量
@router.put("/sd_vars/{var_id}/", response_model=schemas.StableDiffusionVar)
def update_var(
        var_id: int,
        var_data: schemas.StableDiffusionVarUpdate,
        db: Session = Depends(get_db)
):
    # 调用crud的update_var函数，更新SD变量
    db_var = crud.update_var(db, var_id, var_data)
    # 如果更新失败，抛出HTTPException
    if db_var is None:
        raise HTTPException(status_code=404, detail="Var not found or update failed")
    return db_var


# 删除SD变量
@router.delete("/sd_vars/{var_id}/", response_model=schemas.StableDiffusionVar)
def delete_var(
        var_id: int,
        db: Session = Depends(get_db)
):
    # 调用crud的delete_var函数，删除SD变量
    db_var = crud.delete_var(db, var_id)
    # 如果删除失败，抛出HTTPException
    if db_var is None:
        raise HTTPException(status_code=404, detail="Var not found")
    return db_var
