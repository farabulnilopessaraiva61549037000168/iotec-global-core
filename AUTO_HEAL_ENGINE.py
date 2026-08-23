import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

print("")
print("===================================")
print("AUTO HEAL ENGINE")
print("===================================")
print("")

corrigidos = 0

# ==================================================
# 1 - SINCRONIZAR STATUS
# ==================================================

divergencias = cur.execute("""

SELECT

    c.id,
    c.company,
    c.status,
    c.pipeline_opportunity_id,
    p.status

FROM commercial_opportunities c

JOIN pipeline p
ON c.pipeline_opportunity_id = p.id

WHERE c.status <> p.status

""").fetchall()

print("DIVERGENCIAS ENCONTRADAS:", len(divergencias))
print("")

for d in divergencias:
    pass

    comercial_id = d[0]
    empresa = d[1]
    status_comercial = d[2]
    pipeline_id = d[3]
    status_pipeline = d[4]

    cur.execute("""

    UPDATE pipeline

    SET

        status=?,
        updated_at=?

    WHERE id=?

    """,(

        status_comercial,
        datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        ),
        pipeline_id

    ))

    corrigidos += 1

    print(
        f"SYNC: {empresa}"
        f" | PIPELINE {status_pipeline}"
        f" -> {status_comercial}"
    )

print("")

# ==================================================
# 2 - FEEDBACK DUPLICADO
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

print("DUPLICADOS ENCONTRADOS:", len(duplicados))
print("")

for d in duplicados:
    pass

    print(
        f"{d[0]} | {d[1]} | {d[2]} registros"
    )

print("")

# ==================================================
# 3 - OPORTUNIDADES SEM PIPELINE
# ==================================================

sem_pipeline = cur.execute("""

SELECT
company,
status

FROM commercial_opportunities

WHERE pipeline_opportunity_id IS NULL

""").fetchall()

print("SEM PIPELINE:", len(sem_pipeline))

for s in sem_pipeline:
    pass

    print(
        f"{s[0]} | {s[1]}"
    )

print("")

# ==================================================
# 4 - RESUMO
# ==================================================

conn.commit()

print("===================================")
print("AUTO HEAL RESUMO")
print("===================================")
print("")

print("CORRECOES:", corrigidos)
print("DUPLICADOS:", len(duplicados))
print("SEM PIPELINE:", len(sem_pipeline))

print("")

if corrigidos == 0:
    print("NUCLEO ESTAVEL")
else:
    print("NUCLEO CORRIGIDO")

print("")
print("===================================")

conn.close()




