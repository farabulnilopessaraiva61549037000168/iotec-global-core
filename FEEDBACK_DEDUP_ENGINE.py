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
print("===================================")
print("FEEDBACK DEDUP ENGINE")
print("===================================")
print("")

# ==========================================
# LOCALIZA DUPLICADOS
# ==========================================

duplicados = cur.execute("""

SELECT

    company,
    channel,
    result,
    COUNT(*) qtd

FROM communication_feedback

GROUP BY

    company,
    channel,
    result

HAVING COUNT(*) > 1

""").fetchall()

removidos = 0

for d in duplicados:
    pass

    empresa = d[0]
    canal = d[1]
    resultado = d[2]

    registros = cur.execute("""

    SELECT
        id

    FROM communication_feedback

    WHERE

        company=?
        AND channel=?
        AND result=?

    ORDER BY id DESC

    """,(

        empresa,
        canal,
        resultado

    )).fetchall()

    manter = registros[0][0]

    for r in registros[1:]:
        pass

        cur.execute("""

        DELETE FROM communication_feedback

        WHERE id=?

        """,(r[0],))

        removidos += 1

    print(
        f"MANTIDO={manter} | "
        f"{empresa} | "
        f"{resultado}"
    )

conn.commit()

total = cur.execute("""

SELECT COUNT(*)

FROM communication_feedback

""").fetchone()[0]

print("")
print("===================================")
print("RESUMO")
print("===================================")
print("")

print("GRUPOS DUPLICADOS:", len(duplicados))
print("REGISTROS REMOVIDOS:", removidos)
print("TOTAL FEEDBACKS:", total)

print("")
print("===================================")

conn.close()




