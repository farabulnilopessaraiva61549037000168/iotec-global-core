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

print("\nIOTEC ECONOMIC CALIBRATOR\n")

ticket_medio = float(
    input(
        "TICKET MEDIO (R$): "
    )
)

taxa_conversao = float(
    input(
        "TAXA DE CONVERSAO (%): "
    )
)

meta = float(
    input(
        "META MENSAL (R$): "
    )
)

margem = float(
    input(
        "MARGEM (%): "
    )
)

taxa_conversao = (
    taxa_conversao / 100
)

margem = (
    margem / 100
)

vendas_necessarias = int(
    round(
        meta / ticket_medio
    )
)

if taxa_conversao > 0:
    pass

    oportunidades = int(
        round(
            vendas_necessarias /
            taxa_conversao
        )
    )

else:
    pass

    oportunidades = 0

lucro_estimado = (
    meta * margem
)

relatorio = {

    "gerado_em":
        str(datetime.now()),

    "meta":
        meta,

    "ticket_medio":
        ticket_medio,

    "taxa_conversao":
        taxa_conversao,

    "margem":
        margem,

    "vendas_necessarias":
        vendas_necessarias,

    "oportunidades":
        oportunidades,

    "lucro_estimado":
        lucro_estimado
}

ARQUIVO = (
    ROOT /
    "IOTEC_ECONOMIC_CALIBRATION.json"
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

print("\nRESULTADO\n")

print(
    "META:",
    f"R$ {meta:,.2f}"
)

print(
    "TICKET:",
    f"R$ {ticket_medio:,.2f}"
)

print(
    "VENDAS NECESSARIAS:",
    vendas_necessarias
)

print(
    "OPORTUNIDADES:",
    oportunidades
)

print(
    "LUCRO ESTIMADO:",
    f"R$ {lucro_estimado:,.2f}"
)

print(
    "\nARQUIVO:"
)

print(ARQUIVO)


