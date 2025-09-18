from sqlalchemy.orm import Session, joinedload
from sqlalchemy import asc, desc, func
from notes.models import Note
from categories.models import Category
from notes.schemas import NoteCreate, NoteUpdate
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID
from datetime import datetime
from typing import Optional


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


def get_notes(db: Session, user_id: UUID, order: str = 'desc', archived: Optional[bool] = None, is_favorite: Optional[bool] = None, prioritize_pinned: Optional[bool] = None):
    order_field = func.coalesce(Note.updated_at, Note.created_at)

    query = (
        db.query(Note)
        .join(Note.category)
        .options(joinedload(Note.category))  # eager load da categoria
        .filter(Category.user_id == user_id, Note.deleted_at.is_(None))
    )

    # Filtros
    if archived is not None:
        query = query.filter(Note.archived.is_(archived))
    if is_favorite is not None:
        query = query.filter(Note.is_favorite.is_(is_favorite))

    # Ordenação
    if order == 'asc':
        if prioritize_pinned:
            query = query.order_by(desc(Note.pinned), asc(order_field))
        else:
            query = query.order_by(asc(order_field))
    else:
        if prioritize_pinned:
            query = query.order_by(desc(Note.pinned), desc(order_field))
        else:
            query = query.order_by(desc(order_field))

    return query.all()

def get_notes_by_user(db: Session, user_id: UUID, order: str = "desc"):
    return get_notes(db, user_id, order, archived=False, prioritize_pinned=True)

def get_favorites_notes_user(db: Session, user_id: UUID, order: str = "desc"):
    return get_notes(db, user_id, order, is_favorite=True, archived=False)

def get_archived_notes_user(db: Session, user_id: UUID, order: str = "desc"):
    return get_notes(db, user_id, order, archived=True)

def get_deleted_notes_user(db: Session, user_id: UUID, order: str = "desc"):
    order_field = func.coalesce(Note.updated_at, Note.created_at)

    query = (
        db.query(Note)
        .join(Note.category)
        .options(joinedload(Note.category))  # eager load categoria
        .filter(Category.user_id == user_id, Note.deleted_at.isnot(None))
    )

    # Ordenação
    if order == "asc":
        query = query.order_by(asc(order_field))
    else:
        query = query.order_by(desc(order_field))

    return query.all()

def update_note(db: Session, note_id: int, note_data: NoteUpdate):
    note = db.query(Note).filter(Note.id == note_id,
                                 Note.deleted_at.is_(None)).first()

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
    note = db.query(Note).filter(Note.id == note_id,
                                 Note.deleted_at.is_(None)).first()

    if not note:
        return None

    note.deleted_at = datetime.utcnow()  # type: ignore

    try:
        db.commit()
        db.refresh(note)
    except SQLAlchemyError:
        db.rollback()
        raise

    return note
