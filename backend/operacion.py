
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import RegistroOperacionModel

router = APIRouter(prefix="/capa-c", tags=["Capa C - Operación"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class OperacionSchema(BaseModel):
    unidad: str
    estado_operativo: str
    detalles: str

@router.get("/directrices")
def obtener_operaciones(db: Session = Depends(get_db)):
    ops = db.query(RegistroOperacionModel).all()
    return {
        "capa": "C - Operación",
        "total": len(ops),
        "registros": [{"id": o.id, "unidad": o.unidad, "estado": o.estado_operativo, "detalles": o.detalles, "fecha": str(o.fecha_registro)} for o in ops]
    }

@router.post("/directrices")
def crear_operacion(op: OperacionSchema, db: Session = Depends(get_db)):
    nueva = RegistroOperacionModel(
        unidad=op.unidad,
        estado_operativo=op.estado_operativo,
        detalles=op.detalles
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Registro de operación guardado con éxito", "registro": {"id": nueva.id, "unidad": nueva.unidad}}