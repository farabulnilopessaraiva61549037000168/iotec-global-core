import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

CAPACIDADE = 1000

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC LEAD SUPPLY CHAIN ENGINE")
print("==================================================")
print("")

# ==================================================
# ESTATISTICAS
# ==================================================

total = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

""").fetchone()[0]

ocupacao = (total / CAPACIDADE) * 100

# ==================================================
# RANKING INTERNO
# ==================================================

ranking = cur.execute("""

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
# TIERS
# ==================================================

top_tier = []
premium = []
operacional = []

for r in ranking:
    pass

    score = r[3]
    valor = r[4]

    if score >= 80:
        pass

        top_tier.append(r)

    elif score >= 60:
        pass

        premium.append(r)

    else:
        pass

        operacional.append(r)

# ==================================================
# RISCO DE DESCARTE
# ==================================================

descartaveis = []

for r in ranking:
    pass

    score = r[3]
    valor = r[4]
    status = r[5]

    if (
        score < 30 and
        valor < 1000 and
        status == "NOVA"
    ):
        descartaveis.append(r)

# ==================================================
# PAINEL
# ==================================================

print("CAPACIDADE")
print(CAPACIDADE)

print("")
print("EMPRESAS")
print(total)

print("")
print(f"OCUPACAO: {ocupacao:.2f}%")

print("")
print("==================================================")
print("TIERS")
print("==================================================")
print("")

print("TOP_TIER:", len(top_tier))
print("PREMIUM:", len(premium))
print("OPERACIONAL:", len(operacional))

print("")
print("==================================================")
print("TOP 10 PRIORIDADES")
print("==================================================")
print("")

for r in ranking[:10]:
    pass

    print(
        f"{r[1]} | "
        f"SCORE={r[3]} | "
        f"R$ {r[4]:,.2f} | "
        f"{r[5]}"
    )

print("")
print("==================================================")
print("DESCARTAVEIS")
print("==================================================")
print("")

if not descartaveis:
    pass

    print("NENHUMA EMPRESA MARCADA")

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
print("RESUMO")
print("==================================================")
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

conn.close()




