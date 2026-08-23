import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import imaplib
import email
import json
from datetime import datetime

IMAP_SERVER = "imap.gmail.com"
EMAIL_USER = "SEU_EMAIL@gmail.com"
EMAIL_PASS = "SENHA_DE_APP"

ARQUIVO = "C:\\IOTEC\\financeiro\\pagamentos.json"

def salvar_pagamento(valor, descricao):
    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
    except:
        dados = []

    dados.append({
        "valor": valor,
        "descricao": descricao,
        "status": "confirmado",
        "origem": "paypal",
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=2)

def verificar():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")

    status, mensagens = mail.search(None, '(UNSEEN SUBJECT "pagamento")')

    for num in mensagens[0].split():
        status, dados = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(dados[0][1])

        corpo = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    corpo = part.get_payload(decode=True).decode(errors="ignore")
        else:
            corpo = msg.get_payload(decode=True).decode(errors="ignore")

        if "pagou" in corpo.lower() or "pagamento recebido" in corpo.lower():
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° PAGAMENTO DETECTADO")

            valor = 0.0
            descricao = "Pagamento PayPal"

            salvar_pagamento(valor, descricao)

    mail.logout()

if __name__ == "__main__":
    verificar()


