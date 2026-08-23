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

ARQUIVOS = {

    "risk":
        ROOT / "IOTEC_PORTFOLIO_RISK_REPORT.json",

    "goal":
        ROOT / "IOTEC_GOAL_EXECUTION_REPORT.json",

    "revenue":
        ROOT / "IOTEC_REVENUE_SCENARIO_REPORT.json"
}

for nome, arquivo in ARQUIVOS.items():
    pass

    if not arquivo.exists():
        pass

        print(
            f"ARQUIVO AUSENTE: {arquivo}"
        )

        raise SystemExit

with open(
    ARQUIVOS["risk"],
    "r",
    encoding="utf-8"
) as f:

    risk = json.load(f)

with open(
    ARQUIVOS["goal"],
    "r",
    encoding="utf-8"
) as f:

    goal = json.load(f)

with open(
    ARQUIVOS["revenue"],
    "r",
    encoding="utf-8"
) as f:

    revenue = json.load(f)

melhor_portfolio = risk["carteiras"][0]

melhor_cenario = revenue["cenarios"][0]

meta = goal["meta_mensal"]

receita_realista = (
    melhor_portfolio["receita_realista"]
)

atingimento = round(

    (
        receita_realista /
        meta
    ) * 100,

    2
)

dias = goal["dias_ciclo"]

receita_dia = round(

    receita_realista /
    dias,

    2
)

resultado = {

    "gerado_em":
        str(datetime.now()),

    "meta":
        meta,

    "portfolio_ativo":
        melhor_portfolio["portfolio"],

    "risco":
        melhor_portfolio["risco"],

    "resiliencia":
        melhor_portfolio["resiliencia"],

    "receita_realista":
        receita_realista,

    "atingimento_percentual":
        atingimento,

    "receita_media_dia":
        receita_dia,

    "produto_lider":
        melhor_cenario["produto"],

    "ticket_lider":
        melhor_cenario["ticket"],

    "vendas_meta":
        melhor_cenario["vendas_meta"],

    "status":
        (
            "META_ATINGIVEL"
            if atingimento >= 90
            else "META_EM_RISCO"
        )
}

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_EXECUTIVE_COCKPIT.json"
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

print(
    "\nEXECUTIVE COCKPIT\n"
)

print(
    "STATUS:",
    resultado["status"]
)

print(
    "META:",
    f"R$ {meta:,.2f}"
)

print(
    "PORTFOLIO:",
    resultado["portfolio_ativo"]
)

print(
    "RISCO:",
    resultado["risco"]
)

print(
    "RESILIENCIA:",
    resultado["resiliencia"]
)

print(
    "RECEITA REALISTA:",
    f"R$ {receita_realista:,.2f}"
)

print(
    "ATINGIMENTO:",
    f"{atingimento}%"
)

print(
    "RECEITA MEDIA/DIA:",
    f"R$ {receita_dia:,.2f}"
)

print(
    "PRODUTO LIDER:",
    resultado["produto_lider"]
)

print(
    "TICKET:",
    f"R$ {resultado['ticket_lider']:,.2f}"
)

print(
    "VENDAS NECESSARIAS:",
    resultado["vendas_meta"]
)

print(
    "\nARQUIVO:"
)

print(
    ARQUIVO_SAIDA
)


