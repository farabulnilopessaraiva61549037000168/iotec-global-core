import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC PRODUCTION LEDGER
# CONTABILIDADE OPERACIONAL DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EXECUTA MOTORES
# APENAS REGISTRA PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

import json
import os
from datetime import datetime

ROOT = r"C:\IOTEC"

LEDGER_FILE = r"C:\IOTEC\IOTEC_PRODUCTION_LEDGER.json"

# ----------------------------------------------------------
# CRIA LEDGER SE NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EXISTIR
# ----------------------------------------------------------

if not os.path.exists(LEDGER_FILE):
    pass

    with open(
        LEDGER_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "created": str(datetime.now()),
                "records": []
            },
            f,
            indent=4,
            ensure_ascii=False
        )

# ----------------------------------------------------------
# CARREGA
# ----------------------------------------------------------

with open(
    LEDGER_FILE,
    "r",
    encoding="utf-8"
) as f:

    ledger = json.load(f)

# ----------------------------------------------------------
# MOTORES DA GRADE
# ----------------------------------------------------------

GRID_FILE = r"C:\IOTEC\IOTEC_OPERATION_GRID.json"

if os.path.exists(GRID_FILE):
    pass

    with open(
        GRID_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        grid = json.load(f)

else:
    pass

    print("GRADE NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ENCONTRADA")
    raise SystemExit()

# ----------------------------------------------------------
# REGISTRA SNAPSHOT
# ----------------------------------------------------------

snapshot_time = str(datetime.now())

for layer, cfg in grid["layers"].items():
    pass

    for motor in cfg["motors"]:
        pass

        ledger["records"].append({

            "timestamp": snapshot_time,

            "motor": motor,

            "layer": layer,

            "status": "AGENDADO",

            "produced": None,

            "destination": None,

            "value_score": 0
        })

# ----------------------------------------------------------
# ESTATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂSTICAS
# ----------------------------------------------------------

stats = {}

for item in ledger["records"]:
    pass

    layer = item["layer"]

    stats[layer] = stats.get(layer, 0) + 1

ledger["stats"] = stats
ledger["last_update"] = snapshot_time

# ----------------------------------------------------------
# SALVA
# ----------------------------------------------------------

with open(
    LEDGER_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        ledger,
        f,
        indent=4,
        ensure_ascii=False
    )

# ----------------------------------------------------------
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ----------------------------------------------------------

print("")
print("===================================")
print("IOTEC PRODUCTION LEDGER")
print("===================================")
print("")

for layer, total in stats.items():
    pass

    print(
        f"{layer}: {total}"
    )

print("")
print("LEDGER:")
print(LEDGER_FILE)
print("")
print("CONCLUIDO")




