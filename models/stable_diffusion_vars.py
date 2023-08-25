# models/stable_diffusion_vars.py
from sqlalchemy import Column, Integer, String, Boolean, FLOAT
from db.database import Base


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