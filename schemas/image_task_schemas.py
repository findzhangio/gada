# schemas.py
from pydantic import BaseModel
from typing import List


class ImageTaskBase(BaseModel):
    sd_prompt_id: int
    sd_var_id: int
    count: int


class ImageTaskCreate(ImageTaskBase):
    pass


class ImageTask(ImageTaskBase):
    id: int

    class Config:
        from_attributes = True


class ImageTasksList(BaseModel):
    total: int
    data: List[ImageTask]
