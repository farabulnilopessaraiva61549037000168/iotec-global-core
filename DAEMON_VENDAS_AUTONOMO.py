import os
import requests

# Lê o token direto do arquivo de texto sem interferência do PowerShell
with open("C:\\IOTEC\\token.txt", "r", encoding="utf-8") as f:
    ASAAS_TOKEN = f.read().strip()

headers = {
    "access_token": ASAAS_TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "IOTEC-Engine/1.0"
}

def criar_cobranca(nome, cnpj, valor):
    # 1. Cadastra/Busca Cliente
    res_cli = requests.post("https://www.asaas.com/api/v3/customers", json={"name": nome, "cpfCnpj": cnpj}, headers=headers)
    cust_id = None
    if res_cli.status_code == 200:
        cust_id = res_cli.json()["id"]
    else:
        res_s = requests.get(f"https://www.asaas.com/api/v3/customers?cpfCnpj={cnpj}", headers=headers)
        if res_s.status_code == 200 and res_s.json().get("data"):
            cust_id = res_s.json()["data"][0]["id"]
            
    if not cust_id:
        print(f"❌ Erro Cliente ({nome}): {res_cli.status_code} - {res_cli.text}")
        return

    # 2. Gera Pix
    body = {"customer": cust_id, "billingType": "PIX", "value": valor, "dueDate": "2026-08-30", "description": f"Licença IOTEC - {nome}"}
    res_cob = requests.post("https://www.asaas.com/api/v3/payments", json=body, headers=headers)
    
    if res_cob.status_code == 200:
        pay = res_cob.json()
        pay_id = pay["id"]
        inv = pay.get("invoiceUrl", "")
        res_qr = requests.get(f"https://www.asaas.com/api/v3/payments/{pay_id}/pixQrCode", headers=headers)
        pix = res_qr.json().get("payload", "") if res_qr.status_code == 200 else ""
        
        print("===============================================================================")
        print(f" 🟢 COBRANÇA REAL GERADA COM SUCESSO!")
        print(f" ├─ Cliente: {nome}")
        print(f" ├─ Fatura: {inv}")
        print(f" └─ PIX Copia e Cola:\n\n{pix}\n")
        print("===============================================================================")
    else:
        print(f"❌ Erro Cobrança ({nome}): {res_cob.status_code} - {res_cob.text}")

print("🚀 PROCESSANDO COBRANÇAS...")
criar_cobranca("BANCO DO BRASIL SA", "00000000000191", 5000.00)
criar_cobranca("SENDAS DISTRIBUIDORA S/A", "06057223000171", 3500.00)
