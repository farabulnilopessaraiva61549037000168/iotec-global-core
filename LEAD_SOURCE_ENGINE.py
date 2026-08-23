import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime
import sys

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ==================================================
# TABELA
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS lead_sources(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    source TEXT,

    sector TEXT,

    estimated_value REAL,

    status TEXT,

    created_at TEXT

)

""")

conn.commit()

# ==================================================
# REGISTRO MANUAL
# ==================================================

if len(sys.argv) > 2:
    pass

    empresa = sys.argv[1]
    origem = sys.argv[2]

    dados = cur.execute("""

    SELECT
        company,
        sector,
        estimated_value,
        status

    FROM commercial_opportunities

    WHERE company=?

    """,(empresa,)).fetchone()

    if dados:
        pass

        cur.execute("""

        INSERT INTO lead_sources(

            company,
            source,
            sector,
            estimated_value,
            status,
            created_at

        )

        VALUES(

            ?,?,?,?,?,?

        )

        """,(

            dados[0],
            origem,
            dados[1],
            dados[2],
            dados[3],
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

        ))

        conn.commit()

        print("")
        print("===================================")
        print("LEAD SOURCE ENGINE")
        print("===================================")
        print("")
        print("REGISTRADO")
        print("")
        print("EMPRESA:", dados[0])
        print("ORIGEM:", origem)
        print("")
        print("===================================")

    else:
        pass

        print("")
        print("EMPRESA NAO ENCONTRADA")
        print("")

    conn.close()
    raise SystemExit

# ==================================================
# RELATORIO
# ==================================================

print("")
print("===================================")
print("LEAD SOURCE ENGINE")
print("===================================")
print("")

fontes = cur.execute("""

SELECT

    source,
    COUNT(*),
    IFNULL(SUM(estimated_value),0)

FROM lead_sources

GROUP BY source

ORDER BY 3 DESC

""").fetchall()

if not fontes:
    pass

    print("NENHUMA ORIGEM REGISTRADA")
    print("")
    print("EXEMPLO:")
    print("")
    print(
        'python LEAD_SOURCE_ENGINE.py '
        '"ALFA INDUSTRIAL" '
        '"INDICACAO"'
    )
    print("")
    conn.close()
    raise SystemExit

print("RANKING DE ORIGENS")
print("")

for f in fontes:
    pass

    print(
        f"{f[0]} | "
        f"LEADS={f[1]} | "
        f"VALOR=R$ {f[2]:,.2f}"
    )

print("")
print("===================================")

conn.close()




