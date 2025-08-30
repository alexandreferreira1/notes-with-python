from .schemas import NoteCreate, NoteUpdate, NoteOut
from .crud import create_note, get_notes_by_user, get_favorites_notes_user, get_archived_notes_user, update_note, delete_note
from .routes import router as notes_router