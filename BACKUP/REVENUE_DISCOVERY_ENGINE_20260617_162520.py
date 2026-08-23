import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from collections import defaultdict

INPUT_FILE = "ECONOMIC_AUDIT_REPORT.json"

GROUPS = {

    "AI_AUTOMATION": [
        "automation",
        "agent",
        "workflow",
        "pipeline",
        "ai"
    ],

    "ANALYTICS": [
        "analytics",
        "dashboard",
        "report",
        "metric",
        "business"
    ],

    "MONITORING": [
        "monitor",
        "alert",
        "tracking",
        "tower",
        "runtime"
    ],

    "DEPLOY": [
        "deploy",
        "cloud",
        "server",
        "hosting"
    ],

    "OCR": [
        "ocr",
        "document",
        "pdf",
        "image"
    ],

    "COMMERCIAL": [
        "lead",
        "revenue",
        "sales",
        "client",
        "commercial"
    ]

}

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

catalog = defaultdict(list)

for item in data:
    pass

    file_name = item["file"].lower()

    matched = False

    for group, words in GROUPS.items():
        pass

        for word in words:
            pass

            if word in file_name:
                pass

                catalog[group].append(item)

                matched = True
                break

        if matched:
            break

    if not matched:
        pass

        catalog["UNCLASSIFIED"].append(item)

print("")
print("================================================")
print(" REVENUE DISCOVERY REPORT ")
print("================================================")

for group in sorted(catalog.keys()):
    pass

    print("")
    print(group)
    print("-" * 40)

    print(
        "TOTAL:",
        len(catalog[group])
    )

print("")
print("================================================")

with open(
    "REVENUE_DISCOVERY_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        catalog,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print(
    "REPORT GENERATED:"
)

print(
    "REVENUE_DISCOVERY_REPORT.json"
)

print("")


