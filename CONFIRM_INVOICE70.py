import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# CONFIRM_INVOICE70.py
#
# Confirma pagamento final
# Converte projeto em cliente ativo

import sqlite3
import sys
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

if len(sys.argv) < 2:
    pass

    print("")
    print("USO:")
    print("python CONFIRM_INVOICE70.py 2")
    print("")
    exit()

op_id = int(sys.argv[1])

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

UPDATE pipeline

SET

invoice70_status='PAGA',

payment_status='PAGAMENTO_RECEBIDO',

payment_received=1,

status='CLIENTE_ATIVO',

payment_date=?,

updated_at=?

WHERE opportunity_id=?

""",(

datetime.now().strftime(
"%d/%m/%Y %H:%M:%S"
),

datetime.now().strftime(
"%d/%m/%Y %H:%M:%S"
),

op_id

))

conn.commit()
conn.close()

print("")
print("======================================")
print("PAGAMENTO FINAL CONFIRMADO")
print("======================================")
print("")
print("OPPORTUNITY:", op_id)
print("")
print("STATUS: CLIENTE_ATIVO")
print("")
print("RECEITA REALIZADA")
print("")




