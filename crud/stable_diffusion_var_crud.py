from sqlalchemy.orm import Session
import models
import schemas


# CRUD for StableDiffusionVar
def get_var(db: Session, var_id: int):
    return db.query(models.StableDiffusionVar).filter(models.StableDiffusionVar.id == var_id).first()


def get_vars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StableDiffusionVar).offset(skip).limit(limit).all()


def get_var_total(db: Session) -> int:
    return db.query(models.StableDiffusionVar).count()


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
    for key, value in var_data.dict().items():
        setattr(db_var, key, value)

    db.commit()
    db.refresh(db_var)
    return db_var


def delete_var(db: Session, var_id: int):
    var = db.query(models.StableDiffusionVar).filter(models.StableDiffusionVar.id == var_id).first()
    if var:
        db.delete(var)
        db.commit()
    return var