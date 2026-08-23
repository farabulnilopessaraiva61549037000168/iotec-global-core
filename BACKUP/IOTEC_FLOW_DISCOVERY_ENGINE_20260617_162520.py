import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC FLOW DISCOVERY ENGINE
# DESCOBRE FLUXOS REAIS DE DADOS
# ==========================================================

import os
import json
import re
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT = r"C:\IOTEC\IOTEC_FLOW_DISCOVERY_REPORT.json"

patterns = {
    "SQLITE": r"sqlite3\.connect\s*\(",
    "JSON_LOAD": r"json\.load",
    "JSON_DUMP": r"json\.dump",
    "OPEN_READ": r"open\s*\(.*?["']r["']",
    "OPEN_WRITE": r"open\s*\(.*?["']w["']",
}

report = {
    "generated": str(datetime.now()),
    "files_scanned": 0,
    "flows": []
}

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if not file.lower().endswith(".py"):
            continue

        path = os.path.join(root, file)

        try:
            pass

            content = open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ).read()

            flow = {
                "file": file,
                "sqlite": False,
                "json_load": False,
                "json_dump": False,
                "reads": False,
                "writes": False
            }

            if re.search(patterns["SQLITE"], content):
                flow["sqlite"] = True

            if re.search(patterns["JSON_LOAD"], content):
                flow["json_load"] = True

            if re.search(patterns["JSON_DUMP"], content):
                flow["json_dump"] = True

            if re.search(patterns["OPEN_READ"], content):
                flow["reads"] = True

            if re.search(patterns["OPEN_WRITE"], content):
                flow["writes"] = True

            if any(flow.values()):
                report["flows"].append(flow)

            report["files_scanned"] += 1

        except:
            pass

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
print("IOTEC FLOW DISCOVERY ENGINE")
print("===================================")
print("")

print("FILES:", report["files_scanned"])
print("FLOWS:", len(report["flows"]))

print("")
print("TOP FLOW FILES")
print("")

for item in report["flows"][:20]:
    pass

    score = sum([
        item["sqlite"],
        item["json_load"],
        item["json_dump"],
        item["reads"],
        item["writes"]
    ])

    print(
        f"{item['file']} -> FLOW SCORE {score}"
    )

print("")
print("RELATORIO:")
print(OUTPUT)

print("")
print("CONCLUIDO")


