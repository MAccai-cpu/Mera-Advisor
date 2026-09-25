from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import NormativaModel

router = APIRouter(prefix="/capa-e", tags=["Capa E - Normatividad"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class NormativaSchema(BaseModel):
    codigo_norma: str
    descripcion: str
    entidad_emisora: str

@router.get("/marco")
def obtener_normativas(db: Session = Depends(get_db)):
    normas = db.query(NormativaModel).all()
    return {
        "capa": "E - Normatividad",
        "total": len(normas),
        "normativas": [{"id": n.id, "codigo": n.codigo_norma, "descripcion": n.descripcion, "entidad": n.entidad_emisora} for n in normas]
    }

@router.post("/marco")
def crear_normativa(normativa: NormativaSchema, db: Session = Depends(get_db)):
    nueva = NormativaModel(
        codigo_norma=normativa.codigo_norma,
        descripcion=normativa.descripcion,
        entidad_emisora=normativa.entidad_emisora
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Normativa registrada con éxito", "normativa": {"id": nueva.id, "codigo": nueva.codigo_norma}}