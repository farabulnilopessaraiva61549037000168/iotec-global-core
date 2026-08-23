import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# CONFIRM_INVOICE30.py
#
# Confirma pagamento da entrada (30%)
# Libera execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do projeto
# Ativa cobranÃƒÆ'Ã†â€™a final (70%)

import sqlite3
import sys
from datetime import datetime

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

if len(sys.argv) < 2:
    pass

    print("")
    print("USO:")
    print("python CONFIRM_INVOICE30.py 2")
    print("")
    exit()

op_id = int(sys.argv[1])

conn = sqlite3.connect(DB)
cur = conn.cursor()

registro = cur.execute("""

SELECT

invoice30_value,
invoice70_value

FROM pipeline

WHERE opportunity_id=?

""",(op_id,)).fetchone()

if not registro:
    pass

    print("OPORTUNIDADE NAO ENCONTRADA")
    conn.close()
    exit()

cur.execute("""

UPDATE pipeline

SET

invoice30_status='PAGA',

invoice70_status='AGUARDANDO',

status='PROJETO_LIBERADO',

updated_at=?

WHERE opportunity_id=?

""",(

datetime.now().strftime(
"%d/%m/%Y %H:%M:%S"
),

op_id

))

conn.commit()
conn.close()

print("")
print("======================================")
print("ENTRADA CONFIRMADA")
print("======================================")
print("")
print("OPPORTUNITY:", op_id)
print("")
print("STATUS: PROJETO_LIBERADO")
print("")
print("FATURA 70% ATIVADA")
print("")


