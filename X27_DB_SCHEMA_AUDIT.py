import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# X27_DB_SCHEMA_AUDIT.py

import sqlite3
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

for db in ROOT.glob("*.db"):

    print("\n" + "=" * 70)
    print(db.name)
    print("=" * 70)

    try:

        conn = sqlite3.connect(db)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """)

        tabelas = [x[0] for x in cur.fetchall()]

        for tabela in tabelas:

            print("\nTABELA:", tabela)

            cur.execute(f"PRAGMA table_info({tabela})")

            for coluna in cur.fetchall():

                print(
                    coluna[0],
                    coluna[1],
                    coluna[2]
                )

        conn.close()

    except Exception as erro:

        print("ERRO:", erro)



