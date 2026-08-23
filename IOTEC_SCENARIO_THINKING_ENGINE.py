import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

EVENTO = "ESTIAGEM"

impactos = {

    "ABASTECIMENTO":
        "ALTO",

    "AGRICULTURA":
        "ALTO",

    "PECUARIA":
        "ALTO",

    "ENERGIA":
        "MEDIO",

    "TURISMO":
        "MEDIO",

    "COMERCIO":
        "MEDIO"
}

produtos = [

    "MAPA_DE_RISCO",

    "PLANO_DE_CONTINGENCIA",

    "PAINEL_EXECUTIVO",

    "ANALISE_DE_CENARIOS",

    "MODELAGEM_MATEMATICA"
]

print("")
print("===================================")
print("IOTEC SCENARIO THINKING ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("EVENTO:")
print(EVENTO)

print("")
print("IMPACTOS:")

for setor, risco in impactos.items():
    pass

    print(
        setor,
        "->",
        risco
    )

print("")
print("PRODUTOS GERAVEIS:")

for produto in produtos:
    pass

    print(
        "-",
        produto
    )

print("")
print("LOGICA OPERACIONAL:")
print("IDENTIFICAR RISCOS")
print("CALCULAR IMPACTOS")
print("MAPEAR SETORES")
print("GERAR SOLUCOES")
print("GERAR RECEITA")

print("")
print("NUCLEO ESTRATEGICO ATIVO")




