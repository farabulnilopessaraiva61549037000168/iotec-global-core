import os
import urllib.request
import urllib.parse
import json
import base64

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

def carregar_env():
    secrets = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    secrets[k.strip()] = v.strip()
    return secrets

def salvar_env_key(chave, valor):
    secrets = carregar_env()
    secrets[chave] = valor
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        for k, v in secrets.items():
            f.write(f"{k}={v}\n")

def obter_access_token_paypal():
    secrets = carregar_env()
    client_id = secrets.get("PAYPAL_CLIENT_ID", "")
    client_secret = secrets.get("PAYPAL_CLIENT_SECRET", "")
    mode = secrets.get("PAYPAL_MODE", "live") # 'live' ou 'sandbox'

    if not client_id or not client_secret:
        print("\n[!] Credenciais do PayPal não encontradas no arquivo X27_SECRETS.env")
        client_id = input("Digite o PAYPAL_CLIENT_ID: ").strip()
        client_secret = input("Digite o PAYPAL_CLIENT_SECRET: ").strip()
        
        if client_id and client_secret:
            salvar_env_key("PAYPAL_CLIENT_ID", client_id)
            salvar_env_key("PAYPAL_CLIENT_SECRET", client_secret)
            salvar_env_key("PAYPAL_MODE", "live")
            print("[OK] Credenciais salvas com sucesso em C:\\IOTEC\\X27_SECRETS.env!")
        else:
            print("[ERRO] Credenciais inválidas.")
            return None

    # URL oficial do PayPal
    url = "https://api-m.paypal.com/v1/oauth2/token" if mode == "live" else "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    
    # Autenticação Basic Auth (Client_ID:Client_Secret em Base64)
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode()

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            token = res_data.get("access_token")
            expires_in = res_data.get("expires_in")
            
            print("\n==================================================")
            print("         X27 PAYPAL AUTOMATIC TOKEN ENGINE        ")
            print("==================================================")
            print(f" STATUS API      : AUTENTICADO E ONLINE ({mode.upper()})")
            print(f" TOKEN OBTIDO    : {token[:20]}... [OCULTO]")
            print(f" VALIDADE TOKEN  : {expires_in} segundos")
            print("==================================================")
            return token
    except Exception as e:
        print(f"\n[ERRO NA AUTENTICAÇÃO PAYPAL]: {e}")
        print("Verifique se o Client ID e Secret estão corretos no C:\\IOTEC\\X27_SECRETS.env")
        return None

if __name__ == "__main__":
    obter_access_token_paypal()
