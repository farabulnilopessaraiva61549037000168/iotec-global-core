import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC MOTOR ACTIVATION AUDITOR
# DESCOBRE O ESTADO REAL DOS MOTORES
# ==========================================================

import json
import os
from datetime import datetime

TOPOLOGY = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_MOTOR_ACTIVATION_REPORT.json"
OUTPUT_TXT = r"C:\IOTEC\IOTEC_MOTOR_ACTIVATION_REPORT.txt"

with open(
    TOPOLOGY,
    "r",
    encoding="utf-8"
) as f:

    topo = json.load(f)

report = {

    "generated": str(datetime.now()),

    "motors": [],

    "summary": {

        "ACTIVE": 0,
        "PARTIAL": 0,
        "DORMANT": 0,
        "ORPHAN": 0
    }
}

# ==========================================================
# CLASSIFICADOR
# ==========================================================

for motor, data in topo["nodes"].items():
    pass

    if "error" in data:
        pass

        report["motors"].append({

            "motor": motor,
            "status": "ORPHAN",
            "reason": "ERROR"

        })

        report["summary"]["ORPHAN"] += 1

        continue

    path = data.get("path", "")

    exists = os.path.exists(path)

    funcs = data.get("function_count", 0)

    imports = len(
        data.get("imports", [])
    )

    sqlite_used = data.get(
        "sqlite",
        False
    )

    json_used = data.get(
        "json",
        False
    )

    score = 0

    if exists:
        score += 1

    if funcs > 0:
        score += 1

    if imports > 0:
        score += 1

    if sqlite_used:
        score += 1

    if json_used:
        score += 1

    # --------------------------------

    if score >= 5:
        pass

        status = "ACTIVE"

    elif score >= 3:
        pass

        status = "PARTIAL"

    elif score >= 1:
        pass

        status = "DORMANT"

    else:
        pass

        status = "ORPHAN"

    report["summary"][status] += 1

    report["motors"].append({

        "motor": motor,

        "status": status,

        "score": score,

        "functions": funcs,

        "imports": imports,

        "sqlite": sqlite_used,

        "json": json_used,

        "path_exists": exists

    })

# ==========================================================
# ORDENA
# ==========================================================

report["motors"] = sorted(

    report["motors"],

    key=lambda x: x.get(
        "score",
        0
    ),

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
    f.write("IOTEC MOTOR ACTIVATION AUDITOR\n")
    f.write("===================================\n\n")

    f.write(
        f"ACTIVE: {report['summary']['ACTIVE']}\n"
    )

    f.write(
        f"PARTIAL: {report['summary']['PARTIAL']}\n"
    )

    f.write(
        f"DORMANT: {report['summary']['DORMANT']}\n"
    )

    f.write(
        f"ORPHAN: {report['summary']['ORPHAN']}\n\n"
    )

    for item in report["motors"]:
        pass

        f.write(
            f"{item['motor']} -> {item['status']}\n"
        )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC MOTOR ACTIVATION AUDITOR")
print("===================================")
print("")

for k, v in report["summary"].items():
    pass

    print(
        f"{k}: {v}"
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




