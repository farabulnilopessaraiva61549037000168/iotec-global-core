import os

path_ws = "wsgi_cloud.py"
if os.path.exists(path_ws):
    with open(path_ws, "r", encoding="utf-8", errors="ignore") as f:
        code_ws = f.read()
    
    # Injeta os dados oficiais de cobranca
    code_ws = code_ws.replace("[REDACTED_BY_PCI_COMPLIANCE]", "Pix/PicPay: IOTEC.BL@proton.me | PayPal: IOTEC.BL@proton.me")
    
    # Atualiza o ticket base de 29.90 para 299.00 nas transacoes padrao
    code_ws = code_ws.replace("29.90", "299.00")
    
    with open(path_ws, "w", encoding="utf-8") as f:
        f.write(code_ws)

print("✅ wsgi_cloud.py atualizado com os dados oficiais de pagamento e ticket de R$ 299,00!")
