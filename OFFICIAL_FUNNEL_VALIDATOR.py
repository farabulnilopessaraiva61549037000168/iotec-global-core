import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

OFFICIAL_COMPONENTS = {

    "FRONTEND": "IoTec_Plataforma.html",
    "LEAD_BRIDGE": "REAL_LEAD_BRIDGE.py",
    "BACKEND": "ENTERPRISE_RENDER_READY.py",
    "DATABASE": "enterprise.db",
    "TOWER": "COMMERCIAL_TOWER.py",
    "REVENUE": "REVENUE_OPERATION_CENTER.py",
    "PAYMENT": "paypal_server.py"

}

report = {
    "timestamp": str(datetime.now()),
    "components": {}
}

print("")
print("================================================")
print(" OFFICIAL FUNNEL VALIDATOR ")
print("================================================")

for component, target in OFFICIAL_COMPONENTS.items():
    pass

    found = False
    location = ""

    for root, dirs, files in os.walk(ROOT):
        pass

        if target in files:
            pass

            found = True
            location = os.path.join(root, target)
            break

    report["components"][component] = {

        "target": target,
        "found": found,
        "location": location

    }

    print("")
    print(component)

    if found:
        pass

        print("STATUS : OK")
        print("FILE   :", location)

    else:
        pass

        print("STATUS : NOT FOUND")

print("")
print("================================================")

total = len(OFFICIAL_COMPONENTS)

ok = sum(
    1
    for item in report["components"].values()
    if item["found"]
)

score = round((ok / total) * 100)

print("")
print("FUNNEL HEALTH:", score, "%")

if score == 100:
    print("STATUS: READY FOR LIVE VALIDATION")

elif score >= 70:
    print("STATUS: PARTIALLY READY")

else:
    print("STATUS: REQUIRES CONSOLIDATION")

print("")
print("================================================")

with open(
    "OFFICIAL_FUNNEL_VALIDATION_REPORT.json",
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
print("REPORT GENERATED")
print("OFFICIAL_FUNNEL_VALIDATION_REPORT.json")
print("")




