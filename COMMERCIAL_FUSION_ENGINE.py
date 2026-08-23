import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

MASTER = r"C:\IOTEC\iotec_operational.db"

FONTES = [

    r"C:\IOTEC\enterprise.db",
    r"C:\IOTEC\tower.db",
    r"C:\IOTEC\iotec_global.db",
    r"C:\IOTEC\opportunity_radar.db",
    r"C:\IOTEC\iotec_core.db"

]

master = sqlite3.connect(MASTER)
m = master.cursor()

m.execute("""
CREATE TABLE IF NOT EXISTS unified_assets(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source_db TEXT,
    source_table TEXT,
    records_found INTEGER,
    imported_at TEXT

)
""")

for banco in FONTES:
    pass

    try:
        pass

        c = sqlite3.connect(banco)

        cur = c.cursor()

        tabelas = cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """).fetchall()

        for t in tabelas:
            pass

            tabela = t[0]

            try:
                pass

                qtd = cur.execute(
                    f"SELECT COUNT(*) FROM {tabela}"
                ).fetchone()[0]

                m.execute(
                    """
                    INSERT INTO unified_assets(
                    source_db,
                    source_table,
                    records_found,
                    imported_at
                    )
                    VALUES(?,?,?,datetime('now'))
                    """,
                    (
                        banco,
                        tabela,
                        qtd
                    )
                )

            except:
                pass

        c.close()

    except:
        pass

master.commit()
master.close()

print("")
print("====================================")
print("COMMERCIAL FUSION FINALIZADA")
print("====================================")
print("")




