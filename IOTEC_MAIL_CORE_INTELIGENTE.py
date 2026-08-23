import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC_MAIL_CORE_INTELIGENTE.py

# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo que lÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª e-mail, identifica origem e classifica

# ============================================================



import imaplib

import email

from email.header import decode_header



# =========================

# CONFIG

# =========================



EMAIL = "seuemail@gmail.com"

SENHA = "senha_app"

IMAP = "imap.gmail.com"



# =========================

# DETECTAR PAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂS

# =========================



def detectar_origem(remetente):
    pass



    remetente = remetente.lower()



    if ".br" in remetente:
        pass

        return "Brasil"

    elif ".us" in remetente:
        pass

        return "EUA"

    elif ".de" in remetente:
        pass

        return "Alemanha"

    elif ".pt" in remetente:
        pass

        return "Portugal"

    else:
        pass

        return "Internacional"



# =========================

# CLASSIFICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================



def classificar(assunto, remetente):
    pass



    assunto = assunto.lower()



    if "paypal" in remetente or "payment" in assunto:
        pass

        return "PAGAMENTO"



    elif "formulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio" in assunto or "analysis" in assunto:
        pass

        return "SOLICITACAO"



    elif "support" in assunto or "contato" in assunto:
        pass

        return "CLIENTE"



    elif "invoice" in assunto or "cobranÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a" in assunto:
        pass

        return "FINANCEIRO"



    return "OUTROS"



# =========================

# LEITURA

# =========================



def ler_emails():
    pass



    mail = imaplib.IMAP4_SSL(IMAP)

    mail.login(EMAIL, SENHA)

    mail.select("inbox")



    status, mensagens = mail.search(None, "ALL")

    mensagens = mensagens[0].split()



    for num in mensagens[-10:]:
        pass



        status, msg_data = mail.fetch(num, "(RFC822)")

        msg = email.message_from_bytes(msg_data[0][1])



        assunto, enc = decode_header(msg["Subject"])[0]

        if isinstance(assunto, bytes):
            pass

            assunto = assunto.decode(enc if enc else "utf-8")



        remetente = msg.get("From")



        origem = detectar_origem(remetente)

        tipo = classificar(assunto, remetente)



        print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© NOVA ENTRADA")

        print("Origem:", origem)

        print("Tipo:", tipo)

        print("Assunto:", assunto)



        # =========================

        # AÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES AUTOMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂTICAS

        # =========================



        if tipo == "PAGAMENTO":
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° Confirmar pagamento e liberar fluxo")



        elif tipo == "SOLICITACAO":
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Â¦  Gerar anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise e alimentar painel")



        elif tipo == "CLIENTE":
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤ Enviar para atendimento")



        elif tipo == "FINANCEIRO":
            pass

            print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡ ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¯ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Enviar para setor administrativo")



# =========================

# EXECUTAR

# =========================



if __name__ == "__main__":
    pass

    ler_emails()






