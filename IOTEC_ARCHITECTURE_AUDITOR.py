import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC_ARCHITECTURE_AUDITOR.py
# AUDITOR GERAL DA ARQUITETURA
# SOMENTE LEITURA
# ==========================================================

import os
import json
import re
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

IGNORE = {
    "venv",
    "node_modules",
    "__pycache__",
    ".git",
    "DUPLICADOS"
}

system_map = {
    "generated": str(datetime.now()),
    "motors": [],
    "databases": [],
    "reports": [],
    "dashboards": [],
    "apis": [],
    "commercial": [],
    "financial": [],
    "ai": [],
    "dependencies": defaultdict(list)
}

KEYS = {

    "motors": [
        "engine",
        "brain",
        "core",
        "orchestrator",
        "hunter"
    ],

    "dashboards": [
        "dashboard"
    ],

    "commercial": [
        "sales",
        "crm",
        "lead",
        "proposal",
        "pricing",
        "negotiation"
    ],

    "financial": [
        "revenue",
        "payment",
        "invoice",
        "billing"
    ],

    "ai": [
        "ai",
        "brain",
        "intelligence",
        "neural",
        "gpt"
    ]
}

for root, dirs, files in os.walk(ROOT):
    pass

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]

    for file in files:
        pass

        path = os.path.join(root, file)

        lower = file.lower()

        if lower.endswith(".db"):
            system_map["databases"].append(path)

        if (
            lower.endswith(".json")
            and "report" in lower
        ):
            system_map["reports"].append(path)

        for group, words in KEYS.items():
            pass

            if any(
                word in lower
                for word in words
            ):

                system_map[group].append(path)

        if file.endswith(".py"):
            pass

            try:
                pass

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                imports = re.findall(
                    r"import\s+([a-zA-Z0-9_]+)",
                    content
                )

                system_map[
                    "dependencies"
                ][file] = imports

            except:
                pass

with open(
    r"C:\IOTEC\IOTEC_SYSTEM_MAP.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        system_map,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("IOTEC ARCHITECTURE AUDITOR")
print("===================================")
print("")
print("MAPA GERADO:")
print(r"C:\IOTEC\IOTEC_SYSTEM_MAP.json")
print("")
print("CONCLUIDO")




