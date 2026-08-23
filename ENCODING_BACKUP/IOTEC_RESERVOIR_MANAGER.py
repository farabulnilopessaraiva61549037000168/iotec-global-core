import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC RESERVOIR MANAGER
# DISTRIBUI CONHECIMENTO DO WAREHOUSE
# PARA RESERVATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS ESPECIALIZADOS
# ==========================================================

import sqlite3
from datetime import datetime

WAREHOUSE_DB = r"C:\IOTEC\IOTEC_KNOWLEDGE_WAREHOUSE.db"

conn = sqlite3.connect(WAREHOUSE_DB)
cur = conn.cursor()

# ==========================================================
# RESERVATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS reservoirs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    reservoir TEXT,

    source_motor TEXT,

    item_id INTEGER,

    title TEXT,

    value_score INTEGER

)

""")

conn.commit()

# ==========================================================
# REGRAS DE DESTINO
# ==========================================================

RULES = {

    "BRAIN": "INTELLIGENCE",

    "MEMORY": "INTELLIGENCE",

    "CONTROL": "OPERATIONS",

    "COMMERCIAL": "COMMERCIAL",

    "REVENUE": "REVENUE",

    "CAPABILITY": "CAPABILITIES"
}

# ==========================================================
# CARREGA WAREHOUSE
# ==========================================================

rows = cur.execute("""

SELECT

    id,
    source_motor,
    category,
    value_score

FROM warehouse

""").fetchall()

inserted = 0

for row in rows:
    pass

    item_id = row[0]
    source = row[1]
    category = row[2]
    value = row[3]

    reservoir = RULES.get(
        category,
        "OPERATIONS"
    )

    exists = cur.execute("""

    SELECT COUNT(*)

    FROM reservoirs

    WHERE item_id = ?

    """,

    (item_id,)

    ).fetchone()[0]

    if exists:
        continue

    cur.execute("""

    INSERT INTO reservoirs (

        timestamp,
        reservoir,
        source_motor,
        item_id,
        value_score

    )

    VALUES (

        ?,?,?,?,?

    )

    """,

    (

        str(datetime.now()),
        reservoir,
        source,
        item_id,
        value

    ))

    inserted += 1

conn.commit()

# ==========================================================
# RESUMO
# ==========================================================

print("")
print("===================================")
print("IOTEC RESERVOIR MANAGER")
print("===================================")

print("")
print("NOVOS ITENS:", inserted)

print("")
print("RESERVATORIOS")

summary = cur.execute("""

SELECT

    reservoir,
    COUNT(*)

FROM reservoirs

GROUP BY reservoir

ORDER BY COUNT(*) DESC

""").fetchall()

for reservoir, total in summary:
    pass

    print(
        f"{reservoir}: {total}"
    )

print("")
print("DATABASE:")
print(WAREHOUSE_DB)

print("")
print("CONCLUIDO")

conn.close()






