from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from notes import crud, schemas
from database import get_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=schemas.NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note_data: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note_data)


@router.get("/user/{user_id}", response_model=List[schemas.NoteOut])
def read_user_notes(user_id: UUID, order: str = "desc", db: Session = Depends(get_db)):
    return crud.get_notes_by_user(db, user_id, order=order)


@router.get('/user/{user_id}/favorites', response_model=List[schemas.NoteOut])
def read_favorites_notes(user_id: UUID, order: str = "desc", db: Session = Depends(get_db)):
    return crud.get_favorites_notes_user(db, user_id, order=order)


@router.get('/user/{user_id}/archived', response_model=List[schemas.NoteOut])
def read_archived_notes(user_id: UUID, order: str = "desc", db: Session = Depends(get_db)):
    return crud.get_archived_notes_user(db, user_id, order=order)

@router.get('/user/{user_id}/deleted', response_model=List[schemas.NoteOut])
def read_deleted_notes(user_id: UUID, order: str = "desc", db: Session = Depends(get_db)):
    return crud.get_deleted_notes_user(db, user_id, order=order)

@router.patch("/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note_data: schemas.NoteUpdate, db: Session = Depends(get_db)):
    updated_note = crud.update_note(db, note_id, note_data)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return updated_note


@router.delete("/{note_id}", response_model=schemas.NoteOut)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = crud.delete_note(db, note_id)
    if not deleted_note:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return deleted_note