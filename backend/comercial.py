from fastapi import APIRouter

router = APIRouter(prefix="/capa-a", tags=["Capa A - Comercial"])

@router.get("/politicas")
def obtener_politicas_comerciales():
    """Retorna las políticas comerciales y directrices de venta de la Capa A"""
    return {
        "capa": "A - Comercial",
        "descripcion": "Políticas comerciales y directrices de venta de MERA Advisor",
        "politicas": [
            "Optimización de márgenes en cotizaciones de flotas",
            "Validación de descuentos por volumen para clientes frecuentes",
            "Alineación de propuestas con directrices de disponibilidad operativa"
        ]
    }