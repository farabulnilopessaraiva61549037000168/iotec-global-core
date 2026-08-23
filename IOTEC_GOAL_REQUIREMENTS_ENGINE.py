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

META_FINANCEIRA = 100000

TICKET_MEDIO_REFERENCIA = 2000

TAXA_CONVERSAO_REFERENCIA = 0.10

vendas_necessarias = int(
    META_FINANCEIRA /
    TICKET_MEDIO_REFERENCIA
)

oportunidades_necessarias = int(
    vendas_necessarias /
    TAXA_CONVERSAO_REFERENCIA
)

relatorio = {

    "gerado_em": str(datetime.now()),

    "meta_financeira":
        META_FINANCEIRA,

    "ticket_medio":
        TICKET_MEDIO_REFERENCIA,

    "taxa_conversao":
        TAXA_CONVERSAO_REFERENCIA,

    "vendas_necessarias":
        vendas_necessarias,

    "oportunidades_necessarias":
        oportunidades_necessarias,

    "necessidades": {

        "EMPRESAS": {

            "minimo": oportunidades_necessarias,

            "status": "NECESSARIO"
        },

        "ESCOLAS": {

            "minimo": 20,

            "status": "NECESSARIO"
        },

        "UNIVERSIDADES": {

            "minimo": 10,

            "status": "NECESSARIO"
        },

        "FORNECEDORES": {

            "minimo": 10,

            "status": "NECESSARIO"
        },

        "TERCEIRIZADAS": {

            "minimo": 10,

            "status": "NECESSARIO"
        },

        "PARCEIROS": {

            "minimo": 5,

            "status": "NECESSARIO"
        }
    }
}

ARQUIVO = (
    ROOT /
    "IOTEC_GOAL_REQUIREMENTS_REPORT.json"
)

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nGOAL REQUIREMENTS ENGINE\n")

print(
    "META:",
    f"R$ {META_FINANCEIRA:,.2f}"
)

print(
    "VENDAS NECESSARIAS:",
    vendas_necessarias
)

print(
    "OPORTUNIDADES NECESSARIAS:",
    oportunidades_necessarias
)

print(
    "\nNECESSIDADES:"
)

for categoria, dados in relatorio[
    "necessidades"
].items():

    print(
        categoria,
        "->",
        dados["minimo"]
    )

print(
    "\nARQUIVO:"
)

print(ARQUIVO)




