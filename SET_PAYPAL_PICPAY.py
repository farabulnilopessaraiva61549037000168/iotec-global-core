import os
import re
import sqlite3

print("======================================================================")
print(" CONFIGURAÇÃO DE RECEBIMENTO DIRETO: PAYPAL & PICPAY / PIX ")
print("======================================================================")

paypal_email = input("Digite seu e-mail do PayPal para recebimentos: ").strip()
picpay_pix_key = input("Digite sua Chave Pix (PicPay ou banco principal): ").strip()

# Grava as credenciais no arquivo de configuracao do ambiente local
env_content = f"""
PAYPAL_RECEIVER_EMAIL={paypal_email}
PICPAY_PIX_KEY={picpay_pix_key}
ACTIVE_GATEWAY=PAYPAL_PICPAY_HYBRID
"""

with open(".env", "a", encoding="utf-8") as f:
    f.write(env_content)

# Atualiza a estrutura do gateway de pagamento nos scripts principais
path_ws = "wsgi_cloud.py"
if os.path.exists(path_ws):
    with open(path_ws, "r", encoding="utf-8", errors="ignore") as f:
        code_ws = f.read()
    
    code_ws = code_ws.replace("[REDACTED_BY_PCI_COMPLIANCE]", f"Pix/PicPay: {picpay_pix_key} | PayPal: {paypal_email}")
    
    with open(path_ws, "w", encoding="utf-8") as f:
        f.write(code_ws)

print("\n✅ CREDENCIAIS CONFIGURADAS COM SUCESSO!")
print(f"-> PayPal  : {paypal_email}")
print(f"-> PicPay/Pix: {picpay_pix_key}")
print("======================================================================")
