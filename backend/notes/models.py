from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(100), nullable=True)
    content = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    is_favorite = Column(Boolean, nullable=False)
    pinned = Column(Boolean, nullable=False)
    archived = Column(Boolean, nullable=False)
    category_id = Column(ForeignKey("categories.id"), nullable=False)

    # Relacionamentos
    category = relationship("Category", back_populates="notes")
