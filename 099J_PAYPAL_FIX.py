import os
import urllib.request
import urllib.parse
import json
import base64

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

def reconfigurar():
    print("="*65)
    print("        X27 PAYPAL CREDENTIALS FIX & REPAIR ENGINE        ")
    print("="*65)
    
    cid = input("Cole o PAYPAL_CLIENT_ID: ").strip()
    sec = input("Cole o PAYPAL_CLIENT_SECRET: ").strip()
    
    print("\nQual e o modo dessas credenciais no painel do PayPal?")
    print("1 - LIVE (Producao / Dinheiro Real)")
    print("2 - SANDBOX (Ambiente de Testes)")
    opcao = input("Opcao (1 ou 2, Padrao=1): ").strip()
    
    mode = "sandbox" if opcao == "2" else "live"
    
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(f"PAYPAL_CLIENT_ID={cid}\n")
        f.write(f"PAYPAL_CLIENT_SECRET={sec}\n")
        f.write(f"PAYPAL_MODE={mode}\n")
        
    print(f"\n[OK] Credenciais salvas em modo: {mode.upper()}")
    print("Testando conexao com os servidores do PayPal...\n")
    
    url = "https://api-m.paypal.com/v1/oauth2/token" if mode == "live" else "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    
    auth_str = f"{cid}:{sec}"
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
            print("="*65)
            print(" SUCCESS! PAYPAL CONECTADO E AUTENTICADO COM SUCESSO!")
            print(f" MODO        : {mode.upper()}")
            print(f" TOKEN ATIVO : {token[:25]}... [OK]")
            print("="*65)
    except urllib.error.HTTPError as e:
        print("="*65)
        print(f" [ERRO HTTP {e.code}]: Acesso Negado pelo PayPal.")
        if mode == "live":
            print(" DICA: Se as chaves sao de Sandbox, escolha a Opcao 2 (SANDBOX).")
        else:
            print(" DICA: Se as chaves sao de Producao, escolha a Opcao 1 (LIVE).")
        print("="*65)
    except Exception as e:
        print(f"[FALHA DE CONEXAO]: {e}")

if __name__ == "__main__":
    reconfigurar()
