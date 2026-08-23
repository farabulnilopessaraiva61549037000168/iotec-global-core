import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from collections import defaultdict

ROOT = r"C:\IOTEC"

CATEGORIES = {
    "AI_AUTOMATION": ["automation", "agent", "ai", "intelligence"],
    "OCR": ["ocr", "document", "scan"],
    "ANALYTICS": ["analytics", "dashboard", "report", "analysis"],
    "MONITORING": ["monitor", "tower", "watch"],
    "COMMERCIAL": ["lead", "revenue", "sales", "commercial"],
    "DEPLOY": ["deploy", "render", "netlify"],
    "DATABASE": ["db", "database", "sqlite"],
    "SECURITY": ["security", "audit"],
}

catalog = defaultdict(list)

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        name = file.lower()

        matched = False

        for category, keywords in CATEGORIES.items():
            pass

            if any(k in name for k in keywords):
                pass

                catalog[category].append(
                    os.path.join(root, file)
                )

                matched = True
                break

        if not matched:
            catalog["UNCATEGORIZED"].append(
                os.path.join(root, file)
            )

report = {}

for category in sorted(catalog.keys()):
    pass

    report[category] = {
        "total": len(catalog[category]),
        "examples": catalog[category][:20]
    }

with open(
    "MISSION_01_CAPABILITY_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\n===================================")
print(" MISSION 01 COMPLETED")
print("===================================")

for category in sorted(report.keys()):
    pass

    print(
        f"{category}: "
        f"{report[category]['total']}"
    )

print("\nREPORT:")
print("MISSION_01_CAPABILITY_REPORT.json")




