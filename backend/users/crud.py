from sqlalchemy.orm import Session
from users.models import User
from users.schemas import UserCreate
from datetime import datetime
import uuid

def create_user(db: Session, user_data: UserCreate) -> User:
        new_user = User(
                id=uuid.uuid4(),
                name=user_data.name,
                email=user_data.email,
                password=user_data.password,
                created_at=datetime.utcnow(),
            )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: uuid.UUID):
        return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
