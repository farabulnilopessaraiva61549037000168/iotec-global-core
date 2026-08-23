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
print("IOTEC DAILY EXECUTION ENGINE")
print("==================================================")
print("")

# ==================================================
# RECEITA QUENTE
# ==================================================

receita_quente = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status IN (

    'NEGOCIACAO',
    'PAGAMENTO_PENDENTE'

)

""").fetchone()[0]

# ==================================================
# PIPELINE
# ==================================================

pipeline = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

""").fetchone()[0]

# ==================================================
# EMPRESAS
# ==================================================

empresas = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

# ==================================================
# DESCARTAVEIS
# ==================================================

descartaveis = cur.execute("""

SELECT

company

FROM commercial_opportunities

WHERE

lead_score < 30
AND estimated_value < 1000
AND status='NOVA'

""").fetchall()

# ==================================================
# TOP NEGOCIOS
# ==================================================

top = cur.execute("""

SELECT

company,
status,
estimated_value

FROM commercial_opportunities

ORDER BY estimated_value DESC

LIMIT 5

""").fetchall()

# ==================================================
# SETORES
# ==================================================

setores = cur.execute("""

SELECT

sector,
COUNT(*),
SUM(estimated_value)

FROM commercial_opportunities

GROUP BY sector

ORDER BY SUM(estimated_value) DESC

""").fetchall()

# ==================================================
# ACOES
# ==================================================

acoes = []

delta = cur.execute("""

SELECT company

FROM commercial_opportunities

WHERE status='PAGAMENTO_PENDENTE'

LIMIT 1

""").fetchone()

if delta:
    acoes.append(
        f"COBRAR PAGAMENTO: {delta[0]}"
    )

alfa = cur.execute("""

SELECT company

FROM commercial_opportunities

WHERE status='NEGOCIACAO'

LIMIT 1

""").fetchone()

if alfa:
    acoes.append(
        f"AGENDAR REUNIAO: {alfa[0]}"
    )

for d in descartaveis:
    pass

    acoes.append(
        f"SUBSTITUIR: {d[0]}"
    )

# ==================================================
# PAINEL
# ==================================================

print("META")
print(f"R$ {META:,.2f}")

print("")
print("RECEITA QUENTE")
print(f"R$ {receita_quente:,.2f}")

print("")
print("PIPELINE")
print(f"R$ {pipeline:,.2f}")

print("")
print("EMPRESAS")
print(empresas)

print("")
print("==================================================")
print("TOP NEGOCIOS")
print("==================================================")
print("")

for t in top:
    pass

    print(
        f"{t[0]} | "
        f"{t[1]} | "
        f"R$ {t[2]:,.2f}"
    )

print("")
print("==================================================")
print("SETORES")
print("==================================================")
print("")

for s in setores:
    pass

    print(
        f"{s[0]} | "
        f"{s[1]} empresas | "
        f"R$ {s[2]:,.2f}"
    )

print("")
print("==================================================")
print("ACAO DO DIA")
print("==================================================")
print("")

for i, acao in enumerate(acoes, start=1):
    pass

    print(
        f"{i}. {acao}"
    )

print("")

print("==================================================")
print("RESUMO EXECUTIVO")
print("==================================================")
print("")

print(
    f"DESCARTAVEIS: "
    f"{len(descartaveis)}"
)

print(
    f"GAP META: "
    f"R$ {max(0, META - receita_quente):,.2f}"
)

print("")

print("==================================================")

conn.close()




