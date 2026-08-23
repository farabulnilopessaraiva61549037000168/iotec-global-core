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

# ==================================================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TRICAS REAIS
# ==================================================

leads = cur.execute(
    "SELECT COUNT(*) FROM leads"
).fetchone()[0]

opportunities = cur.execute(
    "SELECT COUNT(*) FROM opportunities"
).fetchone()[0]

relatorios = cur.execute(
    """
    SELECT COUNT(*)
    FROM pipeline
    WHERE report_sent=1
    """
).fetchone()[0]

propostas = cur.execute(
    """
    SELECT COUNT(*)
    FROM pipeline
    WHERE proposal_sent=1
    """
).fetchone()[0]

clientes = cur.execute(
    """
    SELECT COUNT(*)
    FROM pipeline
    WHERE status='CLIENTE_ATIVO'
    """
).fetchone()[0]

pagamentos_pendentes = cur.execute(
    """
    SELECT COUNT(*)
    FROM pipeline
    WHERE status='PAGAMENTO_PENDENTE'
    """
).fetchone()[0]

receita_prevista = cur.execute(
    """
    SELECT COALESCE(
        SUM(proposal_value),
        0
    )
    FROM pipeline
    """
).fetchone()[0]

receita_recebida = cur.execute(
    """
    SELECT COALESCE(
        SUM(proposal_value),
        0
    )
    FROM pipeline
    WHERE payment_received=1
    """
).fetchone()[0]

conversao = 0

if opportunities > 0:
    pass

    conversao = round(
        (clientes / opportunities) * 100,
        2
    )

# ==================================================
# TORRE
# ==================================================

print()
print("=" * 65)
print("IOTEC EXECUTIVE COMMAND TOWER")
print("=" * 65)

print()

print(f"LEADS....................... {leads}")
print(f"OPPORTUNITIES............... {opportunities}")
print(f"RELATORIOS.................. {relatorios}")
print(f"PROPOSTAS................... {propostas}")
print(f"PAGAMENTOS PENDENTES........ {pagamentos_pendentes}")
print(f"CLIENTES ATIVOS............. {clientes}")

print()

print(
    f"RECEITA PREVISTA............ R$ {receita_prevista:,.2f}"
)

print(
    f"RECEITA RECEBIDA............ R$ {receita_recebida:,.2f}"
)

print(
    f"TAXA DE CONVERSAO........... {conversao}%"
)

print()

print("=" * 65)

# ==================================================
# CLIENTES ATIVOS
# ==================================================

print()
print("CLIENTES ATIVOS")
print("-" * 65)

ativos = cur.execute("""

SELECT

o.id,
l.company,
p.proposal_value

FROM pipeline p

JOIN opportunities o
ON o.id = p.opportunity_id

JOIN leads l
ON l.id = o.lead_id

WHERE p.status='CLIENTE_ATIVO'

""").fetchall()

for item in ativos:
    pass

    print(
        f"OP#{item[0]} | "
        f"{item[1]} | "
        f"R$ {item[2]:,.2f}"
    )

print()

conn.close()




