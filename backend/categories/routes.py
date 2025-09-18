from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from categories import crud, schemas
from database import get_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=schemas.CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, user_id: UUID, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, name=category.name, user_id=user_id)
    if db_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nome de categoria já existente")
    return crud.create_category(db, category_data=category, user_id=user_id)

@router.get("/", response_model=List[schemas.CategoryOut])
def read_categories(user_id: UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, user_id=user_id, skip=skip, limit=limit)
    return categories