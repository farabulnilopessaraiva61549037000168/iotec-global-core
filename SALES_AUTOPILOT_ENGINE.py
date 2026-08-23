import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

CREATE TABLE IF NOT EXISTS sales_autopilot_log(

```
id INTEGER PRIMARY KEY AUTOINCREMENT,
company TEXT,
score INTEGER,
opportunity_id INTEGER,
proposal_value REAL,
created_at TEXT
```

)

""")

conn.commit()

try:
    pass

```
sessions = cur.execute("""

SELECT

company,
email,
sector,
lead_score,
recommendation,
estimated_value

FROM sales_consultant_sessions

WHERE status='NOVO_LEAD'

""").fetchall()
```

except Exception as e:
    pass

```
print("")
print("ERRO:", e)
print("")

conn.close()
exit()
```

gerados = 0

for row in sessions:
    pass

```
empresa = row[0]
email = row[1]
setor = row[2]
score = row[3]
produto = row[4]
valor = row[5]

if score < 15:
    continue

opportunity_id = int(datetime.now().timestamp())

cur.execute("""

INSERT INTO pipeline(

    opportunity_id,
    status,
    report_sent,
    meeting_scheduled,
    proposal_sent,
    proposal_value,
    payment_received,
    observations,
    updated_at,
    client_name,
    phone,
    approved

)

VALUES(

    ?,?,?,?,?,?,?,?,?,?,?,?

)

""",(

    opportunity_id,
    'PROPOSTA_ENVIADA',
    0,
    0,
    1,
    valor,
    0,
    produto,
    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    empresa,
    '',
    0

))

cur.execute("""

INSERT INTO sales_autopilot_log(

    company,
    score,
    opportunity_id,
    proposal_value,
    created_at

)

VALUES(

    ?,?,?,?,?

)

""",(

    empresa,
    score,
    opportunity_id,
    valor,
    datetime.now().strftime("%d/%m/%Y %H:%M:%S")

))

cur.execute("""

UPDATE sales_consultant_sessions

SET status='PROCESSADO'

WHERE company=?
AND email=?

""",(

    empresa,
    email

))

gerados += 1
```

conn.commit()
conn.close()

print("")
print("===================================================")
print("SALES AUTOPILOT ENGINE")
print("===================================================")
print("")
print("OPORTUNIDADES GERADAS:", gerados)
print("")




