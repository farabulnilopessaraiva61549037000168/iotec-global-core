import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

print("")
print("===================================")
print("COMMUNICATION GUARDIAN")
print("===================================")
print("")

alertas = 0

# ==================================================
# FEEDBACKS DUPLICADOS
# ==================================================

duplicados = cur.execute("""

SELECT
company,
result,
COUNT(*)

FROM communication_feedback

GROUP BY company,result

HAVING COUNT(*) > 1

""").fetchall()

print("FEEDBACKS DUPLICADOS:", len(duplicados))

for d in duplicados:
    pass

    print(
        f"{d[0]} | {d[1]} | REPETICOES={d[2]}"
    )

    alertas += 1

print("")

# ==================================================
# OPORTUNIDADES SEM PIPELINE
# ==================================================

sem_pipeline = cur.execute("""

SELECT
company,
status

FROM commercial_opportunities

WHERE pipeline_opportunity_id IS NULL

""").fetchall()

print("SEM PIPELINE:", len(sem_pipeline))

for r in sem_pipeline:
    pass

    print(
        f"{r[0]} | {r[1]}"
    )

    alertas += 1

print("")

# ==================================================
# DIVERGENCIAS
# ==================================================

divergencias = cur.execute("""

SELECT

c.company,
c.status,
p.status

FROM commercial_opportunities c

JOIN pipeline p
ON c.pipeline_opportunity_id = p.id

WHERE c.status <> p.status

""").fetchall()

print("DIVERGENCIAS:", len(divergencias))

for d in divergencias:
    pass

    print(
        f"{d[0]} | COMERCIAL={d[1]} | PIPELINE={d[2]}"
    )

    alertas += 1

print("")

# ==================================================
# PAGAMENTO PENDENTE
# ==================================================

pendentes = cur.execute("""

SELECT
company,
estimated_value

FROM commercial_opportunities

WHERE status='PAGAMENTO_PENDENTE'

""").fetchall()

print("PAGAMENTOS PENDENTES:", len(pendentes))

for p in pendentes:
    pass

    print(
        f"{p[0]} | R$ {p[1]:,.2f}"
    )

print("")

# ==================================================
# NEGOCIACOES ABERTAS
# ==================================================

negociacoes = cur.execute("""

SELECT
company,
estimated_value

FROM commercial_opportunities

WHERE status='NEGOCIACAO'

""").fetchall()

print("NEGOCIACOES ABERTAS:", len(negociacoes))

for n in negociacoes:
    pass

    print(
        f"{n[0]} | R$ {n[1]:,.2f}"
    )

print("")

# ==================================================
# RECEITA EM RISCO
# ==================================================

receita_risco = 0

for p in pendentes:
    receita_risco += p[1]

for n in negociacoes:
    receita_risco += n[1]

print("RECEITA EM RISCO:")
print(f"R$ {receita_risco:,.2f}")
print("")

# ==================================================
# RESUMO
# ==================================================

print("===================================")
print("RESUMO EXECUTIVO")
print("===================================")
print("")

print("ALERTAS:", alertas)

if alertas == 0:
    pass

    print("STATUS GERAL: OK")

elif alertas <= 5:
    pass

    print("STATUS GERAL: ATENCAO")

else:
    pass

    print("STATUS GERAL: CRITICO")

print("")
print("===================================")

conn.close()


