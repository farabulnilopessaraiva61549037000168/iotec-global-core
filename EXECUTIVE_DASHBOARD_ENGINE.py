import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"
META = 50000

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC EXECUTIVE DASHBOARD")
print("==================================================")
print("")

leads = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

pipeline = cur.execute("""

SELECT IFNULL(
SUM(estimated_value),0
)

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

""").fetchone()[0]

clientes = cur.execute("""

SELECT COUNT(*)

FROM client_projects

""").fetchone()[0]

projetos_entregues = cur.execute("""

SELECT COUNT(*)

FROM client_projects

WHERE status='ENTREGUE'

""").fetchone()[0]

receita_recebida = cur.execute("""

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

atingimento = 0

if META > 0:
    pass

    atingimento = (
        receita_recebida * 100
    ) / META

print("INDICADORES EXECUTIVOS")
print("")

print(f"LEADS: {leads}")
print(f"PIPELINE: R$ {pipeline:,.2f}")
print(f"CLIENTES: {clientes}")
print(f"PROJETOS ENTREGUES: {projetos_entregues}")

print("")
print("FINANCEIRO")
print("")

print(
    f"RECEITA RECEBIDA: "
    f"R$ {receita_recebida:,.2f}"
)

print(
    f"RECEITA EM ABERTO: "
    f"R$ {receita_aberta:,.2f}"
)

print(
    f"META: "
    f"R$ {META:,.2f}"
)

print(
    f"ATINGIMENTO: "
    f"{atingimento:.2f}%"
)

print("")
print("==================================================")
print("STATUS EXECUTIVO")
print("==================================================")
print("")

if atingimento >= 100:
    pass

    print("META ATINGIDA")

elif atingimento >= 70:
    pass

    print("META PROXIMA")

elif atingimento >= 40:
    pass

    print("TRACAO COMERCIAL")

else:
    pass

    print("FOCO EM CONVERSAO")

print("")
print("==================================================")

conn.close()




