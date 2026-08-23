import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import requests
from datetime import datetime

print("")
print("===================================")
print("IOTEC API TEST")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

API_URL = input(
    "\nURL DA API RENDER: "
).strip()

payload = {

    "nome": "TESTE IOTEC",

    "empresa": "EMPRESA TESTE",

    "email": "teste@iotec.local",

    "whatsapp": "88999999999",

    "problema":
    "TESTE DE INTEGRACAO",

    "origem":
    "IOTEC_API_TEST"
}

print("")
print("ENVIANDO TESTE...")

try:
    pass

    resposta = requests.post(

        API_URL,

        json=payload,

        timeout=30
    )

    print("")
    print("STATUS HTTP:")
    print(resposta.status_code)

    print("")
    print("RESPOSTA:")

    try:
        print(
            resposta.json()
        )

    except:
        print(
            resposta.text
        )

    print("")
    print("TESTE FINALIZADO")

except Exception as erro:
    pass

    print("")
    print("FALHA:")
    print(str(erro))




