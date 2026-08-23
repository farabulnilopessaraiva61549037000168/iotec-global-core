import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC TRACTION ENGINE
# GERA METAS DE CRESCIMENTO
# ==========================================================

import sqlite3
import json
import os
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_TRACTION_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_TRACTION_REPORT.txt"

# ==========================================================
# CONTADORES
# ==========================================================

leads = 0
clients = 0
payments = 0
invoices = 0

# ==========================================================
# PROCURA BANCOS
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
# LEITURA
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

        """).fetchall()

        for table in tables:
            pass

            name = table[0]

            low = name.lower()

            try:
                pass

                total = cur.execute(

                    f"SELECT COUNT(*) FROM {name}"

                ).fetchone()[0]

            except:
                pass

                total = 0

            if "lead" in low:
                pass

                leads += total

            elif "client" in low:
                pass

                clients += total

            elif "payment" in low:
                pass

                payments += total

            elif "invoice" in low:
                pass

                invoices += total

        conn.close()

    except:
        pass

# ==========================================================
# METAS
# ==========================================================

target_leads = max(
    100,
    leads * 10
)

target_clients = max(
    10,
    clients * 5
)

target_payments = max(
    20,
    payments * 10
)

# ==========================================================
# SCORE
# ==========================================================

traction_score = (
    leads * 2 +
    clients * 5 +
    payments * 10
)

# ==========================================================
# RELATORIO
# ==========================================================

report = {

    "generated": str(datetime.now()),

    "current": {

        "leads": leads,
        "clients": clients,
        "payments": payments,
        "invoices": invoices

    },

    "targets_30_days": {

        "leads": target_leads,
        "clients": target_clients,
        "payments": target_payments

    },

    "traction_score": traction_score
}

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
    f.write("IOTEC TRACTION ENGINE\n")
    f.write("===================================\n\n")

    f.write(f"LEADS: {leads}\n")
    f.write(f"CLIENTS: {clients}\n")
    f.write(f"PAYMENTS: {payments}\n")
    f.write(f"INVOICES: {invoices}\n\n")

    f.write("META 30 DIAS\n")
    f.write("----------------------\n")
    f.write(f"LEADS: {target_leads}\n")
    f.write(f"CLIENTS: {target_clients}\n")
    f.write(f"PAYMENTS: {target_payments}\n\n")

    f.write(
        f"TRACTION SCORE: {traction_score}\n"
    )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC TRACTION ENGINE")
print("===================================")

print("")
print("LEADS:", leads)
print("CLIENTS:", clients)
print("PAYMENTS:", payments)
print("INVOICES:", invoices)

print("")
print("META 30 DIAS")

print("LEADS:", target_leads)
print("CLIENTS:", target_clients)
print("PAYMENTS:", target_payments)

print("")
print(
    "TRACTION SCORE:",
    traction_score
)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("CONCLUIDO")




