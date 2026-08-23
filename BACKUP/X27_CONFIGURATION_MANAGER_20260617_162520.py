import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 CONFIGURATION MANAGER
# ============================================================

from datetime import datetime
import json

CONFIG = {

    "municipio": "IBICUITINGA",

    "resilience_target": 90,

    "alert_threshold": 70,

    "forecast_days": 365

}

with open(

    "X27_CONFIG.json",

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        CONFIG,

        f,

        indent=4

    )

print("\n================================================")
print("X27 CONFIGURATION MANAGER")
print("================================================")

print(f"DATA : {datetime.now()}")

print("\nCONFIGURACAO SALVA")

print(CONFIG)


