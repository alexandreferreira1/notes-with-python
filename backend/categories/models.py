from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)

    # Relacionamentos
    user = relationship("User", back_populates="categories")
    notes = relationship("Note", back_populates="category", cascade="all, delete-orphan")