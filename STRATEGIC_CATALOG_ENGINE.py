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

KEYWORDS = {

    "REVENUE": [
        "revenue",
        "sales",
        "client",
        "contract",
        "commercial",
        "paypal"
    ],

    "AUTOMATION": [
        "automation",
        "workflow",
        "orchestrator",
        "orchestration",
        "engine"
    ],

    "OPERATIONS": [
        "operation",
        "operational",
        "tower",
        "monitor",
        "supervisor"
    ],

    "ANALYTICS": [
        "analytics",
        "dashboard",
        "report",
        "visual"
    ],

    "CORE": [
        "core",
        "persistent",
        "runtime",
        "master"
    ]

}

VALID_EXTENSIONS = {

    ".py",
    ".ps1",
    ".json",
    ".txt",
    ".html",
    ".js"

}

catalog = defaultdict(list)

for path, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [

        d for d in dirs

        if d.lower() not in {

            "node_modules",
            "__pycache__",
            "duplicados",
            "backup",
            "backups"

        }

    ]

    for file in files:
        pass

        ext = os.path.splitext(file)[1].lower()

        if ext not in VALID_EXTENSIONS:
            continue

        lower = file.lower()

        for group, words in KEYWORDS.items():
            pass

            if any(word in lower for word in words):
                pass

                full_path = os.path.join(path, file)

                try:
                    size_mb = round(
                        os.path.getsize(full_path) /
                        1024 / 1024,
                        2
                    )
                except:
                    size_mb = 0

                catalog[group].append({

                    "file": file,
                    "path": full_path,
                    "size_mb": size_mb

                })

                break

report = {}

print("")
print("================================================")
print(" STRATEGIC CATALOG ")
print("================================================")

for group in catalog:
    pass

    items = sorted(

        catalog[group],

        key=lambda x: x["size_mb"],

        reverse=True

    )

    report[group] = items

    print("")
    print(group)
    print("-" * 40)
    print("TOTAL:", len(items))

    for item in items[:10]:
        pass

        print(
            item["file"],
            "|",
            item["size_mb"],
            "MB"
        )

with open(

    "STRATEGIC_CATALOG_REPORT.json",

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
print("================================================")
print("REPORT GENERATED")
print("STRATEGIC_CATALOG_REPORT.json")
print("================================================")
print("")




