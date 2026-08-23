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

pendentes = cur.execute("""

SELECT
opportunity_id,
proposal_value

FROM pipeline

WHERE status='PAGAMENTO_PENDENTE'

""").fetchall()

for op_id,valor in pendentes:
    pass

    link = f"PAYMENT://OPPORTUNITY/{op_id}"

    cur.execute("""

    UPDATE pipeline

    SET

    payment_provider='PAYPAL',
    payment_link=?,
    payment_status='AGUARDANDO_PAGAMENTO'

    WHERE opportunity_id=?

    """,(

        link,
        op_id

    ))

conn.commit()
conn.close()

print("")
print("================================")
print("PAYMENT ENGINE")
print("================================")
print("")
print("PAGAMENTOS GERADOS:", len(pendentes))
print("")


