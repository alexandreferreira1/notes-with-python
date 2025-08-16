from .schemas import NoteCreate, NoteUpdate, NoteOut
from .crud import create_note, get_notes
from .routes import router as notes_router