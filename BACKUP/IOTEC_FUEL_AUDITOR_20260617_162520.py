import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_FUEL_AUDITOR.py

from pathlib import Path
import json
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

resultado = {
    "data": str(datetime.now()),
    "fontes": [],
    "vazias": [],
    "ativas": [],
    "json": [],
    "db": [],
    "resumo": {}
}

# JSON

for arq in ROOT.rglob("*.json"):
    pass

    try:
        pass

        tamanho = arq.stat().st_size

        resultado["json"].append({
            "arquivo": arq.name,
            "bytes": tamanho
        })

        if tamanho == 0:
            resultado["vazias"].append(arq.name)

        else:
            resultado["ativas"].append(arq.name)

    except:
        pass

# DB

for arq in ROOT.rglob("*.db"):
    pass

    try:
        pass

        tamanho = arq.stat().st_size

        resultado["db"].append({
            "arquivo": arq.name,
            "bytes": tamanho
        })

        if tamanho == 0:
            resultado["vazias"].append(arq.name)

        else:
            resultado["ativas"].append(arq.name)

    except:
        pass

resultado["resumo"] = {

    "fontes_ativas":
        len(resultado["ativas"]),

    "fontes_vazias":
        len(resultado["vazias"]),

    "json":
        len(resultado["json"]),

    "db":
        len(resultado["db"])
}

with open(
    ROOT / "IOTEC_FUEL_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print(resultado["resumo"])


