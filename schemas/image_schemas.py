from pydantic import BaseModel
from typing import Optional


class ImageBase(BaseModel):
    sd_prompt_id: Optional[int]
    sd_var_id: Optional[int]
    file_name: str
    cos_path: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        from_attributes = True