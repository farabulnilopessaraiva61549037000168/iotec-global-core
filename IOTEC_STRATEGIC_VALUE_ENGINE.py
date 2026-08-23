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

ARQUIVO = ROOT / "IOTEC_REAL_OFFER_DISCOVERY_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("RELATORIO NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

PESOS = {

    "Analise de Dados": {
        "ticket": 15000,
        "margem": 0.70,
        "capacidade": 20
    },

    "Agentes IA": {
        "ticket": 25000,
        "margem": 0.80,
        "capacidade": 10
    },

    "Sistema Interno": {
        "ticket": 50000,
        "margem": 0.60,
        "capacidade": 5
    },

    "Dashboard Executivo": {
        "ticket": 12000,
        "margem": 0.75,
        "capacidade": 15
    },

    "Captacao Comercial": {
        "ticket": 8000,
        "margem": 0.50,
        "capacidade": 20
    },

    "Automacao Educacional": {
        "ticket": 3000,
        "margem": 0.80,
        "capacidade": 50
    },

    "Geracao de Provas": {
        "ticket": 500,
        "margem": 0.90,
        "capacidade": 500
    }
}

resultado = {

    "gerado_em": str(datetime.now()),

    "ranking_economico": []
}

for item in dados["ofertas_detectadas"]:
    pass

    nome = item["oferta"]

    evidencias = item["evidencias"]

    if nome not in PESOS:
        continue

    ticket = PESOS[nome]["ticket"]
    margem = PESOS[nome]["margem"]
    capacidade = PESOS[nome]["capacidade"]

    receita_maxima = (
        ticket *
        capacidade
    )

    lucro_maximo = (
        receita_maxima *
        margem
    )

    score = (
        evidencias *
        margem
    )

    resultado["ranking_economico"].append({

        "oferta": nome,

        "evidencias": evidencias,

        "ticket": ticket,

        "capacidade": capacidade,

        "receita_maxima": receita_maxima,

        "lucro_maximo": lucro_maximo,

        "score": round(score, 2)
    })

resultado["ranking_economico"] = sorted(

    resultado["ranking_economico"],

    key=lambda x: x["score"],

    reverse=True
)

SAIDA = (
    ROOT /
    "IOTEC_STRATEGIC_VALUE_REPORT.json"
)

with open(
    SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nSTRATEGIC VALUE ENGINE\n")

print(
    "OFERTAS:",
    len(resultado["ranking_economico"])
)

print("\nRANKING:\n")

for item in resultado["ranking_economico"][:10]:
    pass

    print(
        f"{item['oferta']} "
        f"-> SCORE {item['score']}"
    )

print("\nARQUIVO:")
print(SAIDA)




