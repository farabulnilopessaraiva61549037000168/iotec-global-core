import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import requests

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

PAYPAL_SERVER = "http://127.0.0.1:5001/criar-pagamento"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

pendentes = cur.execute("""

SELECT
    opportunity_id,
    proposal_value

FROM pipeline

WHERE status='PAGAMENTO_PENDENTE'

""").fetchall()

print("")
print("================================")
print("PAYMENT ENGINE")
print("================================")
print("")

gerados = 0
falhas = 0

for op_id, valor in pendentes:

    try:

        resposta = requests.get(PAYPAL_SERVER, timeout=30)

        if resposta.status_code != 200:
            raise Exception(f"HTTP {resposta.status_code}")

        dados = resposta.json()

        payment_link = dados.get("url")

        if not payment_link:
            raise Exception("URL de pagamento nÃƒÂ£o retornada.")

        cur.execute("""

        UPDATE pipeline

        SET

            payment_provider=?,
            payment_link=?,
            payment_status='AGUARDANDO_PAGAMENTO'

        WHERE opportunity_id=?

        """, (

            "PAYPAL",
            payment_link,
            op_id

        ))

        gerados += 1

        print(f"[OK] Oportunidade {op_id}")
        print(payment_link)
        print()

    except Exception as erro:

        falhas += 1

        print(f"[ERRO] {op_id}")
        print(erro)
        print()

conn.commit()
conn.close()

print("================================")
print("RESUMO")
print("================================")
print(f"Links gerados : {gerados}")
print(f"Falhas        : {falhas}")
print("")



