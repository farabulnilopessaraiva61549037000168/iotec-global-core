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

META_MENSAL = 100000.0

ARQUIVO_COCKPIT = (
    ROOT /
    "IOTEC_EXECUTIVE_COCKPIT.json"
)

if not ARQUIVO_COCKPIT.exists():
    pass

    print(
        "COCKPIT NAO ENCONTRADO"
    )

    raise SystemExit

with open(
    ARQUIVO_COCKPIT,
    "r",
    encoding="utf-8"
) as f:

    cockpit = json.load(f)

ARQUIVO_RECEITA = (
    ROOT /
    "IOTEC_REAL_REVENUE.json"
)

if ARQUIVO_RECEITA.exists():
    pass

    with open(
        ARQUIVO_RECEITA,
        "r",
        encoding="utf-8"
    ) as f:

        receita = json.load(f)

else:
    pass

    receita = {
        "eventos": []
    }

print(
    "\nREVENUE TRACKER ENGINE\n"
)

print(
    "META:",
    f"R$ {META_MENSAL:,.2f}"
)

valor = float(

    input(
        "VALOR RECEBIDO (R$): "
    )
)

descricao = input(
    "DESCRICAO: "
)

evento = {

    "data":
        str(datetime.now()),

    "descricao":
        descricao,

    "valor":
        valor
}

receita["eventos"].append(
    evento
)

total = sum(

    item["valor"]

    for item in receita["eventos"]
)

faltante = max(

    0,

    META_MENSAL - total
)

atingimento = round(

    (
        total /
        META_MENSAL
    ) * 100,

    2
)

status = "META_EM_ANDAMENTO"

if total >= META_MENSAL:
    pass

    status = "META_ATINGIDA"

resultado = {

    "gerado_em":
        str(datetime.now()),

    "meta":
        META_MENSAL,

    "receita_realizada":
        total,

    "faltante":
        faltante,

    "atingimento":
        atingimento,

    "status":
        status,

    "eventos":
        receita["eventos"]
}

with open(
    ARQUIVO_RECEITA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        receita,
        f,
        indent=4,
        ensure_ascii=False
    )

ARQUIVO_RELATORIO = (
    ROOT /
    "IOTEC_REVENUE_TRACKER_REPORT.json"
)

with open(
    ARQUIVO_RELATORIO,
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
    "\nRESULTADO\n"
)

print(
    "RECEITA REALIZADA:",
    f"R$ {total:,.2f}"
)

print(
    "FALTANTE:",
    f"R$ {faltante:,.2f}"
)

print(
    "ATINGIMENTO:",
    f"{atingimento}%"
)

print(
    "STATUS:",
    status
)

print(
    "\nARQUIVO:"
)

print(
    ARQUIVO_RELATORIO
)


