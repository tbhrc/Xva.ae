from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, Field


class ExpertBase(BaseModel):
    name: str = Field(..., max_length=255)
    title: str = Field(..., max_length=255)
    summary: Optional[str] = None
    linked_in_url: HttpUrl
    location: Optional[str] = None
    expertise: Optional[str] = None
    tools: Optional[str] = None
    vetted_status: Optional[str] = Field(default="approved")


class ExpertCreate(ExpertBase):
    pass


class ExpertUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=255)
    title: Optional[str] = Field(default=None, max_length=255)
    summary: Optional[str] = None
    linked_in_url: Optional[HttpUrl] = None
    location: Optional[str] = None
    expertise: Optional[str] = None
    tools: Optional[str] = None
    vetted_status: Optional[str] = None


class ExpertOut(ExpertBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
