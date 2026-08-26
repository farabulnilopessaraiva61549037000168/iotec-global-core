import os
import requests

asaas_token = None
if os.path.exists("C:\\IOTEC\\.env"):
    with open("C:\\IOTEC\\.env", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("ASAAS_API_KEY="):
                asaas_token = line.split("=", 1)[1].strip()

if not asaas_token:
    asaas_token = os.getenv("ASAAS_API_KEY")

headers = {
    "access_token": asaas_token,
    "Content-Type": "application/json",
    "User-Agent": "IOTEC-Engine/1.0"
}

# 1. Puxar o cliente já cadastrado ou criar novo
body_cliente = {
    "name": "CLIENTE TESTE HOMOLOGACAO IOTEC",
    "cpfCnpj": "00000000000191"
}

res_cli = requests.post("https://www.asaas.com/api/v3/customers", json=body_cliente, headers=headers)

if res_cli.status_code == 200:
    customer_id = res_cli.json()["id"]
else:
    # Se já existir, busca pelo CPF/CNPJ
    res_search = requests.get("https://www.asaas.com/api/v3/customers?cpfCnpj=00000000000191", headers=headers)
    customer_id = res_search.json()["data"][0]["id"]

# 2. Criar Cobrança Pix no valor mínimo permitido de R$ 5,00
body_cobranca = {
    "customer": customer_id,
    "billingType": "PIX",
    "value": 5.00,
    "dueDate": "2026-08-27",
    "description": "Ativacao de Caixa Real - Farabulini Lopes Saraiva"
}
res_cob = requests.post("https://www.asaas.com/api/v3/payments", json=body_cobranca, headers=headers)

if res_cob.status_code == 200:
    pay_id = res_cob.json()["id"]
    res_qr = requests.get(f"https://www.asaas.com/api/v3/payments/{pay_id}/pixQrCode", headers=headers)
    if res_qr.status_code == 200:
        qr_data = res_qr.json()
        print("===============================================================================")
        print(" 🟢 PIX REAL GERADO COM SUCESSO NO ASAAS!")
        print("===============================================================================")
        print(f" ├─ ID da Transação: {pay_id}")
        print(f" ├─ Valor: R$ 5,00")
        print(f" └─ Copia e Cola PIX:\n\n{qr_data.get('payload')}\n")
        print("===============================================================================")
    else:
        print(f"❌ Erro ao puxar QR Code: Status {res_qr.status_code} - {res_qr.text}")
else:
    print(f"❌ Erro ao criar cobrança: Status {res_cob.status_code} - {res_cob.text}")
