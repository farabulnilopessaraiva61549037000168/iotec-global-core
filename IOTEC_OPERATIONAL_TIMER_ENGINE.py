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
DIAS_CICLO = 30

ARQUIVO = ROOT / "IOTEC_PORTFOLIO_RISK_REPORT.json"

if not ARQUIVO.exists():
    pass

    print("PORTFOLIO RISK REPORT NAO ENCONTRADO")
    raise SystemExit

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

melhor = dados["carteiras"][0]

receita_alvo = melhor["receita_realista"]

cronograma = []

for dia in range(1, DIAS_CICLO + 1):
    pass

    percentual = dia / DIAS_CICLO

    receita_esperada = round(
        receita_alvo * percentual,
        2
    )

    cronograma.append({

        "dia":
            dia,

        "percentual":
            round(
                percentual * 100,
                2
            ),

        "receita_esperada":
            receita_esperada,

        "status":
            "AGUARDANDO"
    })

resultado = {

    "gerado_em":
        str(datetime.now()),

    "portfolio_ativo":
        melhor["portfolio"],

    "receita_alvo":
        receita_alvo,

    "dias":
        DIAS_CICLO,

    "cronograma":
        cronograma
}

SAIDA = (
    ROOT /
    "IOTEC_OPERATIONAL_TIMER_REPORT.json"
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

print("\nOPERATIONAL TIMER ENGINE\n")

print(
    "PORTFOLIO ATIVO:",
    melhor["portfolio"]
)

print(
    "RECEITA ALVO:",
    f"R$ {receita_alvo:,.2f}"
)

print(
    "DIAS:",
    DIAS_CICLO
)

print(
    "\nMARCOS:"
)

for marco in [1,7,15,21,30]:
    pass

    item = cronograma[marco-1]

    print(
        f"DIA {item['dia']} "
        f"-> "
        f"R$ {item['receita_esperada']:,.2f}"
    )

print("\nARQUIVO:")
print(SAIDA)




