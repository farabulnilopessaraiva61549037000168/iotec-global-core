import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    segment TEXT,

    city TEXT,

    state TEXT,

    contact_name TEXT,

    email TEXT,

    phone TEXT,

    status TEXT,

    priority INTEGER

)
""")

accounts = [

    (
        str(datetime.now()),
        "Escola Alfa",
        "EDUCACAO",
        "Quixada",
        "CE",
        "",
        "",
        "",
        "PROSPECCAO",
        10
    ),

    (
        str(datetime.now()),
        "Clinica Vida",
        "SAUDE",
        "Fortaleza",
        "CE",
        "",
        "",
        "",
        "QUALIFICACAO",
        9
    ),

    (
        str(datetime.now()),
        "Prefeitura Modelo",
        "PREFEITURAS",
        "Sobral",
        "CE",
        "",
        "",
        "",
        "PROSPECCAO",
        10
    )

]

for row in accounts:
    pass

    cur.execute("""

    INSERT INTO accounts(

        created_at,
        company,
        segment,
        city,
        state,
        contact_name,
        email,
        phone,
        status,
        priority

    )

    VALUES(

        ?,?,?,?,?,?,?,?,?,?

    )

    """, row)

conn.commit()

total = cur.execute("""
SELECT COUNT(*)
FROM accounts
""").fetchone()[0]

print("")
print("===================================")
print("IOTEC ACCOUNT REGISTRY")
print("===================================")
print("")

print("TOTAL CONTAS:", total)
print("")

for row in cur.execute("""

SELECT

    company,
    segment,
    city,
    state,
    status,
    priority

FROM accounts

ORDER BY priority DESC

"""):

    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"{row[2]}/{row[3]} | "
        f"{row[4]} | "
        f"P{row[5]}"
    )

report = {

    "generated": str(datetime.now()),
    "accounts": total

}

with open(
    r"C:\IOTEC\IOTEC_ACCOUNT_REGISTRY.json",
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
print("DATABASE:")
print(DB)

conn.close()




