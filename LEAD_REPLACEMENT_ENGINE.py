import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

SCORE_MINIMO = 70
VALOR_MINIMO = 5000

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("==================================================")
print("IOTEC LEAD REPLACEMENT ENGINE")
print("==================================================")
print("")

# ==================================================
# DESCARTAVEIS
# ==================================================

descartaveis = cur.execute("""

SELECT

    id,
    company,
    sector,
    lead_score,
    estimated_value,
    status

FROM commercial_opportunities

WHERE

    lead_score < 30

    AND estimated_value < 1000

    AND status='NOVA'

ORDER BY lead_score

""").fetchall()

# ==================================================
# POTENCIAL PERDIDO
# ==================================================

potencial_liberado = sum(
    x[4] for x in descartaveis
)

# ==================================================
# MELHORES EMPRESAS
# ==================================================

fortes = cur.execute("""

SELECT

    company,
    sector,
    lead_score,
    estimated_value,
    status

FROM commercial_opportunities

WHERE

    lead_score >= ?

    AND estimated_value >= ?

ORDER BY

    lead_score DESC,
    estimated_value DESC

""",(

    SCORE_MINIMO,
    VALOR_MINIMO

)).fetchall()

# ==================================================
# SETORES
# ==================================================

setores = {}

for f in fortes:
    pass

    setor = f[1]

    setores[setor] = (
        setores.get(setor, 0) + 1
    )

# ==================================================
# PAINEL
# ==================================================

print("EMPRESAS FRACAS")
print("")

if not descartaveis:
    pass

    print("NENHUMA")

else:
    pass

    for d in descartaveis:
        pass

        print(
            f"{d[1]} | "
            f"SCORE={d[3]} | "
            f"R$ {d[4]:,.2f}"
        )

print("")
print("==================================================")
print("VAGAS LIBERAVEIS")
print("==================================================")
print("")

print(len(descartaveis))

print("")
print("POTENCIAL LIBERADO")
print(
    f"R$ {potencial_liberado:,.2f}"
)

print("")

print("==================================================")
print("EMPRESAS FORTES")
print("==================================================")
print("")

for f in fortes[:10]:
    pass

    print(
        f"{f[0]} | "
        f"{f[1]} | "
        f"SCORE={f[2]} | "
        f"R$ {f[3]:,.2f}"
    )

print("")

print("==================================================")
print("SETORES VENCEDORES")
print("==================================================")
print("")

for setor, qtd in sorted(

    setores.items(),

    key=lambda x: x[1],

    reverse=True

):

    print(
        f"{setor} | "
        f"{qtd} empresas"
    )

print("")

print("==================================================")
print("ORDEM EXECUTIVA")
print("==================================================")
print("")

if len(descartaveis) > 0:
    pass

    print(
        f"SUBSTITUIR "
        f"{len(descartaveis)} "
        f"EMPRESAS"
    )

    print(
        f"SCORE MINIMO: "
        f"{SCORE_MINIMO}"
    )

    print(
        f"VALOR MINIMO: "
        f"R$ {VALOR_MINIMO:,.2f}"
    )

else:
    pass

    print(
        "SEM SUBSTITUICOES"
    )

print("")
print("==================================================")

conn.close()




