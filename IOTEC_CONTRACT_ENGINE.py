import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_CONTRACTS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS contracts(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    product TEXT,

    contract_value REAL,

    status TEXT,

    notes TEXT

)
""")

contracts = [

    (
        str(datetime.now()),
        "CLIENTE_EXEMPLO",
        "Auditoria Operacional",
        5000.00,
        "ATIVO",
        "Contrato inicial"
    )

]

for row in contracts:
    pass

    cur.execute("""

    INSERT INTO contracts(

        created_at,
        company,
        product,
        contract_value,
        status,
        notes

    )

    VALUES(

        ?,?,?,?,?,?

    )

    """, row)

conn.commit()

total_contracts = cur.execute("""

SELECT COUNT(*)

FROM contracts

""").fetchone()[0]

revenue = cur.execute("""

SELECT
COALESCE(SUM(contract_value),0)

FROM contracts

WHERE status='ATIVO'

""").fetchone()[0]

report = {

    "generated": str(datetime.now()),
    "contracts": total_contracts,
    "revenue": revenue

}

with open(
    r"C:\IOTEC\IOTEC_CONTRACT_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("IOTEC CONTRACT ENGINE")
print("===================================")
print("")

print("CONTRATOS:", total_contracts)
print(f"RECEITA REAL: R$ {revenue:,.2f}")

print("")
print("DATABASE:")
print(DB)

conn.close()




