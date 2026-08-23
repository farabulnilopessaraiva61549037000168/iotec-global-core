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

print("")
print("====================================================")
print("IOTEC SALES COMMAND CENTER")
print("====================================================")
print("")

# ====================================================
# RECEITA POTENCIAL
# ====================================================

receita = cur.execute("""

SELECT IFNULL(
    SUM(estimated_value),
    0
)

FROM commercial_opportunities

""").fetchone()[0]

# ====================================================
# RECEITA ESPERADA
# ====================================================

rows = cur.execute("""

SELECT

    company,
    lead_score,
    estimated_value,
    status

FROM commercial_opportunities

""").fetchall()

ranking = []

receita_esperada_total = 0

for row in rows:
    pass

    empresa = row[0]
    score = row[1]
    valor = row[2]
    status = row[3]

    chance = score

    if status == "NEGOCIACAO":
        chance += 30

    elif status == "PAGAMENTO_PENDENTE":
        chance += 40

    elif status == "PROPOSTA_ENVIADA":
        chance += 20

    elif status == "EM_ANALISE":
        chance += 10

    if chance > 100:
        chance = 100

    esperado = valor * (chance / 100)

    receita_esperada_total += esperado

    if status == "PAGAMENTO_PENDENTE":
        pass

        acao = "COBRAR PAGAMENTO"

    elif status == "NEGOCIACAO":
        pass

        acao = "AGENDAR REUNIAO"

    elif status == "PROPOSTA_ENVIADA":
        pass

        acao = "FOLLOW-UP"

    elif status == "EM_ANALISE":
        pass

        acao = "ENVIAR DIAGNOSTICO"

    else:
        pass

        acao = "QUALIFICAR"

    ranking.append(

        (
            empresa,
            chance,
            valor,
            esperado,
            status,
            acao
        )

    )

ranking.sort(
    key=lambda x: x[3],
    reverse=True
)

# ====================================================
# HEALTH CHECK
# ====================================================

sem_pipeline = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities

WHERE pipeline_opportunity_id IS NULL

""").fetchone()[0]

divergencias = cur.execute("""

SELECT COUNT(*)

FROM commercial_opportunities c

JOIN pipeline p
ON c.pipeline_opportunity_id = p.id

WHERE c.status <> p.status

""").fetchone()[0]

# ====================================================
# EXECUTIVE SUMMARY
# ====================================================

print("RECEITA POTENCIAL")
print(f"R$ {receita:,.2f}")
print("")

print("RECEITA ESPERADA")
print(f"R$ {receita_esperada_total:,.2f}")
print("")

print("OPORTUNIDADES SEM PIPELINE:", sem_pipeline)
print("")

print("DIVERGENCIAS:", divergencias)
print("")

print("====================================================")
print("TOP NEGOCIOS")
print("====================================================")
print("")

for item in ranking[:10]:
    pass

    print(
        f"{item[0]} | "
        f"CHANCE={item[1]}% | "
        f"ESPERADO=R$ {item[3]:,.2f} | "
        f"{item[4]} | "
        f"{item[5]}"
    )

print("")
print("====================================================")

conn.close()




