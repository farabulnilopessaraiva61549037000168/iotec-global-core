import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC MISSION EXECUTION LEDGER
# REGISTRA EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DAS MISSÃƒÆ'Ã†â€™ES
# ==========================================================

import sqlite3
import json
from datetime import datetime

MISSION_FILE = r"C:\IOTEC\IOTEC_DAILY_GROWTH_MISSION.json"

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

# ==========================================================
# BANCO
# ==========================================================

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

CREATE TABLE IF NOT EXISTS missions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    product TEXT,

    target_leads INTEGER,
    target_proposals INTEGER,
    target_meetings INTEGER,

    executed_leads INTEGER,
    executed_proposals INTEGER,
    executed_meetings INTEGER,

    execution_percent REAL,

    potential_revenue REAL,

    status TEXT

)

""")

conn.commit()

# ==========================================================
# CARREGA MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

with open(
    MISSION_FILE,
    "r",
    encoding="utf-8"
) as f:

    mission = json.load(f)

product = mission["priority_product"]

target_leads = mission["mission"]["leads"]
target_proposals = mission["mission"]["proposals"]
target_meetings = mission["mission"]["meetings"]

potential_revenue = mission["potential_revenue"]

# ==========================================================
# PRIMEIRO REGISTRO
# ==========================================================

exists = cur.execute("""

SELECT COUNT(*)

FROM missions

WHERE date(timestamp)=date('now')

""").fetchone()[0]

if exists == 0:
    pass

    cur.execute("""

    INSERT INTO missions (

        timestamp,
        product,

        target_leads,
        target_proposals,
        target_meetings,

        executed_leads,
        executed_proposals,
        executed_meetings,

        execution_percent,

        potential_revenue,

        status

    )

    VALUES (

        ?,?,?,?,?,?,?,?,?,?,?

    )

    """,

    (

        str(datetime.now()),
        product,

        target_leads,
        target_proposals,
        target_meetings,

        0,
        0,
        0,

        0,

        potential_revenue,

        "OPEN"

    ))

    conn.commit()

# ==========================================================
# PAINEL
# ==========================================================

row = cur.execute("""

SELECT

    target_leads,
    target_proposals,
    target_meetings,

    executed_leads,
    executed_proposals,
    executed_meetings

FROM missions

ORDER BY id DESC

LIMIT 1

""").fetchone()

tl,tp,tm,el,ep,em = row

target_total = tl + tp + tm
executed_total = el + ep + em

if target_total:
    pass

    execution = round(
        (executed_total / target_total) * 100,
        2
    )

else:
    pass

    execution = 0

cur.execute("""

UPDATE missions

SET execution_percent=?

WHERE id=(

    SELECT MAX(id)

    FROM missions

)

""",

(execution,))

conn.commit()

# ==========================================================
# RESUMO
# ==========================================================

print("")
print("===================================")
print("IOTEC MISSION EXECUTION LEDGER")
print("===================================")

print("")
print("PRODUTO:", product)

print("")
print("META")

print("LEADS:", tl)
print("PROPOSTAS:", tp)
print("REUNIOES:", tm)

print("")
print("EXECUTADO")

print("LEADS:", el)
print("PROPOSTAS:", ep)
print("REUNIOES:", em)

print("")
print(
    "EXECUCAO:",
    execution,
    "%"
)

print("")
print(
    "RECEITA POTENCIAL:",
    potential_revenue
)

print("")
print("DATABASE:")
print(DB)

print("")
print("CONCLUIDO")

conn.close()




