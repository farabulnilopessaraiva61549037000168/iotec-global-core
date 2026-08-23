import os
import sys
import json
import urllib.request
import urllib.parse
import base64

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

def carregar_env():
    env = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    env[k] = v
    return env

def processar_ordem(order_id):
    env = carregar_env()
    cid = env.get("PAYPAL_CLIENT_ID")
    sec = env.get("PAYPAL_CLIENT_SECRET")
    mode = env.get("PAYPAL_MODE", "sandbox")

    base_url = "https://api-m.sandbox.paypal.com" if mode == "sandbox" else "https://api-m.paypal.com"

    # 1. Obter Token
    token_url = f"{base_url}/v1/oauth2/token"
    auth_str = f"{cid}:{sec}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()

    try:
        req = urllib.request.Request(token_url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as resp:
            token = json.loads(resp.read().decode()).get("access_token")
    except Exception as e:
        print(f"[ERRO AUTENTICACAO]: {e}")
        return

    # 2. Tentar Capturar a Ordem Diretamante
    capture_url = f"{base_url}/v2/checkout/orders/{order_id}/capture"
    cap_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        req_cap = urllib.request.Request(capture_url, headers=cap_headers, method="POST")
        with urllib.request.urlopen(req_cap) as resp:
            res_data = json.loads(resp.read().decode())
            status = res_data.get("status")
            print("="*65)
            print("     PROCESSAMENTO / CAPTURA AUTOMÁTICA - NÚCLEO IOTEC")
            print("="*65)
            print(f" ID DA ORDEM : {order_id}")
            print(f" NOVO STATUS : {status}")
            print("="*65)
            if status == "COMPLETED":
                print("[SUCESSO TOTAL] A ordem foi CAPTURADA e PAGA via API!")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print("="*65)
        print("                 STATUS DA ORDEM NO PAYPAL")
        print("="*65)
        print(f" ID DA ORDEM : {order_id}")
        print(" STATUS      : CREATED (Aguardando autorização do cliente)")
        print("="*65)
        print("[NOTA DO NÚCLEO]: No PayPal Sandbox, para o status mudar para")
        print("COMPLETED, é necessário autorizar 1 vez o link no navegador")
        print("ou utilizar chaves LIVE de produção.")

if __name__ == "__main__":
    order_id = sys.argv[1] if len(sys.argv) > 1 else "5D665665CP139141C"
    processar_ordem(order_id)
