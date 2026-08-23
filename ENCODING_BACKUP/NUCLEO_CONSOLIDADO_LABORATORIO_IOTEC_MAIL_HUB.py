import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_MAIL_HUB.py
# Leitura de e-mail + classificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica
# ============================================================

import imaplib
import email
from email.header import decode_header

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

EMAIL = "seuemail@gmail.com"
SENHA = "suasenha"
IMAP_SERVER = "imap.gmail.com"

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def classificar_email(remetente, assunto, corpo):
    pass

    assunto = assunto.lower()

    if "paypal" in remetente or "pagamento" in assunto:
        return "PAGAMENTO"

    elif "cliente" in assunto or "contato" in assunto:
        return "CLIENTE"

    elif "cnpj" in assunto or "empresa" in assunto:
        return "ADMINISTRATIVO"

    elif "formulÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio" in assunto:
        return "PROCESSO"

    elif "cobranÃƒÆ'Ã†â€™a" in assunto or "dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©bito" in assunto:
        return "ALERTA_FINANCEIRO"

    return "OUTROS"

# =========================
# LEITURA DE EMAIL
# =========================

def ler_emails():
    pass

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, SENHA)
    mail.select("inbox")

    status, mensagens = mail.search(None, "ALL")
    mensagens = mensagens[0].split()

    for num in mensagens[-10:]:  # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltimos 10

        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        assunto, encoding = decode_header(msg["Subject"])[0]
        if isinstance(assunto, bytes):
            assunto = assunto.decode(encoding if encoding else "utf-8")

        remetente = msg.get("From")

        tipo = classificar_email(remetente, assunto, "")

        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© Novo Email Detectado")
        print("Assunto:", assunto)
        print("Remetente:", remetente)
        print("Tipo:", tipo)

        # =========================
        # AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICAS
        # =========================

        if tipo == "PAGAMENTO":
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Enviar para mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo financeiro")

        elif tipo == "CLIENTE":
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚Â¤ Enviar para atendimento")

        elif tipo == "PROCESSO":
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Iniciar geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de dossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª")

        elif tipo == "ALERTA_FINANCEIRO":
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Enviar alerta administrativo")

# =========================
# EXECUTAR
# =========================

if __name__ == "__main__":
    ler_emails()


