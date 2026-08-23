import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC ENGINE INTEGRATION AUDITOR
# DESCOBRE QUEM CONVERSA COM QUEM
# ==========================================================

import json
import os
import re
from datetime import datetime

TOPOLOGY = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_ENGINE_INTEGRATION_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_ENGINE_INTEGRATION_REPORT.txt"

with open(
    TOPOLOGY,
    "r",
    encoding="utf-8"
) as f:

    topo = json.load(f)

nodes = topo["nodes"]

report = {

    "generated": str(datetime.now()),

    "integrations": [],

    "summary": {

        "engines": 0,
        "connections": 0
    }
}

# ==========================================================
# LISTA DE NOMES
# ==========================================================

engine_names = []

for motor in nodes.keys():
    pass

    engine_names.append(
        motor.replace(".py", "")
    )

# ==========================================================
# PROCURA REFERÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIAS
# ==========================================================

for motor, data in nodes.items():
    pass

    path = data.get("path", "")

    if not os.path.exists(path):
        continue

    try:
        pass

        with open(
            path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            content = f.read()

        links = []

        for target in engine_names:
            pass

            if target == motor.replace(".py", ""):
                continue

            if re.search(
                re.escape(target),
                content,
                re.IGNORECASE
            ):

                links.append(target)

        report["integrations"].append({

            "motor": motor,

            "connections": links,

            "total_connections": len(links)

        })

        report["summary"]["engines"] += 1
        report["summary"]["connections"] += len(links)

    except:
        pass

# ==========================================================
# ORDENA
# ==========================================================

report["integrations"] = sorted(

    report["integrations"],

    key=lambda x: x["total_connections"],

    reverse=True

)

# ==========================================================
# JSON
# ==========================================================

with open(
    OUTPUT_JSON,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# TXT
# ==========================================================

with open(
    OUTPUT_TXT,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC ENGINE INTEGRATION AUDITOR\n")
    f.write("===================================\n\n")

    f.write(
        f"ENGINES: {report['summary']['engines']}\n"
    )

    f.write(
        f"CONNECTIONS: {report['summary']['connections']}\n\n"
    )

    for item in report["integrations"]:
        pass

        f.write(
            f"{item['motor']}\n"
        )

        f.write(
            f"CONNECTIONS: {item['total_connections']}\n"
        )

        for link in item["connections"]:
            pass

            f.write(
                f"  -> {link}\n"
            )

        f.write("\n")

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC ENGINE INTEGRATION AUDITOR")
print("===================================")
print("")

print(
    "ENGINES:",
    report["summary"]["engines"]
)

print(
    "CONNECTIONS:",
    report["summary"]["connections"]
)

print("")
print("TOP INTEGRATIONS")
print("")

for item in report["integrations"][:10]:
    pass

    print(
        f"{item['motor']} -> {item['total_connections']}"
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




