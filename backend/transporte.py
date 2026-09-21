from fastapi import APIRouter

router = APIRouter(prefix="/capa-b", tags=["Capa B - Transporte"])

@router.get("/flota")
def obtener_flota_unidades():
    """Retorna la información de flota, unidades y disponibilidad operativa de la Capa B"""
    return {
        "capa": "B - Transporte",
        "descripcion": "Gestión de flota, unidades y directrices de transporte de MERA Advisor",
        "unidades": [
            "Monitoreo de disponibilidad y estatus de flota vehicular",
            "Validación de capacidad de carga y restricciones de ruta",
            "Asignación óptima de unidades según la demanda logística"
        ]
    }
