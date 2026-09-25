from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import UnidadTransporteModel

router = APIRouter(prefix="/capa-b", tags=["Capa B - Transporte"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UnidadSchema(BaseModel):
    codigo_unidad: str
    tipo_vehiculo: str
    capacidad_carga: float
    estado: str = "Disponible"

@router.get("/flota")
def obtener_flota(db: Session = Depends(get_db)):
    unidades = db.query(UnidadTransporteModel).all()
    return {
        "capa": "B - Transporte",
        "total": len(unidades),
        "unidades": [{"id": u.id, "codigo": u.codigo_unidad, "tipo": u.tipo_vehiculo, "capacidad": u.capacidad_carga, "estado": u.estado} for u in unidades]
    }

@router.post("/flota")
def crear_unidad(unidad: UnidadSchema, db: Session = Depends(get_db)):
    nueva = UnidadTransporteModel(
        codigo_unidad=unidad.codigo_unidad,
        tipo_vehiculo=unidad.tipo_vehiculo,
        capacidad_carga=unidad.capacidad_carga,
        estado=unidad.estado
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Unidad de transporte registrada con éxito", "unidad": {"id": nueva.id, "codigo": nueva.codigo_unidad}}