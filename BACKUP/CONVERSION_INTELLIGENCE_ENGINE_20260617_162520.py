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
print("==================================================")
print("IOTEC CONVERSION INTELLIGENCE ENGINE")
print("==================================================")
print("")

# ==================================================
# SETORES
# ==================================================

print("ANALISE POR SETOR")
print("")

setores = cur.execute("""

SELECT

    sector,
    COUNT(*),
    IFNULL(SUM(estimated_value),0)

FROM commercial_opportunities

GROUP BY sector

ORDER BY 3 DESC

""").fetchall()

melhor_setor = None
melhor_valor = 0

for setor, qtd, valor in setores:
    pass

    clientes = cur.execute("""

    SELECT COUNT(*)

    FROM commercial_opportunities

    WHERE sector=?
    AND status='CLIENTE_ATIVO'

    """,(setor,)).fetchone()[0]

    conversao = 0

    if qtd > 0:
        pass

        conversao = (
            clientes * 100
        ) / qtd

    print(
        f"{setor} | "
        f"EMPRESAS={qtd} | "
        f"VALOR=R$ {valor:,.2f} | "
        f"CONVERSAO={conversao:.2f}%"
    )

    if valor > melhor_valor:
        pass

        melhor_valor = valor
        melhor_setor = setor

# ==================================================
# ORIGENS
# ==================================================

print("")
print("==================================================")
print("ORIGENS")
print("==================================================")
print("")

origens = cur.execute("""

SELECT

    source,
    COUNT(*)

FROM lead_sources

GROUP BY source

ORDER BY 2 DESC

""").fetchall()

for origem, qtd in origens:
    pass

    print(
        f"{origem} | "
        f"LEADS={qtd}"
    )

# ==================================================
# TICKET MEDIO
# ==================================================

print("")
print("==================================================")
print("TICKET MEDIO")
print("==================================================")
print("")

ticket = cur.execute("""

SELECT AVG(
estimated_value
)

FROM commercial_opportunities

""").fetchone()[0]

ticket = ticket or 0

print(
    f"TICKET MEDIO: "
    f"R$ {ticket:,.2f}"
)

# ==================================================
# TOP OPORTUNIDADES
# ==================================================

print("")
print("==================================================")
print("TOP OPORTUNIDADES")
print("==================================================")
print("")

tops = cur.execute("""

SELECT

    company,
    sector,
    estimated_value,
    status

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY estimated_value DESC

LIMIT 10

""").fetchall()

for t in tops:
    pass

    print(
        f"{t[0]} | "
        f"{t[1]} | "
        f"R$ {t[2]:,.2f} | "
        f"{t[3]}"
    )

# ==================================================
# INTELIGENCIA
# ==================================================

print("")
print("==================================================")
print("INTELIGENCIA")
print("==================================================")
print("")

print(
    f"SETOR MAIS VALIOSO: "
    f"{melhor_setor}"
)

print(
    f"POTENCIAL: "
    f"R$ {melhor_valor:,.2f}"
)

print("")

if melhor_setor:
    pass

    print(
        f"RECOMENDACAO:"
    )

    print(
        f"AUMENTAR CAPTACAO "
        f"NO SETOR {melhor_setor.upper()}"
    )

print("")
print("==================================================")
print("RESUMO EXECUTIVO")
print("==================================================")
print("")

pipeline = cur.execute("""

SELECT IFNULL(
SUM(estimated_value),0
)

FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

""").fetchone()[0]

clientes = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE status='CLIENTE_ATIVO'

""").fetchone()[0]

print(
    f"PIPELINE: "
    f"R$ {pipeline:,.2f}"
)

print(
    f"CLIENTES: "
    f"{clientes}"
)

print(
    f"SETOR PRIORITARIO: "
    f"{melhor_setor}"
)

print("")
print("==================================================")

conn.close()


