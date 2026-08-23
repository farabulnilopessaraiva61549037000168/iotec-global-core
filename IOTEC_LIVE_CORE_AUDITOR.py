import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC LIVE CORE AUDITOR
# AUDITA SOMENTE MOTORES VIVOS
# ==========================================================

import os
import json
import re
from datetime import datetime

ROOT = r"C:\IOTEC"

IGNORE_DIRS = {
    "venv",
    "__pycache__",
    ".git",
    "node_modules",

    "backups",
    "backup",

    "legacy",
    "frozen",

    "mineradora_bruta",

    "nucleo_consolidado",

    "logs",

    "dist",
    "build"
}

CORE_WORDS = [
    "brain",
    "engine",
    "core",
    "orchestrator",
    "sales",
    "revenue",
    "crm",
    "billing",
    "payment",
    "lead",
    "pricing",
    "proposal",
    "capability",
    "audit",
    "intelligence"
]

report = {
    "generated": str(datetime.now()),
    "active_motors": [],
    "commercial_chain": [],
    "revenue_chain": [],
    "brain_chain": [],
    "orchestrators": [],
    "databases": [],
    "largest_files": []
}

sizes = []

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d.lower() not in IGNORE_DIRS
    ]

    for file in files:
        pass

        path = os.path.join(root, file)

        lower = file.lower()

        if not lower.endswith(".py"):
            continue

        try:
            size = os.path.getsize(path)

            sizes.append(
                (
                    size,
                    file,
                    path
                )
            )

            if any(
                word in lower
                for word in CORE_WORDS
            ):

                report["active_motors"].append(path)

            if any(
                word in lower
                for word in [
                    "sales",
                    "crm",
                    "lead",
                    "proposal",
                    "pricing",
                    "negotiation",
                    "commercial"
                ]
            ):
                report["commercial_chain"].append(path)

            if any(
                word in lower
                for word in [
                    "revenue",
                    "billing",
                    "payment",
                    "monetization",
                    "opportunity"
                ]
            ):
                report["revenue_chain"].append(path)

            if any(
                word in lower
                for word in [
                    "brain",
                    "intelligence",
                    "memory",
                    "neural"
                ]
            ):
                report["brain_chain"].append(path)

            if any(
                word in lower
                for word in [
                    "orchestrator",
                    "runner",
                    "manager",
                    "control_tower"
                ]
            ):
                report["orchestrators"].append(path)

        except:
            pass

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d.lower() not in IGNORE_DIRS
    ]

    for file in files:
        pass

        if file.lower().endswith(".db"):
            pass

            report["databases"].append(
                os.path.join(root, file)
            )

sizes.sort(reverse=True)

for size, file, path in sizes[:50]:
    pass

    report["largest_files"].append({
        "file": file,
        "size_mb": round(size / 1024 / 1024, 2),
        "path": path
    })

OUTPUT = r"C:\IOTEC\IOTEC_LIVE_CORE_REPORT.json"

with open(
    OUTPUT,
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
print("IOTEC LIVE CORE AUDITOR")
print("===================================")
print("")
print("RELATORIO:")
print(OUTPUT)
print("")
print("CONCLUIDO")




