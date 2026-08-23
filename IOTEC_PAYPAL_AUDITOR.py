import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import base64
import importlib.util
import requests
import traceback
from pathlib import Path

ARQUIVO = Path(r"C:\IOTEC\paypal_server.py")

print("=" * 70)
print("IOTEC PAYPAL AUDITOR")
print("=" * 70)

# ---------------------------------------------------
# Carrega paypal_server.py sem alterar o arquivo
# ---------------------------------------------------

spec = importlib.util.spec_from_file_location("paypal_server", ARQUIVO)
paypal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paypal)

print("\nCONFIGURAÃƒâ€¡ÃƒÆ'O ENCONTRADA\n")

print("BASE_URL :", paypal.BASE_URL)
print("CLIENT_ID informado :", "SIM" if paypal.CLIENT_ID != "COLOQUE_AQUI" else "NÃƒÆ'O")
print("CLIENT_SECRET informado :", "SIM" if paypal.CLIENT_SECRET != "COLOQUE_AQUI" else "NÃƒÆ'O")

print("\nTESTANDO AUTENTICAÃƒâ€¡ÃƒÆ'O...\n")

try:

    auth = base64.b64encode(
        f"{paypal.CLIENT_ID}:{paypal.CLIENT_SECRET}".encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Accept-Language": "en_US"
    }

    response = requests.post(
        f"{paypal.BASE_URL}/v1/oauth2/token",
        headers=headers,
        data={"grant_type": "client_credentials"},
        timeout=30
    )

    print("=" * 70)
    print("HTTP STATUS")
    print("=" * 70)
    print(response.status_code)

    print("\n" + "=" * 70)
    print("HEADERS")
    print("=" * 70)
    print(response.headers)

    print("\n" + "=" * 70)
    print("BODY")
    print("=" * 70)
    print(response.text)

    try:
        dados = response.json()

        if "access_token" in dados:

            print("\n")
            print("=" * 70)
            print("SUCESSO")
            print("=" * 70)
            print("TOKEN RECEBIDO.")
            print("Primeiros 30 caracteres:")
            print(dados["access_token"][:30] + "...")

        else:

            print("\n")
            print("=" * 70)
            print("SEM ACCESS TOKEN")
            print("=" * 70)

            for chave, valor in dados.items():
                print(f"{chave}: {valor}")

    except Exception:

        print("\nResposta nÃƒÂ£o ÃƒÂ© JSON.")

except Exception:

    print("\n")
    print("=" * 70)
    print("ERRO NA EXECUÃƒâ€¡ÃƒÆ'O")
    print("=" * 70)

    traceback.print_exc()

print("\n")
print("=" * 70)
print("FIM DA AUDITORIA")
print("=" * 70)



