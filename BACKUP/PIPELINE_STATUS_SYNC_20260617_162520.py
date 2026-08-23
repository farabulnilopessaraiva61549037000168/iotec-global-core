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

sincronizados = 0

rows = cur.execute("""

SELECT

    company,
    status,
    pipeline_opportunity_id

FROM commercial_opportunities

WHERE pipeline_opportunity_id IS NOT NULL

""").fetchall()

for row in rows:
    pass

    empresa = row[0]
    status_comercial = row[1]
    pipeline_id = row[2]

    pipeline = cur.execute("""

    SELECT
        status

    FROM pipeline

    WHERE id=?

    """,(pipeline_id,)).fetchone()

    if not pipeline:
        continue

    status_pipeline = pipeline[0]

    if status_pipeline == status_comercial:
        continue

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

    sincronizados += 1

conn.commit()

print("")
print("===================================")
print("PIPELINE STATUS SYNC")
print("===================================")
print("")
print("REGISTROS ANALISADOS:", len(rows))
print("STATUS SINCRONIZADOS:", sincronizados)
print("")

print("DIVERGENCIAS CORRIGIDAS:")
print("")

for row in cur.execute("""

SELECT

    id,
    client_name,
    status

FROM pipeline

WHERE client_name IS NOT NULL
AND client_name <> ''

ORDER BY id

""").fetchall():

    print(row)

print("")

conn.close()


