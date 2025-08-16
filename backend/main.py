from fastapi import FastAPI
from users import users_router
from categories import categories_router
import all_models

app = FastAPI()

# Rota raiz simples para testar
@app.get("/")
def homepage():
    return {"message": "Backend rodando!"}

# Rotas de USERS
app.include_router(users_router, prefix="/users", tags=["Users"])

# Rotas de CATEGORIES
app.include_router(categories_router, prefix="/categories", tags=["Categories"])