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

META = 100000.0

ARQUIVO = ROOT / "IOTEC_REVENUE_SCENARIO_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("REVENUE REPORT NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

resultado = {

    "gerado_em": str(datetime.now()),

    "meta": META,

    "portfolios": []
}

produtos = dados["cenarios"]

# ==========================
# PORTFOLIO 1
# EQUILIBRADO
# ==========================

portfolio_1 = {

    "nome":
        "EQUILIBRADO",

    "componentes": [

        {
            "produto":
                "Agente Comercial",

            "quantidade":
                4,

            "ticket":
                15000
        },

        {
            "produto":
                "Painel Executivo",

            "quantidade":
                4,

            "ticket":
                5000
        },

        {
            "produto":
                "Dashboard Power BI",

            "quantidade":
                2,

            "ticket":
                8000
        }
    ]
}

# ==========================
# PORTFOLIO 2
# ALTO TICKET
# ==========================

portfolio_2 = {

    "nome":
        "ALTO_TICKET",

    "componentes": [

        {
            "produto":
                "Plataforma Operacional",

            "quantidade":
                1,

            "ticket":
                50000
        },

        {
            "produto":
                "Sistema de Controle",

            "quantidade":
                2,

            "ticket":
                30000
        }
    ]
}

# ==========================
# PORTFOLIO 3
# ESCALAVEL
# ==========================

portfolio_3 = {

    "nome":
        "ESCALAVEL",

    "componentes": [

        {
            "produto":
                "Painel Executivo",

            "quantidade":
                10,

            "ticket":
                5000
        },

        {
            "produto":
                "Relatorio Gerencial",

            "quantidade":
                15,

            "ticket":
                3000
        },

        {
            "produto":
                "Dashboard Power BI",

            "quantidade":
                2,

            "ticket":
                8000
        }
    ]
}

for portfolio in [

    portfolio_1,
    portfolio_2,
    portfolio_3

]:

    receita = 0

    vendas = 0

    for item in portfolio["componentes"]:
        pass

        receita += (
            item["ticket"]
            *
            item["quantidade"]
        )

        vendas += (
            item["quantidade"]
        )

    atinge_meta = (
        receita >= META
    )

    resultado["portfolios"].append({

        "nome":
            portfolio["nome"],

        "receita":
            receita,

        "vendas":
            vendas,

        "atinge_meta":
            atinge_meta,

        "gap":
            round(
                META - receita,
                2
            )
    })

resultado["portfolios"] = sorted(

    resultado["portfolios"],

    key=lambda x: x["receita"],

    reverse=True
)

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_PORTFOLIO_GOAL_REPORT.json"
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

print("\nPORTFOLIO GOAL ENGINE\n")

print(
    "META:",
    f"R$ {META:,.2f}"
)

print("\nPORTFOLIOS:\n")

for p in resultado["portfolios"]:
    pass

    print(
        f"{p['nome']} "
        f"-> Receita: R$ {p['receita']:,.2f} "
        f"| Vendas: {p['vendas']} "
        f"| Meta: {p['atinge_meta']}"
    )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)




