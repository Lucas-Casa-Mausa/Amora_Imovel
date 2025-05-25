from schemas.simulacao import SimulacaoOutput, SimulacaoInput
from exceptions.exceptions import SimulacaoError

def calcular_financiamento(dados: SimulacaoInput) -> SimulacaoOutput:
    try:
        valor_imovel = float(dados.valor_imovel)
        percentual = dados.percentual_entrada
        anos = dados.anos_contrato

        if percentual < 5 or percentual > 20:
            raise SimulacaoError("Percentual de entrada deve ser entre 5 e 20%.")

        if anos < 1 or anos > 5:
            raise SimulacaoError("Duração do contrato deve ser entre 1 e 5 anos.")

        valor_entrada = dados.valor_imovel * (dados.percentual_entrada / 100)
        valor_financiado = dados.valor_imovel - valor_entrada
        total_a_guardar = dados.valor_imovel * 0.15
        parcela_mensal = total_a_guardar / (dados.anos_contrato * 12)

        return SimulacaoOutput(
            valor_entrada=round(valor_entrada, 2),
            valor_financiado=round(valor_financiado, 2),
            total_a_guardar=round(total_a_guardar,2),
            parcela_mensal=round(parcela_mensal, 2)
        )

    except ValueError as e:
        raise SimulacaoError("Todos os valores devem ser numéricos e válidos.")