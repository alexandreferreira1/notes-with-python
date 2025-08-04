from database import engine

try:
    with engine.connect():
        print("🟢 Conectado com sucesso ao PostgreSQL!")

except Exception as error:
    print("🔴 Erro ao conectar:", error)
