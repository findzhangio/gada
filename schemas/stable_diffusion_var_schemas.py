from pydantic import BaseModel
from typing import Optional, List


class StableDiffusionVarBase(BaseModel):
    negative_prompt: str
    steps: int
    sampler_name: str
    width: int
    height: int
    cfg_scale: int
    enable_hr: bool
    hr_scale: int
    hr_upscaler: str
    hr_second_pass_steps: int
    hr_resize_x: int
    hr_resize_y: int
    denoising_strength: float
    controlnet_units: str


class StableDiffusionVarUpdate(BaseModel):
    negative_prompt: Optional[str]
    steps: Optional[int]
    sampler_name: Optional[str]
    width: Optional[int]
    height: Optional[int]
    cfg_scale: Optional[int]
    enable_hr: Optional[bool]
    hr_scale: Optional[int]
    hr_upscaler: Optional[str]
    hr_second_pass_steps: Optional[int]
    hr_resize_x: Optional[int]
    hr_resize_y: Optional[int]
    denoising_strength: Optional[float]
    controlnet_units: Optional[str]


class StableDiffusionVarCreate(StableDiffusionVarBase):
    pass


class StableDiffusionVar(StableDiffusionVarBase):
    id: int

    class Config:
        from_attributes = True


class StableDiffusionVarList(BaseModel):
    total: int
    data: List[StableDiffusionVar]
