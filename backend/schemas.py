from pydantic import BaseModel
from typing import List

class EmotionRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotions: str
