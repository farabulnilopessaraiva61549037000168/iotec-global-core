import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC MISSION CYCLE ENGINE
# FECHA CICLO E ABRE NOVA MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_MISSION_EXECUTION.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# ==========================================================
# ÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡LTIMA MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

row = cur.execute("""

SELECT

    id,
    product,
    status,
    execution_percent,

    target_leads,
    target_proposals,
    target_meetings,

    potential_revenue

FROM missions

ORDER BY id DESC

LIMIT 1

""").fetchone()

if not row:
    pass

    print("NENHUMA MISSAO")
    conn.close()
    raise SystemExit()

mission_id = row[0]
product = row[1]
status = row[2]
execution = row[3]

target_leads = row[4]
target_proposals = row[5]
target_meetings = row[6]

potential_revenue = row[7]

print("")
print("===================================")
print("IOTEC MISSION CYCLE ENGINE")
print("===================================")

print("")
print("MISSION:", mission_id)
print("STATUS:", status)
print("EXECUTION:", execution)

# ==========================================================
# VERIFICA CICLO
# ==========================================================

if status != "COMPLETED":
    pass

    print("")
    print("MISSAO AINDA NAO FINALIZADA")

    conn.close()
    raise SystemExit()

# ==========================================================
# EVITA DUPLICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

exists = cur.execute("""

SELECT COUNT(*)

FROM missions

WHERE status='OPEN'

""").fetchone()[0]

if exists > 0:
    pass

    print("")
    print("JA EXISTE MISSAO ABERTA")

    conn.close()
    raise SystemExit()

# ==========================================================
# CRIA NOVA MISSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

new_leads = max(
    target_leads + 1,
    target_leads
)

new_proposals = max(
    target_proposals,
    2
)

new_meetings = max(
    target_meetings,
    1
)

new_revenue = potential_revenue * 1.2

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

    new_leads,
    new_proposals,
    new_meetings,

    0,
    0,
    0,

    0,

    new_revenue,

    "OPEN"

))

conn.commit()

new_id = cur.lastrowid

print("")
print("NOVA MISSAO CRIADA")

print("")
print("MISSION:", new_id)

print("")
print("META")

print("LEADS:", new_leads)
print("PROPOSTAS:", new_proposals)
print("REUNIOES:", new_meetings)

print("")
print(
    "RECEITA POTENCIAL:",
    round(new_revenue, 2)
)

print("")
print("CONCLUIDO")

conn.close()


