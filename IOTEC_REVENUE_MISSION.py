import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

MISSION = {

    "nome":
        "GERAR_RECEITA_REAL",

    "descricao":
        "Transformar demanda real em receita real.",

    "simulacao":
        False,

    "dados_reais":
        True
}

PRIORIDADES = [

    "CAPTAR_DEMANDA",

    "GERAR_LEADS",

    "GERAR_OPORTUNIDADES",

    "GERAR_PROPOSTAS",

    "GERAR_FATURAS",

    "CONFIRMAR_PAGAMENTOS",

    "ENTREGAR_SERVICOS",

    "GERAR_RECEITA"

]

REGRAS = {

    "usar_dados_simulados":
        False,

    "usar_dados_reais":
        True,

    "reportar_falhas":
        True,

    "reportar_oportunidades":
        True,

    "reportar_receita":
        True
}

print("")
print("===================================")
print("IOTEC REVENUE MISSION")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(MISSION["descricao"])

print("")
print("PRIORIDADES:")

for item in PRIORIDADES:
    pass

    print(
        "-",
        item
    )

print("")
print("REGRAS:")

for regra, valor in REGRAS.items():
    pass

    print(
        regra.upper(),
        "->",
        valor
    )

print("")
print("ORDEM MOR:")
print(
    "TRANSFORMAR DEMANDA REAL "
    "EM RECEITA REAL"
)

print("")
print("NUCLEO ORIENTADO PARA RECEITA")




