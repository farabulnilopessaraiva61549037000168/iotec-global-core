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
print("IOTEC MISSION CONTROL ENGINE")
print("==================================================")
print("")

# ==================================================
# RECEITAS
# ==================================================

pipeline = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

""").fetchone()[0]

receita_quente = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status IN (

'NEGOCIACAO',
'PAGAMENTO_PENDENTE'

)

""").fetchone()[0]

receita_provavel = 0

rows = cur.execute("""

SELECT

lead_score,
estimated_value

FROM commercial_opportunities

""").fetchall()

for score, valor in rows:
    pass

    receita_provavel += (
        valor * (score / 100)
    )

# ==================================================
# GAP
# ==================================================

gap = max(
    0,
    META - receita_quente
)

# ==================================================
# ALVOS DE FECHAMENTO
# ==================================================

alvos = cur.execute("""

SELECT

company,
status,
lead_score,
estimated_value

FROM commercial_opportunities

WHERE status IN (

'PAGAMENTO_PENDENTE',
'NEGOCIACAO',
'PROPOSTA_ENVIADA',
'EM_ANALISE'

)

ORDER BY

estimated_value DESC,
lead_score DESC

""").fetchall()

# ==================================================
# MISSAO
# ==================================================

acumulado = 0
missao = []

for a in alvos:
    pass

    if acumulado >= gap:
        break

    missao.append(a)

    acumulado += a[3]

# ==================================================
# PERCENTUAL META
# ==================================================

percentual_meta = 0

if META > 0:
    pass

    percentual_meta = (
        receita_quente / META
    ) * 100

# ==================================================
# PAINEL
# ==================================================

print("META")
print(f"R$ {META:,.2f}")

print("")
print("PIPELINE")
print(f"R$ {pipeline:,.2f}")

print("")
print("RECEITA QUENTE")
print(f"R$ {receita_quente:,.2f}")

print("")
print("RECEITA PROVAVEL")
print(f"R$ {receita_provavel:,.2f}")

print("")
print("META ATINGIDA")
print(f"{percentual_meta:.2f}%")

print("")
print("GAP")
print(f"R$ {gap:,.2f}")

print("")

print("==================================================")
print("MISSAO DE FECHAMENTO")
print("==================================================")
print("")

for i, m in enumerate(missao, start=1):
    pass

    print(
        f"{i}. "
        f"{m[0]} | "
        f"{m[1]} | "
        f"SCORE={m[2]} | "
        f"R$ {m[3]:,.2f}"
    )

print("")

print("RECEITA DA MISSAO")
print(f"R$ {acumulado:,.2f}")

print("")

print("==================================================")
print("DECISAO EXECUTIVA")
print("==================================================")
print("")

if acumulado >= gap:
    pass

    print(
        "MISSAO SUFICIENTE PARA BATER A META"
    )

else:
    pass

    print(
        "NECESSARIO GERAR NOVAS OPORTUNIDADES"
    )

print("")
print("==================================================")

conn.close()




