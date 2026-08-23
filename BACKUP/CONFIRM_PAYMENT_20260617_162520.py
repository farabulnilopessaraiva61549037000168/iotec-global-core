import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import sys
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

if len(sys.argv) < 2:
    pass

    print("")
    print("USO:")
    print("python CONFIRM_PAYMENT.py 1")
    print("")
    exit()

op_id = int(sys.argv[1])

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""

UPDATE pipeline

SET

payment_status='PAGAMENTO_RECEBIDO',
payment_date=?,
status='CLIENTE_ATIVO',
payment_received=1,
updated_at=?

WHERE opportunity_id=?

""",(

datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
op_id

))

conn.commit()
conn.close()

print("")
print("==============================")
print("PAGAMENTO CONFIRMADO")
print("==============================")
print("OPPORTUNITY:", op_id)
print("")


