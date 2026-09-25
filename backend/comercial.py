from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.database import SessionLocal
from backend.models import PoliticaComercialModel

router = APIRouter(prefix="/capa-a", tags=["Capa A - Comercial"])

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Esquema Pydantic para validar los datos que recibimos al crear una política
class PoliticaSchema(BaseModel):
    titulo: str
    descripcion: str

@router.get("/politicas")
def obtener_politicas_comerciales(db: Session = Depends(get_db)):
    """Retorna las políticas comerciales almacenadas en PostgreSQL"""
    politicas = db.query(PoliticaComercialModel).all()
    
    if not politicas:
        return {
            "capa": "A - Comercial",
            "mensaje": "Aún no hay políticas comerciales registradas en la base de datos.",
            "politicas": []
        }
        
    return {
        "capa": "A - Comercial",
        "total": len(politicas),
        "politicas": [
            {
                "id": p.id,
                "titulo": p.titulo,
                "descripcion": p.descripcion,
                "fecha_creacion": str(p.fecha_creacion)
            } for p in politicas
        ]
    }

@router.post("/politicas")
def crear_politica_comercial(politica: PoliticaSchema, db: Session = Depends(get_db)):
    """Guarda una nueva política comercial en PostgreSQL"""
    nueva_politica = PoliticaComercialModel(
        titulo=politica.titulo,
        descripcion=politica.descripcion
    )
    db.add(nueva_politica)
    db.commit()
    db.refresh(nueva_politica)
    
    return {
        "mensaje": "Política comercial creada y guardada con éxito en la base de datos",
        "politica": {
            "id": nueva_politica.id,
            "titulo": nueva_politica.titulo,
            "descripcion": nueva_politica.descripcion
        }
    }