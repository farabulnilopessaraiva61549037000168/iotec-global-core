import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC CONTROL TOWER LEDGER
# CENTRAL OPERACIONAL DE PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ==========================================================

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_CONTROL_TOWER_LEDGER.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==========================================================
# TABELA DE MOTORES
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS motors (

    motor TEXT PRIMARY KEY,

    layer TEXT,

    interval_seconds INTEGER,

    last_start TEXT,

    last_finish TEXT,

    status TEXT,

    executions INTEGER DEFAULT 0,

    success INTEGER DEFAULT 0,

    errors INTEGER DEFAULT 0,

    total_value INTEGER DEFAULT 0,

    reservoir TEXT,

    last_production TEXT
)

""")

# ==========================================================
# HISTORICO
# ==========================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS production_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    motor TEXT,

    layer TEXT,

    status TEXT,

    duration_seconds REAL,

    value_score INTEGER,

    production TEXT,

    reservoir TEXT
)

""")

# ==========================================================
# GRADE
# ==========================================================

GRID = {

    "REALTIME": {

        "interval": 10,

        "motors": [

            "IOTEC_CORE_RUNNER",
            "IOTEC_CONTROL_TOWER_ENGINE",
            "IOTEC_CORE_LIVE_QUEUE"
        ]
    },

    "COMMERCIAL": {

        "interval": 300,

        "motors": [

            "CRM_ENGINE",
            "LEAD_SCORE_ENGINE",
            "SALES_BRAIN",
            "NEGOTIATION_ENGINE",
            "PROPOSAL_ENGINE",
            "SALES_AUTOPILOT_ENGINE"
        ]
    },

    "REVENUE": {

        "interval": 1800,

        "motors": [

            "REVENUE_DISCOVERY_ENGINE",
            "REVENUE_OPERATION_CENTER",
            "AUTO_MONETIZATION_ENGINE",
            "PRICING_ENGINE"
        ]
    },

    "INTELLIGENCE": {

        "interval": 7200,

        "motors": [

            "ECONOMIC_INTELLIGENCE",
            "IOTEC_CENTRAL_BRAIN",
            "IOTEC_MEMORY_ENGINE",
            "IOTEC_UNIFIED_BRAIN"
        ]
    },

    "STRATEGIC": {

        "interval": 21600,

        "motors": [

            "IOTEC_CAPABILITY_HUNTER",
            "MISSION_01_CAPABILITY_CATALOG",
            "TOP_ASSETS_ENGINE",
            "IOTEC_REVENUE_IDENTITY_ENGINE"
        ]
    }
}

# ==========================================================
# REGISTRA MOTORES
# ==========================================================

for layer, cfg in GRID.items():
    pass

    for motor in cfg["motors"]:
        pass

        cur.execute("""

        INSERT OR IGNORE INTO motors (

            motor,
            layer,
            interval_seconds,
            status

        )

        VALUES (

            ?,
            ?,
            ?,
            'REGISTERED'

        )

        """,

        (

            motor,
            layer,
            cfg["interval"]

        ))

conn.commit()

# ==========================================================
# RESUMO
# ==========================================================

print("")
print("===================================")
print("IOTEC CONTROL TOWER LEDGER")
print("===================================")
print("")

rows = cur.execute("""

SELECT
layer,
COUNT(*)

FROM motors

GROUP BY layer

""").fetchall()

for layer, total in rows:
    pass

    print(
        f"{layer}: {total}"
    )

print("")
print("DATABASE:")
print(DB)
print("")
print("CONCLUIDO")

conn.close()




