from fastapi import FastAPI
from users import users_router
from categories import categories_router
from notes import notes_router
import all_models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que o frontend (Vite) acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # porta do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota raiz simples para testar
@app.get("/")
def homepage():
    return {"message": "Backend rodando!"}

# Rotas de USERS
app.include_router(users_router, prefix="/users", tags=["Users"])

# Rotas de CATEGORIES
app.include_router(categories_router, prefix="/categories", tags=["Categories"])

# Rotas de NOTES
app.include_router(notes_router, prefix="/notes", tags=["Notes"])