from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class CategoryBase(BaseModel):
    name: str = Field(..., max_length=100)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(..., max_length=100)


class CategoryOut(CategoryBase):
    id: int
    user_id: UUID

    class Config:
        orm_mode = True
