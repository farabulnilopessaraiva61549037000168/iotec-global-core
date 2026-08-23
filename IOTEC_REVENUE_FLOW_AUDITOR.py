import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC REVENUE FLOW AUDITOR
# PROCURA FLUXO REAL DE RECEITA
# ==========================================================

import os
import sqlite3
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_REVENUE_FLOW_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_REVENUE_FLOW_REPORT.txt"

KEYWORDS = [

    "lead",
    "client",
    "customer",
    "cliente",
    "crm",
    "proposal",
    "contract",
    "revenue",
    "sale",
    "sales",
    "payment",
    "invoice",
    "negotiation"

]

report = {
    "generated": str(datetime.now()),
    "databases": [],
    "commercial_tables": 0,
    "commercial_records": 0
}

# ==========================================================
# PROCURA DBS
# ==========================================================

dbs = []

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".db"):
            pass

            dbs.append(
                os.path.join(root, file)
            )

# ==========================================================
# ANALISA
# ==========================================================

for db in dbs:
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

        db_info = {

            "database": db,
            "tables": []

        }

        for table in tables:
            pass

            table_name = table[0]

            low = table_name.lower()

            if any(

                word in low

                for word in KEYWORDS

            ):

                report[
                    "commercial_tables"
                ] += 1

                try:
                    pass

                    total = cur.execute(

                        f"SELECT COUNT(*) FROM {table_name}"

                    ).fetchone()[0]

                except:
                    pass

                    total = 0

                report[
                    "commercial_records"
                ] += total

                db_info["tables"].append({

                    "table": table_name,
                    "records": total

                })

        if db_info["tables"]:
            pass

            report["databases"].append(
                db_info
            )

        conn.close()

    except:
        pass

# ==========================================================
# SCORE
# ==========================================================

score = 0

score += min(
    report["commercial_tables"] * 5,
    50
)

score += min(
    report["commercial_records"] // 10,
    50
)

score = min(score, 100)

report["flow_score"] = score

if score >= 80:
    pass

    status = "FLUXO_COMERCIAL_FORTE"

elif score >= 60:
    pass

    status = "FLUXO_COMERCIAL_ATIVO"

elif score >= 40:
    pass

    status = "FLUXO_PARCIAL"

else:
    pass

    status = "FLUXO_MINIMO"

report["status"] = status

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
    f.write("IOTEC REVENUE FLOW AUDITOR\n")
    f.write("===================================\n\n")

    f.write(
        f"COMMERCIAL TABLES: {report['commercial_tables']}\n"
    )

    f.write(
        f"COMMERCIAL RECORDS: {report['commercial_records']}\n"
    )

    f.write(
        f"FLOW SCORE: {score}/100\n"
    )

    f.write(
        f"STATUS: {status}\n\n"
    )

    for db in report["databases"]:
        pass

        f.write(
            f"DATABASE: {db['database']}\n"
        )

        for table in db["tables"]:
            pass

            f.write(
                f"   {table['table']} -> {table['records']}\n"
            )

        f.write("\n")

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC REVENUE FLOW AUDITOR")
print("===================================")

print("")
print(
    "COMMERCIAL TABLES:",
    report["commercial_tables"]
)

print(
    "COMMERCIAL RECORDS:",
    report["commercial_records"]
)

print(
    "FLOW SCORE:",
    score
)

print(
    "STATUS:",
    status
)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")




