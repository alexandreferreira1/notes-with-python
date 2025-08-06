from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[str] = Field(None, max_length=100)
    password: Optional[str]


class UserOut(UserBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
