import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from engine.payroll import calcular_folha
from engine.previdencia import calcular_rpps
from engine.risco import avaliar_risco

def rodar_simulacao(dados):
    folha_atual = calcular_folha(dados["professores"], dados["salario_atual"])
    folha_nova = calcular_folha(dados["professores"], dados["piso"])

    aumento = folha_nova - folha_atual
    percentual = (aumento / folha_atual) * 100

    rpps_atual = calcular_rpps(folha_atual, dados["aliquota_rpps"])
    rpps_novo = calcular_rpps(folha_nova, dados["aliquota_rpps"])

    risco = avaliar_risco(percentual)

    return {
        "Folha Atual": folha_atual,
        "Folha Nova": folha_nova,
        "Aumento (%)": round(percentual, 2),
        "RPPS Atual": rpps_atual,
        "RPPS Novo": rpps_novo,
        "Risco": risco
    }



