# ==========================================================
# 068_COLLECTION_ORCHESTRATOR.py
# IOTEC COLLECTION ORCHESTRATOR
# ==========================================================

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"

db = sqlite3.connect(DB, timeout=30)
cursor = db.cursor()

# ==========================================================
# FILA DE COLETA
# ==========================================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS collection_queue(

id INTEGER PRIMARY KEY AUTOINCREMENT,

mission_code TEXT,

source TEXT,

status TEXT,

started_at TEXT,

finished_at TEXT,

records_found INTEGER,

message TEXT

)

""")

db.commit()

print("="*70)
print("IOTEC COLLECTION ORCHESTRATOR")
print("="*70)
print()

cursor.execute("""

SELECT
codigo,
nome,
status

FROM intelligence_missions

WHERE status='AGUARDANDO'

ORDER BY prioridade DESC

""")

missoes = cursor.fetchall()

print("MISSÃƒâ€¢ES ENCONTRADAS :", len(missoes))
print()

for codigo, nome, status in missoes:

    print(f"[MISSÃƒÆ'O] {codigo}")
    print(nome)
    print()

    fontes = [

        "Google Maps",
        "Google Business",
        "LinkedIn",
        "CRM",
        "Bases PÃƒÂºblicas"

    ]

    for fonte in fontes:

        cursor.execute("""

        INSERT INTO collection_queue(

        mission_code,

        source,

        status,

        started_at,

        records_found,

        message

        )

        VALUES(?,?,?,?,?,?)

        """,(

        codigo,

        fonte,

        "AGUARDANDO",

        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        0,

        "Conector aguardando implementaÃƒÂ§ÃƒÂ£o."

        ))

        print(" ->",fonte)

    print("-"*60)

db.commit()

print()
print("="*70)
print("INDICADORES")
print("="*70)
print()

cursor.execute("SELECT COUNT(*) FROM collection_queue")
fila = cursor.fetchone()[0]

print("Conectores na fila :", fila)

print()
print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A InteligÃƒÂªncia agora")
print("despacha missÃƒÂµes")
print("para conectores")
print("reais.")

print()
print("Cada conector")
print("serÃƒÂ¡ responsÃƒÂ¡vel")
print("por uma fonte")
print("de mercado.")

db.close()


