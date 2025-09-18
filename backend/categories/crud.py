from sqlalchemy.orm import Session
from categories.models import Category
from categories.schemas import CategoryCreate
from uuid import UUID


def create_category(db: Session, category_data: CategoryCreate, user_id: UUID):
    new_category = Category(
        name= category_data.name,
        user_id=user_id
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_category_by_name(db: Session, name: str, user_id: UUID):
    return db.query(Category).filter(
        Category.name == name,
        Category.user_id == user_id
        ).first()

def get_categories(db: Session, user_id: UUID, skip: int = 0, limit: int = 100):
    return db.query(Category).filter(
        Category.user_id == user_id
    ).offset(skip).limit(limit).all()