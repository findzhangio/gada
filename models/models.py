# models.py
from sqlalchemy import Column, Integer, String, Boolean, FLOAT
from db.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    sd_prompt_id = Column(Integer)
    sd_var_id = Column(Integer)
    file_name = Column(String(length=255))
    cos_path = Column(String(length=255))


class StableDiffusionPrompt(Base):
    __tablename__ = "stable_diffusion_prompts"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(length=32))
    prompt_content = Column(String(length=4096))


class StableDiffusionVar(Base):
    __tablename__ = "stable_diffusion_vars"

    id = Column(Integer, primary_key=True, index=True)
    negative_prompt = Column(String(length=2048))
    steps = Column(Integer)
    sampler_name = Column(String(length=32))
    width = Column(Integer)
    height = Column(Integer)
    cfg_scale = Column(Integer)
    enable_hr = Column(Boolean)
    hr_scale = Column(Integer)
    hr_upscaler = Column(String(length=32))
    hr_second_pass_steps = Column(Integer)
    hr_resize_x = Column(Integer)
    hr_resize_y = Column(Integer)
    denoising_strength = Column(FLOAT)
    controlnet_units = Column(String(length=64))


class ImageTask(Base):
    __tablename__ = "image_tasks"

    id = Column(Integer, primary_key=True, index=True)
    sd_prompt_id = Column(Integer)
    sd_var_id = Column(Integer)
    count = Column(Integer)
