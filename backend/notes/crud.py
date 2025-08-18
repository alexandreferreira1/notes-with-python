from sqlalchemy.orm import Session, joinedload
from notes.models import Note
from categories.models import Category
from notes.schemas import NoteCreate, NoteUpdate
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID
from datetime import datetime



def create_note(db: Session, note_data: NoteCreate):
    # Não salvar nota sem conteúdo
    if not note_data.content or note_data.content.strip() == "":
        return None

    # Gerar position da nota
    last_position = db.query(Note).order_by(
        Note.position.desc()).first()
    current_position = last_position.position + 1 if last_position else 1

    new_note = Note(
        title=note_data.title,
        content=note_data.content,
        category_id=note_data.category_id,
        position=current_position,
        is_favorite=note_data.is_favorite,
        pinned=note_data.pinned,
        archived=note_data.archived
    )

    try:
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
    except SQLAlchemyError:
        db.rollback()
        raise
    return new_note


def get_notes_by_user(db: Session, user_id: UUID):
    return (
        db.query(Note)
        .join(Note.category)
        .options(joinedload(Note.category)) # eager load da categoria
        .filter(Category.user_id == user_id, Note.deleted_at.is_(None))
        .all()
    )

def update_note(db: Session, note_id: int, note_data: NoteUpdate):
    note = db.query(Note).filter(Note.id == note_id, Note.deleted_at.is_(None)).first()
    
    if not note:
        return None
    
    for field, value in note_data.dict(exclude_unset=True).items():
        setattr(note, field, value)
    note.updated_at = datetime.utcnow()  # type: ignore

    try:
        db.commit()
        db.refresh(note)
    except SQLAlchemyError:
        db.rollback()
        raise

    return note

def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id, Note.deleted_at.is_(None)).first()
    
    if not note:
        return None
    
    note.deleted_at = datetime.utcnow() # type: ignore

    try:
        db.commit()
        db.refresh(note)
    except SQLAlchemyError:
        db.rollback()
        raise

    return note