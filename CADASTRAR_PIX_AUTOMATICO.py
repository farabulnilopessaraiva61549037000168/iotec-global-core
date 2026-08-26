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

# Payload para chave aleatória (EVP)
body_pix = {
    "type": "EVP"
}

print("===============================================================================")
print(" 🔑 GERANDO CHAVE PIX ALEATÓRIA (EVP) NO ASAAS...")
print("===============================================================================")

res = requests.post("https://www.asaas.com/api/v3/pix/addressKeys", json=body_pix, headers=headers)

if res.status_code in [200, 201]:
    chave_gerada = res.json().get("key")
    print("\n [🟢 SUCESSO] Chave Pix EVP criada com sucesso!")
    print(f" └─ Chave Ativa: {chave_gerada}")
    print("===============================================================================\n")
else:
    print(f"\n [❌ RESPOSTA DO ASAAS]: {res.status_code} - {res.text}\n")
