from pydantic import BaseModel, Field
from typing import List, Optional


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=1000
    )
    conversation: List[Message] = []


class ChatResponse(BaseModel):
    response: str
    intent: str
    availability: Optional[dict] = None


class AvailabilityRequest(BaseModel):
    check_in: str
    check_out: str
    adults: int = Field(
        ...,
        ge=1,
        le=20
    )


class AvailabilityResponse(BaseModel):
    check_in: str
    check_out: str
    adults: int
    available: bool
    rooms: list