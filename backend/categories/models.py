from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from base import Base
from typing import TYPE_CHECKING


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relacionamentos
    user = relationship("User", back_populates="categories")
    notes = relationship("Note", back_populates="category", cascade="all, delete-orphan")


if TYPE_CHECKING:
    from users.models import User
    from notes.models import Note