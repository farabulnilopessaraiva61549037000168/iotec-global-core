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

COMPONENTES = {

    "WAR_ROOM":
        ROOT / "IOTEC_WAR_ROOM_DATABASE.json",

    "COCKPIT":
        ROOT / "IOTEC_EXECUTIVE_COCKPIT.json",

    "REVENUE_TRACKER":
        ROOT / "IOTEC_REVENUE_TRACKER_REPORT.json",

    "GOAL_DEVIATION":
        ROOT / "IOTEC_GOAL_DEVIATION_REPORT.json"
}

resultado = {

    "gerado_em":
        str(datetime.now()),

    "status":
        "INICIALIZANDO",

    "componentes": {},

    "fontes": {

        "email": False,
        "whatsapp": False,
        "site": False,
        "paypal": False,
        "pix": False
    }
}

ativos = 0

for nome, arquivo in COMPONENTES.items():
    pass

    existe = arquivo.exists()

    resultado["componentes"][nome] = existe

    if existe:
        ativos += 1

resultado["componentes_ativos"] = ativos

resultado["componentes_totais"] = len(
    COMPONENTES
)

if ativos == len(COMPONENTES):
    pass

    resultado["status"] = "OPERACIONAL"

else:
    pass

    resultado["status"] = "PARCIAL"

ARQUIVO = (
    ROOT /
    "IOTEC_OPERATION_STATUS.json"
)

with open(
    ARQUIVO,
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
    "\nIOTEC OPERATION START ENGINE\n"
)

print(
    "STATUS:",
    resultado["status"]
)

print(
    "\nCOMPONENTES:\n"
)

for nome, valor in resultado["componentes"].items():
    pass

    print(
        f"{nome} -> "
        f"{'ONLINE' if valor else 'OFFLINE'}"
    )

print(
    "\nATIVOS:",
    ativos,
    "/",
    len(COMPONENTES)
)

print(
    "\nARQUIVO:"
)

print(
    ARQUIVO
)




