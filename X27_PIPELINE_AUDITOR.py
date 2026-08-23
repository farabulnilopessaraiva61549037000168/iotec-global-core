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

print("=" * 70)
print("X27 PIPELINE AUDITOR")
print("=" * 70)

status_list = [
    "DESCOBERTO",
    "QUALIFICADO",
    "CONTATADO",
    "REUNIAO",
    "PROPOSTA",
    "NEGOCIACAO",
    "FECHADO",
    "PERDIDO"
]

total = 0

print()

for status in status_list:

    cur.execute(
        "SELECT COUNT(*) FROM real_leads WHERE status=?",
        (status,)
    )

    qtd = cur.fetchone()[0]

    total += qtd

    print(f"{status:15} {qtd}")

print()
print("=" * 70)

cur.execute("""
SELECT COALESCE(SUM(estimated_value),0)
FROM real_leads
WHERE status <> 'PERDIDO'
""")

pipeline = cur.fetchone()[0]

print("LEADS..............", total)
print("PIPELINE...........", f"R$ {pipeline:,.2f}")

print()
print("=" * 70)
print("TOP OPORTUNIDADES")
print("=" * 70)

cur.execute("""
SELECT
company,
segment,
estimated_value,
status
FROM real_leads
ORDER BY estimated_value DESC
LIMIT 10
""")

for row in cur.fetchall():

    print(
        f"{row[0]:30} "
        f"{row[1]:15} "
        f"R$ {row[2]:,.2f} "
        f"{row[3]}"
    )

conn.close()

print()
print("=" * 70)
print("AUDITORIA FINALIZADA")
print("=" * 70)



