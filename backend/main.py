from fastapi import FastAPI
from users.routes import router as users_router
import all_models

app = FastAPI()

# Rota raiz simples para testar
@app.get("/")
def homepage():
    return {"message": "Backend rodando!"}

# Rotas de USERS
app.include_router(users_router, prefix="/users", tags=["Users"])