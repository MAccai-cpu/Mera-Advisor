from fastapi import FastAPI
from sqlalchemy import text
from backend.database import engine

app = FastAPI(
    title="MERA Advisor - Motor Cognitivo ANA",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al núcleo de MERA Advisor. Sistema operativo y conectado."}

@app.get("/health/db")
def test_db_connection():
    """Verifica la conexión con PostgreSQL y las tablas creadas"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT tablename FROM pg_tables WHERE schemaname='public';"))
            tables = [row[0] for row in result]
        return {
            "estado": "Conexión exitosa a PostgreSQL",
            "tablas_encontradas": tables
        }
    except Exception as e:
        return {
            "estado": "Error de conexión",
            "detalles": str(e)
        }