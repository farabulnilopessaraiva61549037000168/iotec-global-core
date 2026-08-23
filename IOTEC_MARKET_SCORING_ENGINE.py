import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime

print("")
print("===================================")
print("IOTEC MARKET SCORING ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(
    "PRIORIZAR OPORTUNIDADES "
    "POR POTENCIAL DE MERCADO"
)

oportunidades = [

    {
        "nome":"ESTIAGEM",
        "impacto":10,
        "urgencia":10,
        "orcamento":8,
        "concorrencia":5
    },

    {
        "nome":"ENCHENTE",
        "impacto":9,
        "urgencia":9,
        "orcamento":8,
        "concorrencia":6
    },

    {
        "nome":"PAINEL_EXECUTIVO",
        "impacto":7,
        "urgencia":6,
        "orcamento":8,
        "concorrencia":7
    },

    {
        "nome":"MODELAGEM_MATEMATICA",
        "impacto":9,
        "urgencia":7,
        "orcamento":9,
        "concorrencia":3
    },

    {
        "nome":"INTELIGENCIA_COMERCIAL",
        "impacto":8,
        "urgencia":8,
        "orcamento":8,
        "concorrencia":6
    }
]

for item in oportunidades:
    pass

    score = (
        item["impacto"] +
        item["urgencia"] +
        item["orcamento"] -
        item["concorrencia"]
    )

    item["score"] = score

ranking = sorted(
    oportunidades,
    key=lambda x: x["score"],
    reverse=True
)

print("")
print("===================================")
print("RANKING DE OPORTUNIDADES")
print("===================================")

posicao = 1

for item in ranking:
    pass

    print("")
    print(f"#{posicao}")

    print("OPORTUNIDADE:")
    print(item["nome"])

    print("IMPACTO:")
    print(item["impacto"])

    print("URGENCIA:")
    print(item["urgencia"])

    print("ORCAMENTO:")
    print(item["orcamento"])

    print("CONCORRENCIA:")
    print(item["concorrencia"])

    print("SCORE:")
    print(item["score"])

    posicao += 1

print("")
print("===================================")
print("FORMULA")
print("===================================")

print("IMPACTO")
print("+")
print("URGENCIA")
print("+")
print("ORCAMENTO")
print("-")
print("CONCORRENCIA")
print("=")
print("PRIORIDADE")

print("")
print("===================================")
print("MISSAO DO NUCLEO")
print("===================================")

print(
    "ATACAR PRIMEIRO "
    "AS OPORTUNIDADES "
    "COM MAIOR SCORE."
)

print("")
print("PERGUNTA CENTRAL:")
print(
    "ONDE EXISTE DOR, "
    "ORCAMENTO E BAIXA CONCORRENCIA?"
)

print("")
print("MARKET SCORING ENGINE ATIVO")




