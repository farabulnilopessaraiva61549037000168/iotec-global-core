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



ARQUIVO = (
    r"C:\IOTEC\NUCLEO_CONSOLIDADO"
    r"\FINANCEIRO\pagamentos.json"
)



def salvar_pagamento(valor, descricao):
    pass

    try:
        pass

        with open(ARQUIVO, "r") as f:
            pass

            dados = json.load(f)

    except:
        pass

        dados = []



    dados.append({

        "valor": valor,

        "descricao": descricao,

        "status": "confirmado",

        "origem": "paypal",

        "data": datetime.now().strftime("%Y-%m-%d %H:%M")

    })



    with open(ARQUIVO, "w") as f:
        pass

        json.dump(dados, f, indent=2)



def verificar():
    pass

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    mail.login(EMAIL_USER, EMAIL_PASS)

    mail.select("inbox")



    status, mensagens = mail.search(None, '(UNSEEN SUBJECT "pagamento")')



    for num in mensagens[0].split():
        pass

        status, dados = mail.fetch(num, "(RFC822)")

        msg = email.message_from_bytes(dados[0][1])



        corpo = ""



        if msg.is_multipart():
            pass

            for part in msg.walk():
                pass

                if part.get_content_type() == "text/plain":
                    pass

                    corpo = part.get_payload(decode=True).decode(errors="ignore")

        else:
            pass

            corpo = msg.get_payload(decode=True).decode(errors="ignore")



        if "pagou" in corpo.lower() or "pagamento recebido" in corpo.lower():
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° PAGAMENTO DETECTADO")



            valor = 0.0

            descricao = "Pagamento PayPal"



            salvar_pagamento(valor, descricao)



    mail.logout()



if __name__ == "__main__":
    pass

    verificar()








