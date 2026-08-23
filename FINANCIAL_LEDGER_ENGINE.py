import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC FINANCIAL LEDGER ENGINE")
print("==================================================")
print("")

cur.execute("""

CREATE TABLE IF NOT EXISTS financial_ledger(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    project_code TEXT,

    amount REAL,

    type TEXT,

    status TEXT,

    created_at TEXT,

    paid_at TEXT

)

""")

conn.commit()

projetos = cur.execute("""

SELECT

    company,
    project_code,
    estimated_value,
    status

FROM client_projects

""").fetchall()

gerados = 0

for empresa, codigo, valor, status in projetos:
    pass

    existe = cur.execute("""

    SELECT id

    FROM financial_ledger

    WHERE project_code=?

    """,(codigo,)).fetchone()

    if existe:
        continue

    financeiro_status = "ABERTO"

    if status == "ENTREGUE":
        financeiro_status = "PAGO"

    cur.execute("""

    INSERT INTO financial_ledger(

        company,
        project_code,
        amount,
        type,
        status,
        created_at,
        paid_at

    )

    VALUES(

        ?,?,?,?,?,?,?

    )

    """,(

        empresa,
        codigo,
        valor,
        "RECEITA",
        financeiro_status,
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

        datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if financeiro_status == "PAGO"
        else None

    ))

    gerados += 1

conn.commit()

receita_total = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

""").fetchone()[0]

receita_paga = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

WHERE status='PAGO'

""").fetchone()[0]

receita_aberta = cur.execute("""

SELECT IFNULL(
SUM(amount),0
)

FROM financial_ledger

WHERE status='ABERTO'

""").fetchone()[0]

print("LANCAMENTOS")
print("")

lancamentos = cur.execute("""

SELECT

company,
project_code,
amount,
status

FROM financial_ledger

ORDER BY amount DESC

""").fetchall()

for l in lancamentos:
    pass

    print(
        f"{l[0]} | "
        f"{l[1]} | "
        f"R$ {l[2]:,.2f} | "
        f"{l[3]}"
    )

print("")
print("==================================================")
print("RESUMO FINANCEIRO")
print("==================================================")
print("")

print(f"NOVOS LANCAMENTOS: {gerados}")
print(f"RECEITA TOTAL: R$ {receita_total:,.2f}")
print(f"RECEITA RECEBIDA: R$ {receita_paga:,.2f}")
print(f"RECEITA EM ABERTO: R$ {receita_aberta:,.2f}")

print("")
print("==================================================")

conn.close()




