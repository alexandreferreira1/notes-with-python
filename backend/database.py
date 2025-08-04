from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

# Lê a variável DATABASE_URL
DATABASE_URL = os.getenv('DATABASE_URL')

# Cria conexão com o banco
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões, gerando sessões sempre com a mesma configuração
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base para os modelos ORM
Base = declarative_base()
