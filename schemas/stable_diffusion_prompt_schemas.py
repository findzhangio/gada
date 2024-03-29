from pydantic import BaseModel
from typing import Optional, List


class StableDiffusionPromptBase(BaseModel):
    subject: str
    prompt_content: str


class StableDiffusionPromptCreate(StableDiffusionPromptBase):
    pass


class StableDiffusionPrompt(StableDiffusionPromptBase):
    id: int

    class Config:
        from_attributes = True


class StableDiffusionPromptUpdate(BaseModel):
    subject: Optional[str]
    prompt_content: Optional[str]


class StableDiffusionPromptList(BaseModel):
    total: int
    data: List[StableDiffusionPrompt]
