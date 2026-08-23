import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
import requests
import base64

DB = r"C:\IOTEC_OMEGA_X\backend\iotec.db"

CLIENT_ID = "COLOQUE_O_CLIENT_ID_AQUI"
CLIENT_SECRET = "COLOQUE_O_CLIENT_SECRET_AQUI"

BASE_URL = "https://api-m.sandbox.paypal.com"

def get_access_token():

    auth = base64.b64encode(
        f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r = requests.post(
        f"{BASE_URL}/v1/oauth2/token",
        headers=headers,
        data="grant_type=client_credentials"
    )

    r.raise_for_status()

    return r.json()["access_token"]


print("")
print("================================")
print("PAYPAL CONFIRM ENGINE")
print("================================")
print("")

print("ENGINE CRIADO.")
print("PRÃ"XIMA ETAPA: CONSULTAR ORDENS.")




