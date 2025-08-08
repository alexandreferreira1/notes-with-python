from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from base import Base
from datetime import datetime
from typing import TYPE_CHECKING


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(100), nullable=True)
    content = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    is_favorite = Column(Boolean, default=False, nullable=False)
    pinned = Column(Boolean, default=False, nullable=False)
    archived = Column(Boolean, default=False, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Relacionamentos
    category = relationship("Category", back_populates="notes")

if TYPE_CHECKING:
    from categories.models import Category