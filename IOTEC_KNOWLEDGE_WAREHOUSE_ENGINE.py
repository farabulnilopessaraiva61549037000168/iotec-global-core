import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC KNOWLEDGE WAREHOUSE ENGINE
# ARMAZÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°M CENTRAL DE CONHECIMENTO
# ==========================================================

import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_KNOWLEDGE_WAREHOUSE.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==========================================================
# CONHECIMENTO BRUTO
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS warehouse (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    source_motor TEXT,

    category TEXT,

    title TEXT,

    content TEXT,

    relevance INTEGER,

    value_score INTEGER,

    status TEXT

)

""")

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

    value_score INTEGER

)

""")

# ==========================================================
# CAPACIDADES
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS capabilities (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    capability TEXT,

    source TEXT,

    maturity INTEGER,

    economic_value INTEGER

)

""")

conn.commit()

# ==========================================================
# CARREGA TORRE
# ==========================================================

MASTER_FILE = r"C:\IOTEC\IOTEC_MASTER_TOWER.json"

with open(
    MASTER_FILE,
    "r",
    encoding="utf-8"
) as f:

    tower = json.load(f)

# ==========================================================
# REGISTRO INICIAL
# ==========================================================

timestamp = str(datetime.now())

seed_data = [

    (
        tower["master_brain"],
        "BRAIN",
        "MASTER BRAIN ONLINE",
        "CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro mestre conectado ao Warehouse",
        100,
        100
    ),

    (
        tower["unified_brain"],
        "BRAIN",
        "UNIFIED BRAIN ONLINE",
        "CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro unificado conectado ao Warehouse",
        90,
        90
    ),

    (
        tower["control_tower"],
        "CONTROL",
        "CONTROL TOWER ONLINE",
        "Torre operacional conectada",
        95,
        95
    ),

    (
        tower["memory"],
        "MEMORY",
        "MEMORY ONLINE",
        "MemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria central conectada",
        85,
        85
    )

]

for item in seed_data:
    pass

    cur.execute("""

    INSERT INTO warehouse (

        timestamp,
        source_motor,
        category,
        title,
        content,
        relevance,
        value_score,
        status

    )

    VALUES (

        ?,?,?,?,?,?,?,?

    )

    """,

    (

        timestamp,
        item[0],
        item[1],
        item[2],
        item[3],
        item[4],
        item[5],
        "ACTIVE"

    ))

conn.commit()

# ==========================================================
# RESUMO
# ==========================================================

warehouse_count = cur.execute(
    "SELECT COUNT(*) FROM warehouse"
).fetchone()[0]

print("")
print("===================================")
print("IOTEC KNOWLEDGE WAREHOUSE")
print("===================================")

print("")
print("ITENS NO ARMAZEM:", warehouse_count)

print("")
print("MASTER BRAIN:")
print(tower["master_brain"])

print("")
print("UNIFIED BRAIN:")
print(tower["unified_brain"])

print("")
print("CONTROL TOWER:")
print(tower["control_tower"])

print("")
print("MEMORY:")
print(tower["memory"])

print("")
print("DATABASE:")
print(DB)

print("")
print("CONCLUIDO")

conn.close()




