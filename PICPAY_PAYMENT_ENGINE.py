import requests
import json
import sqlite3

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

# CONFIGURE COM AS CREDENCIAIS REAIS DO PICPAY
PICPAY_TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

URL = "https://appws.picpay.com/ecommerce/public/payments"

payload = {
    "referenceId": "IOTEC-HOMOLOGACAO-001",
    "callbackUrl": "https://SEU_DOMINIO/callback/picpay",
    "returnUrl": "https://SEU_DOMINIO/sucesso",
    "value": 29.90,
    "expiresAt": "2030-12-31T23:59:59-03:00",
    "buyer": {
        "firstName": "PRESIDENCIA",
        "lastName": "IOTEC",
        "email": "presidencia@iotec.local",
        "phone": "+5588999999999"
    }
}

headers = {
    "x-picpay-token": PICPAY_TOKEN,
    "Content-Type": "application/json"
}

print("="*60)
print("IOTEC PICPAY ENGINE")
print("="*60)

try:

    r = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    print(r.status_code)

    data = r.json()

    print(json.dumps(data, indent=4, ensure_ascii=False))

    payment_url = (
        data.get("paymentUrl")
        or data.get("charge", {}).get("url")
    )

    if payment_url:

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

        cur.execute("""

        INSERT INTO pipeline(

            opportunity_id,
            status,
            payment_provider,
            payment_link,
            payment_status

        )

        VALUES(?,?,?,?,?)

        """,(

            999999999,

            "PAGAMENTO_PENDENTE",

            "PICPAY",

            payment_url,

            "AGUARDANDO_PAGAMENTO"

        ))

        conn.commit()
        conn.close()

        print()
        print("="*60)
        print("LINK GERADO")
        print("="*60)
        print(payment_url)

except Exception as e:

    print(e)

