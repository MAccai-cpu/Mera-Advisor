from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import RegistroExperienciaModel

router = APIRouter(prefix="/capa-f", tags=["Capa F - Experiencia MERA"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ExperienciaSchema(BaseModel):
    usuario: str
    retroalimentacion: str
    puntuacion: int

@router.get("/historial")
def obtener_experiencias(db: Session = Depends(get_db)):
    exps = db.query(RegistroExperienciaModel).all()
    return {
        "capa": "F - Experiencia MERA",
        "total": len(exps),
        "registros": [{"id": e.id, "usuario": e.usuario, "retroalimentacion": e.retroalimentacion, "puntuacion": e.puntuacion, "fecha": str(e.fecha)} for e in exps]
    }

@router.post("/historial")
def crear_experiencia(exp: ExperienciaSchema, db: Session = Depends(get_db)):
    nueva = RegistroExperienciaModel(
        usuario=exp.usuario,
        retroalimentacion=exp.retroalimentacion,
        puntuacion=exp.puntuacion
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Registro de experiencia guardado con éxito", "experiencia": {"id": nueva.id, "usuario": nueva.usuario}}