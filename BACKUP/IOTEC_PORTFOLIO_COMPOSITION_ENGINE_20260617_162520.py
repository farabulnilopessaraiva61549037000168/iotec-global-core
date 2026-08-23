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

ARQUIVO = ROOT / "IOTEC_PORTFOLIO_GOAL_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("PORTFOLIO REPORT NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

# =====================================
# COMPOSICAO CONHECIDA DOS PORTFOLIOS
# =====================================

COMPOSICOES = {

    "ESCALAVEL": [

        {
            "produto": "Painel Executivo",
            "receita": 50000
        },

        {
            "produto": "Relatorio Gerencial",
            "receita": 45000
        },

        {
            "produto": "Dashboard Power BI",
            "receita": 16000
        }
    ],

    "ALTO_TICKET": [

        {
            "produto": "Plataforma Operacional",
            "receita": 50000
        },

        {
            "produto": "Sistema de Controle",
            "receita": 60000
        }
    ],

    "EQUILIBRADO": [

        {
            "produto": "Agente Comercial",
            "receita": 60000
        },

        {
            "produto": "Painel Executivo",
            "receita": 20000
        },

        {
            "produto": "Dashboard Power BI",
            "receita": 16000
        }
    ]
}

resultado = {

    "gerado_em": str(datetime.now()),

    "portfolios": []
}

for portfolio in dados["portfolios"]:
    pass

    nome = portfolio["nome"]

    receita_total = portfolio["receita"]

    componentes = []

    if nome not in COMPOSICOES:
        continue

    for item in COMPOSICOES[nome]:
        pass

        percentual = round(

            (
                item["receita"] /
                receita_total
            ) * 100,

            2
        )

        componentes.append({

            "produto":
                item["produto"],

            "receita":
                item["receita"],

            "percentual":
                percentual
        })

    componentes = sorted(

        componentes,

        key=lambda x: x["receita"],

        reverse=True
    )

    produto_lider = componentes[0]

    resultado["portfolios"].append({

        "portfolio":
            nome,

        "receita_total":
            receita_total,

        "produto_lider":
            produto_lider["produto"],

        "participacao_lider":
            produto_lider["percentual"],

        "componentes":
            componentes
    })

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_PORTFOLIO_COMPOSITION_REPORT.json"
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

print("\nPORTFOLIO COMPOSITION ENGINE\n")

for portfolio in resultado["portfolios"]:
    pass

    print(
        f"\n{portfolio['portfolio']}"
    )

    print(
        f"RECEITA: "
        f"R$ {portfolio['receita_total']:,.2f}"
    )

    print(
        f"LIDER: "
        f"{portfolio['produto_lider']}"
    )

    print(
        f"PARTICIPACAO: "
        f"{portfolio['participacao_lider']}%"
    )

    print(
        "\nCOMPONENTES:"
    )

    for item in portfolio["componentes"]:
        pass

        print(
            f"  {item['produto']} "
            f"-> {item['percentual']}%"
        )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)


