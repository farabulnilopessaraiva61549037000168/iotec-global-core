import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

OFFICIAL_FUNNEL = {

    "created_at": str(datetime.now()),

    "status": "OFFICIAL_FUNNEL",

    "frontend": {
        "component": "IoTec_Plataforma.html",
        "role": "CLIENT_ENTRY"
    },

    "lead_bridge": {
        "component": "REAL_LEAD_BRIDGE.py",
        "role": "LEAD_CAPTURE"
    },

    "backend": {
        "component": "ENTERPRISE_RENDER_READY.py",
        "role": "API_AND_PROCESSING"
    },

    "database": {
        "component": "enterprise.db",
        "role": "OFFICIAL_DATABASE"
    },

    "tower": {
        "component": "COMMERCIAL_TOWER.py",
        "role": "COMMERCIAL_QUEUE"
    },

    "revenue": {
        "component": "REVENUE_OPERATION_CENTER.py",
        "role": "PROPOSALS_AND_REVENUE"
    },

    "payment": {
        "component": "paypal_server.py",
        "role": "PAYMENT_GATEWAY"
    }

}

with open(
    "OFFICIAL_FUNNEL.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        OFFICIAL_FUNNEL,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("================================================")
print(" OFFICIAL FUNNEL LOCKED ")
print("================================================")
print("")
print("Frontend : IoTec_Plataforma.html")
print("Lead     : REAL_LEAD_BRIDGE.py")
print("Backend  : ENTERPRISE_RENDER_READY.py")
print("Database : enterprise.db")
print("Tower    : COMMERCIAL_TOWER.py")
print("Revenue  : REVENUE_OPERATION_CENTER.py")
print("Payment  : paypal_server.py")
print("")
print("OFFICIAL_FUNNEL.json CREATED")
print("")


