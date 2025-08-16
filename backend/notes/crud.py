from sqlalchemy.orm import Session
from notes.models import Note
from notes.schemas import NoteCreate
from sqlalchemy.exc import SQLAlchemyError


def create_note(db: Session, note_data: NoteCreate):
    # Não salvar nota sem conteúdo
    if not note_data.content or note_data.content.strip() == "":
        return None

    # Gerar position da nota
    last_position = db.query(Note).order_by(
        Note.position.desc()).first()
    current_position = (last_position[0] + 1) if last_position else 1

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


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()
