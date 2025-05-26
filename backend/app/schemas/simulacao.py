from pydantic import BaseModel, Field


class SimulacaoInput(BaseModel):
    valor_imovel: float = Field(ge=0, description="Valor do imóvel")
    percentual_entrada: float = Field(
        ge=5, le=20, description="Percentual de entrada (5 a 20)"
    )
    anos_contrato: int = Field(
        ge=1, le=5, description="Duração do contrato (1 a 5 anos)"
    )


class SimulacaoOutput(BaseModel):
    valor_entrada: float
    valor_financiado: float
    total_a_guardar: float
    parcela_mensal: float
