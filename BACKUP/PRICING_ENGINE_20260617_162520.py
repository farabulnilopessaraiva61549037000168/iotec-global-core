import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS pricing_rules(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    service TEXT,

    base_value REAL,

    min_value REAL,

    max_value REAL

)

""")

conn.commit()

regras = [

    ("DIAGNOSTICO",500,500,1500),

    ("AUTOMACAO",2500,1500,10000),

    ("ANALISE_DADOS",3000,2000,12000),

    ("IA_EMPRESARIAL",5000,3000,25000),

    ("IMPLANTACAO_COMPLETA",10000,5000,50000)

]

for r in regras:
    pass

    existe = cur.execute(

        "SELECT COUNT(*) FROM pricing_rules WHERE service=?",

        (r[0],)

    ).fetchone()[0]

    if existe == 0:
        pass

        cur.execute(

            """
            INSERT INTO pricing_rules(
                service,
                base_value,
                min_value,
                max_value
            )
            VALUES(?,?,?,?)
            """,

            r

        )

conn.commit()

print("PRICING ENGINE INSTALADO")

conn.close()


