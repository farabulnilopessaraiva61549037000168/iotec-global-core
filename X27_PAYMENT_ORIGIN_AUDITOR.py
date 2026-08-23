import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from pathlib import Path

ROOT = Path(r"C:\IOTEC")

PAYMENT_ID = "3f9b3fb1-4f9f-4f4a-a36f-c31b2766ce60"

print("=" * 70)
print("X27 PAYMENT ORIGIN AUDITOR")
print("=" * 70)
print()
print("PAYMENT ID:", PAYMENT_ID)
print()

encontrado = False

for db_file in ROOT.glob("*.db"):

    print("-" * 70)
    print("BANCO:", db_file.name)

    try:

        conn = sqlite3.connect(db_file)
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

            try:

                cur.execute(f"PRAGMA table_info({tabela})")
                colunas = [x[1] for x in cur.fetchall()]

                cur.execute(f"SELECT * FROM {tabela}")
                registros = cur.fetchall()

                for registro in registros:

                    texto = str(registro)

                    if PAYMENT_ID in texto:

                        encontrado = True

                        print()
                        print("LOCALIZADO")
                        print("TABELA :", tabela)
                        print("COLUNAS:")
                        print(colunas)
                        print()
                        print("REGISTRO:")
                        print(registro)
                        print()

            except Exception:
                pass

        conn.close()

    except Exception as erro:

        print("ERRO:", erro)

print()
print("=" * 70)

if encontrado:
    print("ORIGEM LOCALIZADA")
else:
    print("PAGAMENTO NAO ENCONTRADO")

print("=" * 70)



