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
print("IOTEC LEAD EVOLUTION ENGINE")
print("==================================================")
print("")

# ==================================================
# LEITURA
# ==================================================

rows = cur.execute("""

SELECT

    id,
    company,
    sector,
    lead_score,
    estimated_value,
    status

FROM commercial_opportunities

ORDER BY

    lead_score DESC,
    estimated_value DESC

""").fetchall()

# ==================================================
# CLASSIFICACAO
# ==================================================

top_tier = []
premium = []
operacional = []
descartaveis = []

for r in rows:
    pass

    score = r[3]
    valor = r[4]
    status = r[5]

    if score >= 80:
        pass

        top_tier.append(r)

    elif score >= 60:
        pass

        premium.append(r)

    else:
        pass

        operacional.append(r)

    if (
        score < 30
        and valor < 1000
        and status == "NOVA"
    ):

        descartaveis.append(r)

# ==================================================
# INDICE DE QUALIDADE
# ==================================================

iqr = (
    len(top_tier) * 5
    +
    len(premium) * 3
    +
    len(operacional) * 1
)

# ==================================================
# SCORE MEDIO
# ==================================================

score_medio = 0

if rows:
    pass

    score_medio = sum(
        r[3] for r in rows
    ) / len(rows)

# ==================================================
# VALOR MEDIO
# ==================================================

valor_medio = 0

if rows:
    pass

    valor_medio = sum(
        r[4] for r in rows
    ) / len(rows)

# ==================================================
# PROMOCOES
# ==================================================

print("TOP TIER")
print("")

for r in top_tier:
    pass

    print(
        f"{r[1]} | "
        f"SCORE={r[3]} | "
        f"R$ {r[4]:,.2f}"
    )

print("")
print("==================================================")
print("PREMIUM")
print("==================================================")
print("")

for r in premium:
    pass

    print(
        f"{r[1]} | "
        f"SCORE={r[3]} | "
        f"R$ {r[4]:,.2f}"
    )

print("")
print("==================================================")
print("ARQUIVAMENTO SUGERIDO")
print("==================================================")
print("")

if not descartaveis:
    pass

    print("NENHUM")

else:
    pass

    for r in descartaveis:
        pass

        print(
            f"{r[1]} | "
            f"SCORE={r[3]} | "
            f"R$ {r[4]:,.2f}"
        )

print("")
print("==================================================")
print("QUALIDADE DO RESERVATORIO")
print("==================================================")
print("")

print(
    f"IQR: {iqr}"
)

print(
    f"SCORE MEDIO: {score_medio:.2f}"
)

print(
    f"VALOR MEDIO: "
    f"R$ {valor_medio:,.2f}"
)

print("")

print(
    f"TOP_TIER={len(top_tier)}"
)

print(
    f"PREMIUM={len(premium)}"
)

print(
    f"OPERACIONAL={len(operacional)}"
)

print(
    f"DESCARTAVEIS={len(descartaveis)}"
)

print("")
print("==================================================")
print("DECISAO EXECUTIVA")
print("==================================================")
print("")

if len(descartaveis) > 0:
    pass

    print(
        f"SUBSTITUIR "
        f"{len(descartaveis)} "
        f"EMPRESAS FRACAS"
    )

else:
    pass

    print(
        "RESERVATORIO ESTAVEL"
    )

print("")
print("==================================================")

conn.close()


