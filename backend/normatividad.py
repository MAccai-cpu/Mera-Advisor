from fastapi import APIRouter

router = APIRouter(prefix="/capa-e", tags=["Capa E - Normatividad"])

@router.get("/marco")
def obtener_marco_regulatorio():
    """Retorna el marco regulatorio y normatividad de la Capa E"""
    return {
        "capa": "E - Normatividad",
        "descripcion": "Marco regulatorio y cumplimiento normativo de MERA Advisor",
        "normas": [
            "Cumplimiento de normativas de transporte y vialidad aplicables",
            "Alineación con regulaciones fiscales y comerciales vigentes",
            "Auditoría y control de estándares de calidad corporativa"
        ]
    }