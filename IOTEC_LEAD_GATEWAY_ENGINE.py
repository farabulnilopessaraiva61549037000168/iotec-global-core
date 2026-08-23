import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.db"
EVENT_DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

event_conn = sqlite3.connect(EVENT_DB)
event_cur = event_conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS leads(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    name TEXT,

    company TEXT,

    email TEXT,

    phone TEXT,

    city TEXT,

    message TEXT,

    status TEXT

)

""")

lead = {

    "name": "VISITANTE_PORTAL",
    "company": "EMPRESA_EXEMPLO",
    "email": "contato@empresa.com",
    "phone": "(00)00000-0000",
    "city": "QUXIADA",
    "message": "Solicitou diagnostico executivo"

}

created = str(datetime.now())

cur.execute("""

INSERT INTO leads(

    created_at,
    name,
    company,
    email,
    phone,
    city,
    message,
    status

)

VALUES(

    ?,?,?,?,?,?,?,?

)

""",

(
    created,
    lead["name"],
    lead["company"],
    lead["email"],
    lead["phone"],
    lead["city"],
    lead["message"],
    "NOVO"
))

event_cur.execute("""

INSERT INTO events(

    timestamp,
    source,
    event_type,
    payload,
    processed

)

VALUES(

    ?,?,?,?,?

)

""",

(
    created,
    "LEAD_GATEWAY",
    "LEAD",
    json.dumps(lead),
    0
))

conn.commit()
event_conn.commit()

lead_id = cur.lastrowid

print("")
print("===================================")
print("IOTEC LEAD GATEWAY")
print("===================================")
print("")

print("LEAD ID:", lead_id)
print("EMPRESA:", lead["company"])
print("EMAIL:", lead["email"])

print("")
print("EVENTO LEAD CRIADO")

print("")
print("DATABASE CRM:")
print(DB)

print("")
print("DATABASE EVENT BUS:")
print(EVENT_DB)

conn.close()
event_conn.close()




