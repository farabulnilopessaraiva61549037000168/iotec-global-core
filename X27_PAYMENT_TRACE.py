import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC\iotec_operational.db"

REQUEST_ID = "2e48289f-6fb7-4c9a-a641-b0be7a658226"

print("=" * 70)
print("X27 PAYMENT TRACE")
print("=" * 70)

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("\nREQUEST")

cur.execute("""
SELECT *
FROM requests
WHERE request_id = ?
""", (REQUEST_ID,))

request = cur.fetchone()

if request:

    print(request)

    client_id = request[2]

    print("\nCLIENTE")

    cur.execute("""
    SELECT *
    FROM clients
    WHERE client_id = ?
    """, (client_id,))

    cliente = cur.fetchone()

    if cliente:
        print(cliente)

print("\nPAGAMENTO")

cur.execute("""
SELECT *
FROM payments
WHERE request_id = ?
""", (REQUEST_ID,))

for p in cur.fetchall():
    print(p)

conn.close()

print()
print("=" * 70)
print("FIM")
print("=" * 70)



