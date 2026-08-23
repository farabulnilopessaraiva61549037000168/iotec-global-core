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

ARQUIVO = ROOT / "IOTEC_STRATEGIC_VALUE_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("RELATORIO ESTRATEGICO NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

CATALOGO = {

    "Analise de Dados": [

        {
            "produto": "Painel Executivo",
            "ticket": 5000
        },

        {
            "produto": "Relatorio Gerencial",
            "ticket": 3000
        },

        {
            "produto": "Previsao de Indicadores",
            "ticket": 8000
        },

        {
            "produto": "Monitoramento Operacional",
            "ticket": 12000
        }
    ],

    "Agentes IA": [

        {
            "produto": "Agente Comercial",
            "ticket": 15000
        },

        {
            "produto": "Agente Atendimento",
            "ticket": 12000
        },

        {
            "produto": "Agente Educacional",
            "ticket": 10000
        },

        {
            "produto": "Agente Auditor",
            "ticket": 25000
        }
    ],

    "Sistema Interno": [

        {
            "produto": "Sistema de Controle",
            "ticket": 30000
        },

        {
            "produto": "Plataforma Operacional",
            "ticket": 50000
        },

        {
            "produto": "Painel Corporativo",
            "ticket": 25000
        }
    ],

    "Dashboard Executivo": [

        {
            "produto": "Dashboard Power BI",
            "ticket": 8000
        },

        {
            "produto": "Painel KPI",
            "ticket": 10000
        }
    ]
}

resultado = {

    "gerado_em": str(datetime.now()),

    "catalogo": []
}

for oferta in dados["ranking_economico"]:
    pass

    nome = oferta["oferta"]

    if nome not in CATALOGO:
        continue

    resultado["catalogo"].append({

        "oferta": nome,

        "score": oferta["score"],

        "produtos": CATALOGO[nome]
    })

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_PRODUCT_CATALOG_REPORT.json"
)

with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nPRODUCT CATALOG ENGINE\n")

print(
    "OFERTAS:",
    len(resultado["catalogo"])
)

print("\nCATALOGO:\n")

for item in resultado["catalogo"]:
    pass

    print(
        item["oferta"],
        "->",
        len(item["produtos"]),
        "produtos"
    )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)




