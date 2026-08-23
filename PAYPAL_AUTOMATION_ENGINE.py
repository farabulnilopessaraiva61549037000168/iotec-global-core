import sqlite3
import requests
import subprocess
import sys
import time

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

print("="*70)
print("PAYPAL AUTOMATION ENGINE")
print("="*70)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

rows = cur.execute("""

SELECT
    opportunity_id,
    payment_reference,
    payment_status

FROM pipeline

WHERE payment_status='AGUARDANDO_PAGAMENTO'

ORDER BY opportunity_id

""").fetchall()

print()
print(f"Ordens monitoradas: {len(rows)}")
print()

confirmados = 0
pendentes = 0
erros = 0

for row in rows:

    op = row["opportunity_id"]
    order = row["payment_reference"]

    print("-"*60)
    print(f"Opportunity : {op}")

    if not order:

        print("Sem payment_reference.")
        erros += 1
        continue

    try:

        r = requests.get(
            f"http://127.0.0.1:5001/order-status/{order}",
            timeout=20
        )

        dados = r.json()

        status = dados.get("status","UNKNOWN")

        print(f"PayPal : {status}")

        if status == "COMPLETED":

            subprocess.run(
                [
                    sys.executable,
                    r"C:\IOTEC\CONFIRM_PAYMENT.py",
                    str(op)
                ]
            )

            confirmados += 1

        elif status in ("CREATED","APPROVED","PAYER_ACTION_REQUIRED"):

            pendentes += 1

        else:

            print("Status nÃ£o tratado:", status)

    except Exception as e:

        erros += 1
        print(e)

print()
print("="*70)
print("RESUMO")
print("="*70)
print(f"Confirmados : {confirmados}")
print(f"Pendentes   : {pendentes}")
print(f"Erros       : {erros}")

conn.close()


