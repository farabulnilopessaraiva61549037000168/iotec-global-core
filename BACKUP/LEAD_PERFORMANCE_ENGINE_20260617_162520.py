import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("===================================")
print("LEAD PERFORMANCE ENGINE")
print("===================================")
print("")

# ==========================================
# ORIGENS
# ==========================================

fontes = cur.execute("""

SELECT DISTINCT source

FROM lead_sources

ORDER BY source

""").fetchall()

if not fontes:
    pass

    print("NENHUMA ORIGEM REGISTRADA")
    print("")
    conn.close()
    raise SystemExit

ranking = []

for fonte_row in fontes:
    pass

    fonte = fonte_row[0]

    leads = cur.execute("""

    SELECT COUNT(*)

    FROM lead_sources

    WHERE source=?

    """,(fonte,)).fetchone()[0]

    valor_total = cur.execute("""

    SELECT IFNULL(SUM(estimated_value),0)

    FROM lead_sources

    WHERE source=?

    """,(fonte,)).fetchone()[0]

    clientes = cur.execute("""

    SELECT COUNT(*)

    FROM lead_sources

    WHERE source=?
    AND status='CLIENTE_ATIVO'

    """,(fonte,)).fetchone()[0]

    negociacao = cur.execute("""

    SELECT COUNT(*)

    FROM lead_sources

    WHERE source=?
    AND status='NEGOCIACAO'

    """,(fonte,)).fetchone()[0]

    pagamento = cur.execute("""

    SELECT COUNT(*)

    FROM lead_sources

    WHERE source=?
    AND status='PAGAMENTO_PENDENTE'

    """,(fonte,)).fetchone()[0]

    conversao = 0

    if leads > 0:
        conversao = (clientes / leads) * 100

    ranking.append(

        (
            fonte,
            leads,
            clientes,
            negociacao,
            pagamento,
            valor_total,
            conversao
        )

    )

ranking.sort(
    key=lambda x: x[5],
    reverse=True
)

# ==========================================
# RELATORIO
# ==========================================

print("RANKING DE PERFORMANCE")
print("")

for r in ranking:
    pass

    print(
        f"{r[0]} | "
        f"LEADS={r[1]} | "
        f"CLIENTES={r[2]} | "
        f"NEGOCIACAO={r[3]} | "
        f"PAGAMENTO={r[4]} | "
        f"VALOR=R$ {r[5]:,.2f} | "
        f"CONVERSAO={r[6]:.2f}%"
    )

print("")
print("===================================")
print("MELHOR ORIGEM")
print("===================================")
print("")

if ranking:
    pass

    melhor = ranking[0]

    print(
        f"{melhor[0]} | "
        f"VALOR=R$ {melhor[5]:,.2f}"
    )

print("")
print("===================================")

conn.close()


