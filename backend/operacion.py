from fastapi import APIRouter

router = APIRouter(prefix="/capa-c", tags=["Capa C - Operación"])

@router.get("/directrices")
def obtener_directrices_operativas():
    """Retorna las directrices operativas de la Capa C"""
    return {
        "capa": "C - Operación",
        "descripcion": "Directrices operativas y de ejecución de MERA Advisor",
        "directrices": [
            "Supervisión y control de procesos logísticos diarios",
            "Coordinación de tiempos de entrega y asignación de recursos",
            "Mitigación de cuellos de botella en la cadena operativa"
        ]
    }