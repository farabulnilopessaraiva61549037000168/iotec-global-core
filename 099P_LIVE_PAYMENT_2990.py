import sys
import json
import argparse
import requests
from datetime import datetime, timezone, timedelta

# Credenciais Oficiais LIVE (Produção IOTEC)
CLIENT_ID = "AUFsIcepzxZyce0ii28lKKcFdflhRQioxI8mzBJvKSKGikX8B53NNy0rWP3ga04_itSAvQzvCgWF-YEY"
CLIENT_SECRET = "EOcWsBThytL1r9SIafn_3wwulYBJXNeHHvuJHHumANzuww-FF5no2wxtX44_14FWfif4X1ww3TUxuaix"
BASE_URL = "https://api-m.paypal.com"

def obter_hora_brasilia():
    tz_br = timezone(timedelta(hours=-3))
    return datetime.now(tz_br).strftime("%d/%m/%Y %H:%M:%S")

def obter_access_token():
    url = f"{BASE_URL}/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"[ERRO Token] {response.status_code}: {response.text}")
        sys.exit(1)

def criar_ordem_live(nome, sobrenome, email):
    token = obter_access_token()
    hora_emissao = obter_hora_brasilia()
    
    url = f"{BASE_URL}/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    payload = {
        "intent": "CAPTURE",
        "payer": {
            "name": {
                "given_name": nome,
                "surname": sobrenome
            },
            "email_address": email
        },
        "purchase_units": [
            {
                "reference_id": "IOTEC_LIVE_2990",
                "description": "Fatura Atendimento IOTEC - R$ 29,90",
                "custom_id": f"AUDIT_BR_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "amount": {
                    "currency_code": "BRL",
                    "value": "29.90",
                    "breakdown": {
                        "item_total": {
                            "currency_code": "BRL",
                            "value": "29.90"
                        }
                    }
                },
                "items": [
                    {
                        "name": "Licenca / Servico Atendimento IOTEC Base",
                        "sku": "IOTEC-SRV-2990",
                        "unit_amount": {
                            "currency_code": "BRL",
                            "value": "29.90"
                        },
                        "quantity": "1",
                        "category": "DIGITAL_GOODS"
                    }
                ]
            }
        ],
        "application_context": {
            "brand_name": "IOTEC / X27 TECNOLOGIA",
            "locale": "pt-BR",
            "landing_page": "LOGIN",
            "user_action": "PAY_NOW",
            "return_url": "https://iotec.com.br/sucesso",
            "cancel_url": "https://iotec.com.br/cancelado"
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code in [200, 201]:
        data = response.json()
        ordem_id = data["id"]
        approve_url = next(link["href"] for link in data["links"] if link["rel"] == "approve")
        
        print("="*65)
        print("     NÚCLEO IOTEC/X27 - COBRANÇA REAL (LIVE) GERADA     ")
        print("="*65)
        print(f" [!] HORA DE EMISSÃO : {hora_emissao} (Horário de Brasília)")
        print(f" [!] CLIENTE (PAYER) : {nome} {sobrenome} ({email})")
        print(f" [!] ID DA ORDEM     : {ordem_id}")
        print(f" [!] VALOR TOTAL     : R$ 29,90")
        print("-" * 65)
        print(" >> LINK DE PAGAMENTO REAL EXPOSTO PARA O CLIENTE:")
        print(f" {approve_url}")
        print("="*65)
    else:
        print(f"[ERRO Criar Ordem] {response.status_code}: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de Cobrança Live IOTEC")
    parser.add_argument("--nome", type=str, default="Cliente", help="Nome do cliente")
    parser.add_argument("--sobrenome", type=str, default="IOTEC", help="Sobrenome do cliente")
    parser.add_argument("--email", type=str, default="cliente@iotec.com.br", help="E-mail do cliente")
    args = parser.parse_args()

    criar_ordem_live(args.nome, args.sobrenome, args.email)
