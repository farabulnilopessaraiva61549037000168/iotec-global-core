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
print("COMMERCIAL HEALTH CHECK")
print("===================================")
print("")

# ==================================================
# OPORTUNIDADES SEM PIPELINE
# ==================================================

sem_pipeline = cur.execute("""

SELECT
id,
company,
status

FROM commercial_opportunities

WHERE pipeline_opportunity_id IS NULL

""").fetchall()

print("OPORTUNIDADES SEM PIPELINE:", len(sem_pipeline))

for r in sem_pipeline:
    print(r)

print("")

# ==================================================
# PIPELINE SEM CLIENTE
# ==================================================

pipeline_sem_cliente = cur.execute("""

SELECT
id,
status,
proposal_value

FROM pipeline

WHERE client_name IS NULL
OR client_name=''

""").fetchall()

print("PIPELINE SEM CLIENTE:", len(pipeline_sem_cliente))

for r in pipeline_sem_cliente:
    print(r)

print("")

# ==================================================
# DIVERGENCIA DE STATUS
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

print("DIVERGENCIAS DE STATUS:", len(divergencias))

for r in divergencias:
    print(r)

print("")

# ==================================================
# VALORES ZERADOS
# ==================================================

zerados = cur.execute("""

SELECT
id,
company

FROM commercial_opportunities

WHERE estimated_value <= 0

""").fetchall()

print("VALORES ZERADOS:", len(zerados))

for r in zerados:
    print(r)

print("")

# ==================================================
# PROPOSTAS SEM ARQUIVO
# ==================================================

propostas = cur.execute("""

SELECT
company

FROM commercial_opportunities

WHERE status='PROPOSTA_ENVIADA'

""").fetchall()

print("PROPOSTAS ENVIADAS:", len(propostas))

for r in propostas:
    print(r[0])

print("")

# ==================================================
# RESUMO
# ==================================================

problemas = (
    len(sem_pipeline)
    + len(pipeline_sem_cliente)
    + len(divergencias)
    + len(zerados)
)

print("===================================")
print("RESUMO")
print("===================================")
print("")

print("TOTAL DE PROBLEMAS:", problemas)

if problemas == 0:
    print("STATUS GERAL: OK")
else:
    print("STATUS GERAL: ATENCAO")

print("")

conn.close()


