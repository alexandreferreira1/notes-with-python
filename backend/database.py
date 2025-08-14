from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from base import Base  # Importa Base isolado em base.py

load_dotenv()

# Lê a variável DATABASE_URL
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL is None:
    raise ValueError("Variável de ambiente DATABASE_URL não definida")

# Cria conexão com o banco
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões, gerando sessões sempre com a mesma configuração
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Função para fornecer sessão do banco como dependência no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()