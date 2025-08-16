from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NoteBase(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    content: str
    position: Optional[int] = None
    category_id: int
    is_favorite: bool = False
    pinned: bool = False
    archived: bool = False


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    content: Optional[str]
    position: Optional[int]
    category_id: Optional[int]
    is_favorite: Optional[bool]
    pinned: Optional[bool]
    archived: Optional[bool]
    deleted_at: Optional[datetime] = None


class NoteOut(NoteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True
