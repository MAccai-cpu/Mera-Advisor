from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import EvaluacionRiesgoModel

router = APIRouter(prefix="/capa-d", tags=["Capa D - Riesgos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class RiesgoSchema(BaseModel):
    nivel_riesgo: str
    factor_riesgo: str
    recomendacion: str

@router.get("/evaluaciones")
def obtener_riesgos(db: Session = Depends(get_db)):
    riesgos = db.query(EvaluacionRiesgoModel).all()
    return {
        "capa": "D - Riesgos",
        "total": len(riesgos),
        "evaluaciones": [{"id": r.id, "nivel": r.nivel_riesgo, "factor": r.factor_riesgo, "recomendacion": r.recomendacion} for r in riesgos]
    }

@router.post("/evaluaciones")
def crear_riesgo(riesgo: RiesgoSchema, db: Session = Depends(get_db)):
    nuevo = EvaluacionRiesgoModel(
        nivel_riesgo=riesgo.nivel_riesgo,
        factor_riesgo=riesgo.factor_riesgo,
        recomendacion=riesgo.recomendacion
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Evaluación de riesgo registrada con éxito", "riesgo": {"id": nuevo.id, "factor": nuevo.factor_riesgo}}