import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import sqlite3
from datetime import datetime

print("=" * 60)
print("X27 REVENUE FLOW AUDIT")
print("=" * 60)
print()
print("DATA:", datetime.now())
print()

ROOT = r"C:\IOTEC"

dbs = []

for pasta, _, arquivos in os.walk(ROOT):
    for arquivo in arquivos:
        if arquivo.lower().endswith(".db"):
            dbs.append(os.path.join(pasta, arquivo))

print("=" * 60)
print("DATABASES ENCONTRADOS")
print("=" * 60)

for db in dbs:
    print(db)

print()

for db in dbs:

    print("=" * 60)
    print("ANALISANDO:", db)
    print("=" * 60)

    try:

        conn = sqlite3.connect(db)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )

        tabelas = cur.fetchall()

        if not tabelas:
            print("SEM TABELAS")
            conn.close()
            continue

        for tabela in tabelas:

            nome = tabela[0]

            print()
            print("TABELA:", nome)

            try:

                cur.execute(
                    f"SELECT COUNT(*) FROM [{nome}]"
                )

                total = cur.fetchone()[0]

                print("REGISTROS:", total)

            except Exception as erro:
                print("ERRO:", erro)

        conn.close()

    except Exception as erro:
        print("FALHA:", erro)

print()
print("=" * 60)
print("AUDITORIA FINALIZADA")
print("=" * 60)



