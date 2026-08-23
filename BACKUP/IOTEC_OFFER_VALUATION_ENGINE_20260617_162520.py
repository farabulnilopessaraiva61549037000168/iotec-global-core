import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ofertas = [

    {
        "nome": "Automacao Educacional",
        "ticket": 5000,
        "margem": 0.40,
        "capacidade_mensal": 20
    },

    {
        "nome": "Geracao de Provas",
        "ticket": 500,
        "margem": 0.90,
        "capacidade_mensal": 500
    },

    {
        "nome": "Dashboard Executivo",
        "ticket": 15000,
        "margem": 0.60,
        "capacidade_mensal": 10
    },

    {
        "nome": "Consultoria",
        "ticket": 10000,
        "margem": 0.80,
        "capacidade_mensal": 15
    },

    {
        "nome": "Projeto Sob Demanda",
        "ticket": 50000,
        "margem": 0.50,
        "capacidade_mensal": 4
    }
]

resultado = {

    "gerado_em": str(datetime.now()),

    "ofertas": []
}

for oferta in ofertas:
    pass

    receita_maxima = (
        oferta["ticket"] *
        oferta["capacidade_mensal"]
    )

    lucro_maximo = (
        receita_maxima *
        oferta["margem"]
    )

    score = (
        receita_maxima *
        oferta["margem"]
    )

    resultado["ofertas"].append({

        "nome":
            oferta["nome"],

        "ticket":
            oferta["ticket"],

        "margem":
            oferta["margem"],

        "capacidade":
            oferta["capacidade_mensal"],

        "receita_maxima":
            receita_maxima,

        "lucro_maximo":
            lucro_maximo,

        "score":
            score
    })

resultado["ofertas"] = sorted(

    resultado["ofertas"],

    key=lambda x: x["score"],

    reverse=True
)

ARQUIVO = (
    ROOT /
    "IOTEC_OFFER_VALUATION_REPORT.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nOFFER VALUATION ENGINE\n")

print(
    "OFERTAS:",
    len(resultado["ofertas"])
)

print("\nRANKING:\n")

for item in resultado["ofertas"]:
    pass

    print(
        item["nome"],
        "-> SCORE:",
        round(item["score"], 2)
    )

print("\nARQUIVO:")

print(ARQUIVO)


