from .schemas import NoteCreate, NoteUpdate, NoteOut
from .crud import create_note, get_notes_by_user, update_note
from .routes import router as notes_router