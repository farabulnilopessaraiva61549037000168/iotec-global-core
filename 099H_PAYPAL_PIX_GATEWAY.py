import os
import sys
import json
import urllib.request
import urllib.parse
import base64
import argparse
from datetime import datetime, timezone, timedelta

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

# CNPJ e Dados do Vendedor/Empresa IOTEC
EMPRESA_CNPJ = "00.000.000/0001-00"
EMPRESA_NOME = "IOTEC / X27 TECNOLOGIA E SERVICOS"

def carregar_env():
    env = {}
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    env[k] = v
    return env

def obter_hora_brasilia():
    tz_br = timezone(timedelta(hours=-3))
    return datetime.now(tz_br).strftime("%d/%m/%Y %H:%M:%S (Horário de Brasília)")

def gerar_fatura_discriminada(item_nome, item_qtd, valor_unit, comprador_nome="", comprador_cpf=""):
    env = carregar_env()
    cid = env.get("PAYPAL_CLIENT_ID")
    sec = env.get("PAYPAL_CLIENT_SECRET")
    mode = env.get("PAYPAL_MODE", "sandbox")

    if not cid or not sec:
        print("[ERRO CRÍTICO]: Credenciais do PayPal não encontradas em X27_SECRETS.env")
        sys.exit(1)

    base_url = "https://api-m.sandbox.paypal.com" if mode == "sandbox" else "https://api-m.paypal.com"

    # 1. Autenticação OAuth2
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
        print(f"[ERRO AUTENTICAÇÃO]: {e}")
        sys.exit(1)

    valor_total = item_qtd * valor_unit
    hora_emissao = obter_hora_brasilia()

    # 2. Ordem Discriminada na API
    order_url = f"{base_url}/v2/checkout/orders"
    order_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "reference_id": f"IOTEC_REF_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "description": f"Serviço/Produto: {item_nome}",
                "custom_id": f"CNPJ_EMISSOR:{EMPRESA_CNPJ}",
                "amount": {
                    "currency_code": "BRL",
                    "value": f"{valor_total:.2f}",
                    "breakdown": {
                        "item_total": {
                            "currency_code": "BRL",
                            "value": f"{valor_total:.2f}"
                        }
                    }
                },
                "items": [
                    {
                        "name": item_nome,
                        "description": f"Fornecido por {EMPRESA_NOME} - CNPJ: {EMPRESA_CNPJ}",
                        "unit_amount": {
                            "currency_code": "BRL",
                            "value": f"{valor_unit:.2f}"
                        },
                        "quantity": str(item_qtd),
                        "category": "DIGITAL_GOODS"
                    }
                ]
            }
        ],
        "application_context": {
            "brand_name": EMPRESA_NOME,
            "locale": "pt-BR",
            "landing_page": "LOGIN",
            "user_action": "PAY_NOW",
            "return_url": "https://example.com/sucesso",
            "cancel_url": "https://example.com/cancelado"
        }
    }

    req_order = urllib.request.Request(
        order_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=order_headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req_order) as resp:
            res_data = json.loads(resp.read().decode())
            order_id = res_data.get("id")
            status = res_data.get("status")
            approve_url = next((link["href"] for link in res_data.get("links", []) if link.get("rel") == "approve"), None)

            print("="*70)
            print("         COMPROVANTE / FATURA DISCRIMINADA - NÚCLEO IOTEC/X27       ")
            print("="*70)
            print(f" RAZÃO SOCIAL EMISSORA : {EMPRESA_NOME}")
            print(f" CNPJ DO EMISSOR       : {EMPRESA_CNPJ}")
            print(f" DATA/HORA DA EMISSÃO  : {hora_emissao}")
            print("-" * 70)
            if comprador_nome:
                print(f" NOME DO COMPRADOR    : {comprador_nome}")
            if comprador_cpf:
                print(f" CPF/CNPJ COMPRADOR   : {comprador_cpf}")
            print("-" * 70)
            print(" DISCRIMINAÇÃO DOS ITENS/SERVIÇOS:")
            print(f"  • Item/Serviço      : {item_nome}")
            print(f"  • Quantidade        : {item_qtd}")
            print(f"  • Valor Unitário    : R$ {valor_unit:.2f}")
            print(f"  • VALOR TOTAL       : R$ {valor_total:.2f}")
            print("-" * 70)
            print(f" ID DA ORDEM (PAYPAL) : {order_id}")
            print(f" AMBIENTE             : {mode.upper()}")
            print(f" STATUS DA COBRANÇA   : {status}")
            print("="*70)
            print(" LINK PARA APROVAÇÃO E PAGAMENTO PELO CLIENTE:")
            print(f" {approve_url}")
            print("="*70)

    except urllib.error.HTTPError as e:
        print(f"[ERRO AO GERAR FATURA DISCRIMINADA]: {e.read().decode()}")
    except Exception as e:
        print(f"[ERRO INESPERADO]: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gateway de Pagamentos Discriminados IOTEC")
    parser.add_argument("--item", type=str, default="Licenca de Uso Nucleo IOTEC/X27", help="Nome do produto ou serviço")
    parser.add_argument("--qtd", type=int, default=1, help="Quantidade")
    parser.add_argument("--valor", type=float, default=29.90, help="Valor unitário")
    parser.add_argument("--cliente", type=str, default="Cliente Nao Informado", help="Nome do cliente")
    parser.add_argument("--cpf", type=str, default="", help="CPF ou CNPJ do cliente")
    args = parser.parse_args()

    gerar_fatura_discriminada(args.item, args.qtd, args.valor, args.cliente, args.cpf)
