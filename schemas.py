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
        orm_mode = True


class StableDiffusionPromptBase(BaseModel):
    subject: str
    prompt_content: str


class StableDiffusionPromptCreate(StableDiffusionPromptBase):
    pass


class StableDiffusionPrompt(StableDiffusionPromptBase):
    id: int

    class Config:
        orm_mode = True


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
        orm_mode = True

