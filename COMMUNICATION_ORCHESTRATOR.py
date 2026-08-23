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

# ==================================================
# HISTÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRICO
# ==================================================

cur.execute("""

CREATE TABLE IF NOT EXISTS communication_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    queue_id INTEGER,

    company TEXT,

    objective TEXT,

    priority TEXT,

    executed_at TEXT,

    result TEXT

)

""")

conn.commit()

print("")
print("===================================")
print("COMMUNICATION ORCHESTRATOR")
print("===================================")
print("")

# ==================================================
# FILA
# ==================================================

fila = cur.execute("""

SELECT

    id,
    company,
    objective,
    priority,
    status

FROM communication_queue

WHERE status='PENDENTE'

ORDER BY

CASE priority
    WHEN 'CRITICA' THEN 1
    WHEN 'ALTA' THEN 2
    WHEN 'MEDIA' THEN 3
    ELSE 4
END

""").fetchall()

processadas = 0

for item in fila:
    pass

    queue_id = item[0]
    empresa = item[1]
    objetivo = item[2]
    prioridade = item[3]

    # marca execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o

    cur.execute("""

    UPDATE communication_queue

    SET status='PROCESSADA'

    WHERE id=?

    """,(queue_id,))

    # histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico

    cur.execute("""

    INSERT INTO communication_history(

        queue_id,
        company,
        objective,
        priority,
        executed_at,
        result

    )

    VALUES(?,?,?,?,?,?)

    """,(

        queue_id,
        empresa,
        objetivo,
        prioridade,
        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "EXECUTADA"

    ))

    processadas += 1

conn.commit()

pendentes = cur.execute("""

SELECT COUNT(*)

FROM communication_queue

WHERE status='PENDENTE'

""").fetchone()[0]

historico = cur.execute("""

SELECT COUNT(*)

FROM communication_history

""").fetchone()[0]

print("PROCESSADAS:", processadas)
print("PENDENTES:", pendentes)
print("HISTORICO:", historico)

print("")
print("ULTIMAS EXECUCOES")
print("")

for row in cur.execute("""

SELECT

    company,
    priority,
    objective,
    executed_at

FROM communication_history

ORDER BY id DESC

LIMIT 10

""").fetchall():

    print(row)

print("")
print("===================================")

conn.close()




