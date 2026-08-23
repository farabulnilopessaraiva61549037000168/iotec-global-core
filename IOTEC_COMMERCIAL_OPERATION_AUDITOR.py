import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC COMMERCIAL OPERATION AUDITOR
# AUDITA OPERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O COMERCIAL REAL
# ==========================================================

import os
import sqlite3
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_COMMERCIAL_OPERATION_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_COMMERCIAL_OPERATION_REPORT.txt"

report = {
    "generated": str(datetime.now()),
    "commercial_score": 0,
    "evidence": []
}

# ==========================================================
# EVIDÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIAS
# ==========================================================

CHECKS = [

    ("CRM_ENGINE.py", 15),
    ("SALES_BRAIN.py", 15),
    ("REVENUE_OPERATION_CENTER.py", 15),
    ("AUTO_MONETIZATION_ENGINE.py", 10),
    ("AUTONOMOUS_LEAD.py", 10),
    ("IOTEC_GOVTECH_PIPELINE_DASHBOARD.py", 10),
    ("IOTEC_CONTROL_TOWER_LEDGER.db", 10),
    ("IOTEC_KNOWLEDGE_WAREHOUSE.db", 5),
    ("IOTEC_MASTER_TOWER.json", 5),
    ("IOTEC_OPERATION_GRID.json", 5)

]

# ==========================================================
# ARQUIVOS
# ==========================================================

for filename, points in CHECKS:
    pass

    found = False

    for root, dirs, files in os.walk(ROOT):
        pass

        if filename in files:
            pass

            found = True
            break

    if found:
        pass

        report["commercial_score"] += points

        report["evidence"].append({

            "asset": filename,
            "status": "FOUND",
            "points": points

        })

# ==========================================================
# BANCO DE LEADS
# ==========================================================

dbs_found = []

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".db"):
            pass

            dbs_found.append(
                os.path.join(root, file)
            )

for db in dbs_found:
    pass

    try:
        pass

        conn = sqlite3.connect(db)

        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        tables = cur.execute("""

        SELECT name

        FROM sqlite_master

        WHERE type='table'

        """

        ).fetchall()

        table_names = [

            x[0].lower()

            for x in tables

        ]

        if any(

            x in str(table_names)

            for x in [

                "lead",
                "client",
                "customer",
                "crm",
                "proposal",
                "sales"

            ]

        ):

            report["commercial_score"] += 10

            report["evidence"].append({

                "asset": db,
                "status": "COMMERCIAL_DATABASE",
                "points": 10

            })

        conn.close()

    except:
        pass

# ==========================================================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

score = report["commercial_score"]

if score >= 80:
    pass

    readiness = "PRONTO_PARA_ESCALA"

elif score >= 60:
    pass

    readiness = "PRONTO_PARA_VENDER"

elif score >= 40:
    pass

    readiness = "VENDA_ASSISTIDA"

else:
    pass

    readiness = "EM_PREPARACAO"

report["readiness"] = readiness

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
    f.write("IOTEC COMMERCIAL OPERATION AUDITOR\n")
    f.write("===================================\n\n")

    f.write(
        f"SCORE: {score}/100\n"
    )

    f.write(
        f"STATUS: {readiness}\n\n"
    )

    f.write("EVIDENCIAS\n")
    f.write("----------------------\n")

    for item in report["evidence"]:
        pass

        f.write(
            f"{item['points']} | "
            f"{item['asset']}\n"
        )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC COMMERCIAL OPERATION AUDITOR")
print("===================================")

print("")
print("SCORE:", score)

print(
    "STATUS:",
    readiness
)

print("")
print("EVIDENCIAS:")

for item in report["evidence"]:
    pass

    print(
        f"{item['points']} | "
        f"{item['asset']}"
    )

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")




