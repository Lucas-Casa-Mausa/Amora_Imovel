from fastapi import APIRouter, HTTPException
from schemas.simulacao import SimulacaoInput, SimulacaoOutput
from services.calculos import calcular_financiamento
from exceptions.exceptions import SimulacaoError

router = APIRouter(tags=["Simulação"])


@router.post("/simulacao", response_model=SimulacaoOutput)
async def simular_financiamento(dados: SimulacaoInput):
    try:
        return calcular_financiamento(dados)
    except SimulacaoError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno do servidor.")
