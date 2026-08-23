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

resultado = {

    "gerado_em": str(datetime.now()),

    "carteiras": []
}

for portfolio in dados["portfolios"]:
    pass

    vendas = portfolio["vendas"]

    receita = portfolio["receita"]

    if vendas <= 3:
        pass

        risco = "ALTO"
        resiliencia = 20
        classificacao = "ALTO_TICKET"

    elif vendas <= 10:
        pass

        risco = "MEDIO"
        resiliencia = 60
        classificacao = "EQUILIBRADO"

    else:
        pass

        risco = "BAIXO"
        resiliencia = 90
        classificacao = "ESCALAVEL"

    receita_pessimista = round(
        receita * 0.50,
        2
    )

    receita_conservadora = round(
        receita * 0.75,
        2
    )

    receita_realista = round(
        receita * 0.90,
        2
    )

    receita_otimista = round(
        receita * 1.10,
        2
    )

    resultado["carteiras"].append({

        "portfolio":
            portfolio["nome"],

        "receita":
            receita,

        "vendas":
            vendas,

        "risco":
            risco,

        "resiliencia":
            resiliencia,

        "classificacao":
            classificacao,

        "receita_pessimista":
            receita_pessimista,

        "receita_conservadora":
            receita_conservadora,

        "receita_realista":
            receita_realista,

        "receita_otimista":
            receita_otimista
    })

resultado["carteiras"] = sorted(

    resultado["carteiras"],

    key=lambda x: (
        -x["receita_realista"],
        -x["resiliencia"]
    )
)

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_PORTFOLIO_RISK_REPORT.json"
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

print("\nPORTFOLIO RISK ENGINE\n")

print(
    "CARTEIRAS:",
    len(resultado["carteiras"])
)

print("\nRANKING:\n")

for item in resultado["carteiras"]:
    pass

    print(
        f"{item['portfolio']} | "
        f"RISCO={item['risco']} | "
        f"RESILIENCIA={item['resiliencia']} | "
        f"REALISTA=R$ {item['receita_realista']:,.2f}"
    )

print("\nARQUIVO:")
print(ARQUIVO_SAIDA)


