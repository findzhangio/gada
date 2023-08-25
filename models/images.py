# models/images.py
from sqlalchemy import Column, Integer, String
from db.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    sd_prompt_id = Column(Integer)
    sd_var_id = Column(Integer)
    file_name = Column(String(length=255))
    cos_path = Column(String(length=255))

