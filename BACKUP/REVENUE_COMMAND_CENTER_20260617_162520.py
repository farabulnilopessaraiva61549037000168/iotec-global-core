import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

META = 50000

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("==================================================")
print("IOTEC REVENUE COMMAND CENTER")
print("==================================================")
print("")

pipeline = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

""").fetchone()[0]

empresas = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

negociacao = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status='NEGOCIACAO'

""").fetchone()[0]

pagamento = cur.execute("""

SELECT IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

WHERE status='PAGAMENTO_PENDENTE'

""").fetchone()[0]

receita_quente = negociacao + pagamento

# ==========================================
# TOP 5 OPORTUNIDADES
# ==========================================

top = cur.execute("""

SELECT

company,
status,
estimated_value

FROM commercial_opportunities

ORDER BY estimated_value DESC

LIMIT 5

""").fetchall()

# ==========================================
# ORIGENS
# ==========================================

try:
    pass

    fontes = cur.execute("""

    SELECT

        source,
        COUNT(*),
        IFNULL(SUM(estimated_value),0)

    FROM lead_sources

    GROUP BY source

    ORDER BY 3 DESC

    LIMIT 5

    """).fetchall()

except:
    pass

    fontes = []

# ==========================================
# PAINEL
# ==========================================

print("META")
print(f"R$ {META:,.2f}")
print("")

print("PIPELINE")
print(f"R$ {pipeline:,.2f}")
print("")

print("RECEITA QUENTE")
print(f"R$ {receita_quente:,.2f}")
print("")

print("EMPRESAS")
print(empresas)
print("")

print("GAP")
print(f"R$ {max(0, META - receita_quente):,.2f}")
print("")

print("==================================================")
print("TOP OPORTUNIDADES")
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
print("ORIGENS")
print("==================================================")
print("")

for f in fontes:
    pass

    print(
        f"{f[0]} | "
        f"LEADS={f[1]} | "
        f"R$ {f[2]:,.2f}"
    )

print("")
print("==================================================")

conn.close()


