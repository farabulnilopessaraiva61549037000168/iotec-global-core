import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\IOTEC_REAL_LEADS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
SELECT COUNT(*)
FROM real_leads
""")

total = cur.fetchone()[0]

print("=" * 70)
print("IOTEC REAL BUSINESS STATUS")
print("=" * 70)

print()
print("LEADS REAIS:", total)
print()

cur.execute("""
SELECT status, COUNT(*)
FROM real_leads
GROUP BY status
""")

for row in cur.fetchall():

    print(
        f"{row[0]:15} {row[1]}"
    )

print()

if total == 0:

    print("ALERTA")
    print("BANCO AINDA VAZIO")

elif total < 10:

    print("FASE 1")
    print("CAPTURA DE LEADS")

elif total < 50:

    print("FASE 2")
    print("PROSPECCAO ATIVA")

else:

    print("FASE 3")
    print("OPERACAO COMERCIAL")

conn.close()



