import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

dados = cur.execute("""

SELECT

o.id,
l.company,
l.email,
l.sector,
p.status,
p.proposal_value

FROM opportunities o

JOIN leads l
ON l.id = o.lead_id

JOIN pipeline p
ON p.opportunity_id = o.id

ORDER BY o.id

""").fetchall()

print()
print("=" * 90)
print("IOTEC LEAD OPERATIONS CENTER")
print("=" * 90)
print()

for item in dados:
    pass

    print(f"OPPORTUNITY..... {item[0]}")
    print(f"EMPRESA......... {item[1]}")
    print(f"EMAIL........... {item[2]}")
    print(f"SETOR........... {item[3]}")
    print(f"STATUS.......... {item[4]}")
    print(f"VALOR........... R$ {item[5]:,.2f}")
    print("-" * 90)

print()
print("TOTAL DE REGISTROS:", len(dados))
print()

conn.close()




