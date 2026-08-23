import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC EVENT PUBLISHER
# ==========================================================

import sqlite3
import json
import sys
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_EVENT_BUS.db"

if len(sys.argv) < 2:
    pass

    print("")
    print("USO:")
    print("python IOTEC_EVENT_PUBLISHER.py lead")
    print("python IOTEC_EVENT_PUBLISHER.py proposal")
    print("python IOTEC_EVENT_PUBLISHER.py meeting")
    print("python IOTEC_EVENT_PUBLISHER.py payment")
    exit()

event_type = sys.argv[1].upper()

conn = sqlite3.connect(DB)
cur = conn.cursor()

payload = {

    "created":
    str(datetime.now())

}

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
    "MANUAL",
    event_type,
    json.dumps(payload)

))

conn.commit()

event_id = cur.lastrowid

print("")
print("===================================")
print("IOTEC EVENT PUBLISHER")
print("===================================")

print("")
print("EVENT ID:", event_id)
print("EVENT TYPE:", event_type)

print("")
print("DATABASE:")
print(DB)

print("")
print("CONCLUIDO")

conn.close()


