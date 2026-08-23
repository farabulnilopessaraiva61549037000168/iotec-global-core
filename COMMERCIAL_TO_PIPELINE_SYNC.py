import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import time
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

oportunidades = cur.execute("""

SELECT

    id,
    company,
    estimated_value,
    status,
    pipeline_opportunity_id

FROM commercial_opportunities

WHERE status IN (

    'PROPOSTA_ENVIADA',
    'NEGOCIACAO',
    'PAGAMENTO_PENDENTE',
    'CLIENTE_ATIVO'

)

""").fetchall()

sincronizadas = 0

for op in oportunidades:
    pass

    op_id = op[0]
    empresa = op[1]
    valor = op[2]
    status = op[3]
    pipeline_id = op[4]

    if pipeline_id:
        continue

    existe = cur.execute("""

    SELECT id

    FROM pipeline

    WHERE client_name=?

    """,(empresa,)).fetchone()

    if existe:
        pass

        cur.execute("""

        UPDATE commercial_opportunities

        SET pipeline_opportunity_id=?

        WHERE id=?

        """,(

            existe[0],
            op_id

        ))

        sincronizadas += 1
        continue

    novo_opportunity_id = int(time.time()) + op_id

    cur.execute("""

    INSERT INTO pipeline(

        opportunity_id,
        status,
        report_sent,
        meeting_scheduled,
        proposal_sent,
        proposal_value,
        payment_received,
        observations,
        updated_at,
        client_name,
        phone,
        approved

    )

    VALUES(

        ?,?,?,?,?,?,?,?,?,?,?,?

    )

    """,(

        novo_opportunity_id,
        status,
        0,
        0,
        1,
        valor,
        0,
        "CRIADO PELO COMMERCIAL SYNC",
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        empresa,
        "",
        0

    ))

    pipeline_row_id = cur.lastrowid

    cur.execute("""

    UPDATE commercial_opportunities

    SET pipeline_opportunity_id=?

    WHERE id=?

    """,(

        pipeline_row_id,
        op_id

    ))

    sincronizadas += 1

conn.commit()

print("")
print("===================================")
print("COMMERCIAL TO PIPELINE SYNC")
print("===================================")
print("")
print("SINCRONIZADAS:", sincronizadas)
print("")

total_pipeline = cur.execute("""

SELECT COUNT(*)

FROM pipeline

""").fetchone()[0]

print("TOTAL PIPELINE:", total_pipeline)
print("")

conn.close()




