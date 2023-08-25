# models/stable_diffusion_prompts.py
from sqlalchemy import Column, Integer, String
from db.database import Base


class StableDiffusionPrompt(Base):
    __tablename__ = "stable_diffusion_prompts"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(length=32))
    prompt_content = Column(String(length=4096))