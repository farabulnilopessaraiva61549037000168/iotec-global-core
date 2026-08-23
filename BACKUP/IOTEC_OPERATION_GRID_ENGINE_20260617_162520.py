import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC OPERATION GRID ENGINE
# GRADE OPERACIONAL DOS MOTORES
# ==========================================================

import json
from datetime import datetime

GRID = {

    "REALTIME": {

        "interval_seconds": 10,

        "motors": [

            "IOTEC_CORE_RUNNER",
            "IOTEC_CONTROL_TOWER_ENGINE",
            "IOTEC_CORE_LIVE_QUEUE"
        ]
    },

    "COMMERCIAL": {

        "interval_seconds": 300,

        "motors": [

            "CRM_ENGINE",
            "LEAD_SCORE_ENGINE",
            "SALES_BRAIN",
            "NEGOTIATION_ENGINE",
            "PROPOSAL_ENGINE",
            "SALES_AUTOPILOT_ENGINE"
        ]
    },

    "REVENUE": {

        "interval_seconds": 1800,

        "motors": [

            "REVENUE_DISCOVERY_ENGINE",
            "REVENUE_OPERATION_CENTER",
            "AUTO_MONETIZATION_ENGINE",
            "PRICING_ENGINE"
        ]
    },

    "INTELLIGENCE": {

        "interval_seconds": 7200,

        "motors": [

            "ECONOMIC_INTELLIGENCE",
            "IOTEC_CENTRAL_BRAIN",
            "IOTEC_MEMORY_ENGINE",
            "IOTEC_UNIFIED_BRAIN"
        ]
    },

    "STRATEGIC": {

        "interval_seconds": 21600,

        "motors": [

            "IOTEC_CAPABILITY_HUNTER",
            "MISSION_01_CAPABILITY_CATALOG",
            "TOP_ASSETS_ENGINE",
            "IOTEC_REVENUE_IDENTITY_ENGINE"
        ]
    }
}

report = {
    "generated": str(datetime.now()),
    "layers": GRID
}

with open(
    r"C:\IOTEC\IOTEC_OPERATION_GRID.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("IOTEC OPERATION GRID")
print("===================================")
print("")

for layer, cfg in GRID.items():
    pass

    print(
        f"{layer} -> "
        f"{cfg['interval_seconds']}s"
    )

print("")
print("ARQUIVO:")
print(r"C:\IOTEC\IOTEC_OPERATION_GRID.json")
print("")
print("CONCLUIDO")


