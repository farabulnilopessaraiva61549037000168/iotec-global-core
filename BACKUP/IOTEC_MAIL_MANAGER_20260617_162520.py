import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC_MAIL_MANAGER.py

# Monitoramento + limpeza + organizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de e-mails

# ============================================================



import imaplib

import email

from email.header import decode_header



EMAIL = "seu@gmail.com"

SENHA = "senha_app"

IMAP = "imap.gmail.com"



# =========================

# CLASSIFICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O SIMPLES

# =========================



def classificar(assunto):
    pass



    assunto = assunto.lower()



    if "paypal" in assunto or "payment" in assunto:
        pass

        return "FINANCEIRO"



    if "formulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio" in assunto or "analysis" in assunto:
        pass

        return "CLIENTE"



    if "promo" in assunto or "newsletter" in assunto:
        pass

        return "SPAM"



    return "OUTROS"



# =========================

# ORGANIZAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



def organizar_email(mail, num, tipo):
    pass



    if tipo == "SPAM":
        pass

        mail.copy(num, "Spam")



    elif tipo == "CLIENTE":
        pass

        mail.copy(num, "Processados")



    elif tipo == "FINANCEIRO":
        pass

        mail.copy(num, "Financeiro")



    # marca como lido

    mail.store(num, '+FLAGS', '\\Seen')



# =========================

# MONITORAMENTO

# =========================



def monitorar():
    pass



    mail = imaplib.IMAP4_SSL(IMAP)

    mail.login(EMAIL, SENHA)

    mail.select("inbox")



    status, mensagens = mail.search(None, "UNSEEN")

    mensagens = mensagens[0].split()



    for num in mensagens:
        pass



        status, msg_data = mail.fetch(num, "(RFC822)")

        msg = email.message_from_bytes(msg_data[0][1])



        assunto, enc = decode_header(msg["Subject"])[0]

        if isinstance(assunto, bytes):
            pass

            assunto = assunto.decode(enc if enc else "utf-8")



        tipo = classificar(assunto)



        print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© Novo:", assunto, "| Tipo:", tipo)



        organizar_email(mail, num, tipo)



# =========================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



if __name__ == "__main__":
    pass

    monitorar()




