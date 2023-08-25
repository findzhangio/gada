# models/image_tasks.py
from sqlalchemy import Column, Integer
from db.database import Base


class ImageTask(Base):
    __tablename__ = "image_tasks"

    id = Column(Integer, primary_key=True, index=True)
    sd_prompt_id = Column(Integer)
    sd_var_id = Column(Integer)
    count = Column(Integer)
