import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import sys

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

if len(sys.argv) < 2:
    pass

    print("USO:")
    print("python APPROVE_PROPOSAL.py 1")
    exit()

op_id = int(sys.argv[1])

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

UPDATE pipeline

SET

approved=1,
status='PAGAMENTO_PENDENTE',
last_contact=datetime('now')

WHERE opportunity_id=?

""",(op_id,))

conn.commit()
conn.close()

print("")
print("==============================")
print("PROPOSTA APROVADA")
print("==============================")
print("OPPORTUNITY:", op_id)
print("")




