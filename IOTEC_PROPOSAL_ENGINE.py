import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import json
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_PROPOSALS.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

CREATE TABLE IF NOT EXISTS proposals(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    created_at TEXT,

    company TEXT,

    product TEXT,

    value REAL,

    status TEXT,

    notes TEXT

)

""")

proposals = [

    (
        str(datetime.now()),
        "Prefeitura Modelo",
        "GovTech Analytics",
        15000.00,
        "ENVIADA",
        "Aguardando retorno"
    ),

    (
        str(datetime.now()),
        "Clinica Vida",
        "Auditoria Inteligente",
        8000.00,
        "EM_ANALISE",
        "Reuniao realizada"
    ),

    (
        str(datetime.now()),
        "Escola Alfa",
        "Auditoria Operacional",
        5000.00,
        "RASCUNHO",
        "Preparando proposta"
    )

]

for row in proposals:
    pass

    cur.execute("""

    INSERT INTO proposals(

        created_at,
        company,
        product,
        value,
        status,
        notes

    )

    VALUES(

        ?,?,?,?,?,?

    )

    """, row)

conn.commit()

total = cur.execute("""

SELECT COUNT(*)

FROM proposals

""").fetchone()[0]

proposal_value = cur.execute("""

SELECT

COALESCE(SUM(value),0)

FROM proposals

""").fetchone()[0]

print("")
print("===================================")
print("IOTEC PROPOSAL ENGINE")
print("===================================")
print("")

print("TOTAL PROPOSTAS:", total)
print(
    f"VALOR TOTAL: R$ {proposal_value:,.2f}"
)

print("")

for row in cur.execute("""

SELECT

    company,
    product,
    value,
    status

FROM proposals

ORDER BY value DESC

"""):

    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"R$ {row[2]:,.2f} | "
        f"{row[3]}"
    )

report = {

    "generated": str(datetime.now()),
    "total_proposals": total,
    "proposal_value": proposal_value

}

with open(
    r"C:\IOTEC\IOTEC_PROPOSALS_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

with open(
    r"C:\IOTEC\IOTEC_PROPOSALS_REPORT.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC PROPOSAL ENGINE\n")
    f.write("===================================\n\n")

    f.write(
        f"TOTAL PROPOSTAS: {total}\n"
    )

    f.write(
        f"VALOR TOTAL: R$ {proposal_value:,.2f}\n"
    )

print("")
print("DATABASE:")
print(DB)

print("")
print("TXT:")
print(
    r"C:\IOTEC\IOTEC_PROPOSALS_REPORT.txt"
)

print("")
print("JSON:")
print(
    r"C:\IOTEC\IOTEC_PROPOSALS_REPORT.json"
)

conn.close()




