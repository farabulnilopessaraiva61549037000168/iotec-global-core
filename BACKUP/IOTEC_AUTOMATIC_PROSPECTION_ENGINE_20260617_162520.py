import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC AUTOMATIC PROSPECTION ENGINE
# GERA LEADS PARA A TORRE
# ==========================================================

import sqlite3
import json
from datetime import datetime

EVENT_DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

LEADS = [

    {
        "company":"Escola Alfa",
        "sector":"EDUCACAO"
    },

    {
        "company":"Clinica Vida",
        "sector":"SAUDE"
    },

    {
        "company":"Prefeitura Modelo",
        "sector":"GOVTECH"
    }

]

conn = sqlite3.connect(EVENT_DB)
cur = conn.cursor()

generated = 0

print("")
print("===================================")
print("IOTEC AUTOMATIC PROSPECTION ENGINE")
print("===================================")

for lead in LEADS:
    pass

    cur.execute("""

    INSERT INTO events (

        timestamp,
        source,
        event_type,
        payload,
        processed

    )

    VALUES (

        ?,?,?,?,0

    )

    """,

    (

        str(datetime.now()),
        "AUTOMATIC_PROSPECTION",
        "LEAD",
        json.dumps(lead),
        0

    ))

    generated += 1

    print(
        f"LEAD GERADO -> {lead['company']}"
    )

conn.commit()

print("")
print(
    "TOTAL LEADS:",
    generated
)

print("")
print("DATABASE:")
print(EVENT_DB)

print("")
print("CONCLUIDO")

conn.close()


