import sqlite3
import glob

for db in glob.glob("*.db"):
    print("=" * 70)
    print(db)

    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in cur.fetchall()]

        print(f"Tabelas: {len(tables)}")

        for table in tables:
            try:
                cur.execute(f'SELECT COUNT(*) FROM "{table}"')
                count = cur.fetchone()[0]
                print(f"  {table:<40} {count}")
            except Exception as e:
                print(f"  {table:<40} ERRO")

        conn.close()

    except Exception as e:
        print("Erro:", e)

    print()



