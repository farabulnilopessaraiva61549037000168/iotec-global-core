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

WAR_ROOM = ROOT / "IOTEC_WAR_ROOM_DATABASE.json"

CHANNELS = [
    "WHATSAPP",
    "FORMULARIO",
    "SITE",
    "PORTAL",
    "EMAIL",
    "REDES_SOCIAIS",
    "INDICACAO"
]

print("")
print("===================================")
print("IOTEC CHANNEL STATUS")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

status = {}

for canal in CHANNELS:
    pass

    status[canal] = {
        "oportunidades": 0,
        "operacoes": 0
    }

try:
    pass

    with open(
        WAR_ROOM,
        "r",
        encoding="utf-8-sig"
    ) as f:

        db = json.load(f)

    oportunidades = db.get(
        "oportunidades",
        []
    )

    operacoes = db.get(
        "operacoes",
        []
    )

    for op in oportunidades:
        pass

        origem = (
            op.get(
                "origem",
                "DESCONHECIDA"
            )
            .upper()
            .strip()
        )

        if origem not in status:
            pass

            status[origem] = {
                "oportunidades": 0,
                "operacoes": 0
            }

        status[origem][
            "oportunidades"
        ] += 1

    for op in operacoes:
        pass

        origem = (
            op.get(
                "origem",
                "DESCONHECIDA"
            )
            .upper()
            .strip()
        )

        if origem not in status:
            pass

            status[origem] = {
                "oportunidades": 0,
                "operacoes": 0
            }

        status[origem][
            "operacoes"
        ] += 1

except Exception as erro:
    pass

    print("")
    print("ERRO:")
    print(erro)

print("")
print("===================================")
print("CANAIS")
print("===================================")

for canal, dados in status.items():
    pass

    print("")

    print(canal)

    print(
        "OPORTUNIDADES:",
        dados["oportunidades"]
    )

    print(
        "OPERACOES:",
        dados["operacoes"]
    )

print("")
print("===================================")
print("RESUMO")
print("===================================")

ativos = 0

for canal, dados in status.items():
    pass

    if (
        dados["oportunidades"] > 0
        or
        dados["operacoes"] > 0
    ):
        ativos += 1

print(
    "CANAIS ATIVOS:",
    ativos
)

print(
    "CANAIS MONITORADOS:",
    len(status)
)

print("")
print("===================================")
print("MISSAO")
print("===================================")

print(
    "IDENTIFICAR QUAIS CANAIS"
)

print(
    "GERAM OPORTUNIDADES"
)

print(
    "GERAM OPERACOES"
)

print(
    "GERAM RECEITA"
)

print("")
print("STATUS FINALIZADO")




