import sqlite3
import requests
import subprocess
import sys
import time

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

print("="*70)
print("PAYMENT MONITOR ENGINE")
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
    payment_link,
    payment_status

FROM pipeline

WHERE payment_status='AGUARDANDO_PAGAMENTO'

ORDER BY opportunity_id

""").fetchall()

print()
print(f"Pagamentos monitorados: {len(rows)}")
print()

for row in rows:

    op = row["opportunity_id"]

    print("-"*60)
    print(f"Opportunity : {op}")

    #
    # SimulaÃ§Ã£o de confirmaÃ§Ã£o.
    # No futuro este trecho consultarÃ¡ a API oficial do PayPal.
    #

    pagamento_confirmado = False

    try:

        r = requests.get(
            "http://127.0.0.1:5001/health",
            timeout=5
        )

        if r.status_code == 200:

            print("Servidor PayPal ONLINE")

        else:

            print("Servidor PayPal OFFLINE")
            continue

    except Exception as e:

        print(e)
        continue

    #
    # Troque esta variÃ¡vel quando integrar
    # a API oficial do PayPal.
    #

    if pagamento_confirmado:

        subprocess.run(

            [
                sys.executable,
                r"C:\IOTEC\CONFIRM_PAYMENT.py",
                str(op)
            ]

        )

        print("Pagamento confirmado.")

    else:

        print("Pagamento ainda pendente.")

print()
print("="*70)
print("FIM")
print("="*70)

conn.close()


