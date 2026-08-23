import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC GROWTH SIMULATOR
# ALIMENTA A TORRE COM EVENTOS
# ==========================================================

import sqlite3
import json

from datetime import datetime

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("===================================")
print("IOTEC GROWTH SIMULATOR")
print("===================================")

events = [

    {
        "event_type":"LEAD",
        "payload":{
            "company":"Escola Alfa"
        }
    },

    {
        "event_type":"LEAD",
        "payload":{
            "company":"Clinica Vida"
        }
    },

    {
        "event_type":"LEAD",
        "payload":{
            "company":"Prefeitura Modelo"
        }
    },

    {
        "event_type":"PROPOSAL",
        "payload":{
            "proposal":"AUDITORIA_OPERACIONAL"
        }
    },

    {
        "event_type":"PROPOSAL",
        "payload":{
            "proposal":"AUDITORIA_FINANCEIRA"
        }
    },

    {
        "event_type":"MEETING",
        "payload":{
            "meeting":"REUNIAO_COMERCIAL"
        }
    }

]

created = 0

for event in events:
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

        ?,?,?,?,?

    )

    """,

    (

        str(datetime.now()),
        "GROWTH_SIMULATOR",
        event["event_type"],
        json.dumps(
            event["payload"]
        ),
        0

    ))

    created += 1

    print(

        f"EVENTO -> {event['event_type']}"

    )

conn.commit()

print("")
print("EVENTOS GERADOS:", created)

print("")
print("DATABASE:")
print(DB)

print("")
print("CONCLUIDO")

conn.close()


