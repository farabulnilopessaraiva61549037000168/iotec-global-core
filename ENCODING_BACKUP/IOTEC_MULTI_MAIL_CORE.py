import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_MULTI_MAIL_CORE.py
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo com mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltiplas caixas de e-mail
# ============================================================

import imaplib
import email
from email.header import decode_header

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# =========================

CAIXAS = [
    {
        "nome": "PESSOAL",
        "email": "seu@gmail.com",
        "senha": "senha_app",
        "imap": "imap.gmail.com",
        "tipo": "OPERACIONAL"
    },
    {
        "nome": "COMERCIAL",
        "email": "seu@proton.me",
        "senha": "senha_app",
        "imap": "imap.gmail.com",  # via encaminhamento
        "tipo": "CLIENTE"
    }
]

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def classificar(tipo_caixa, assunto):
    pass

    assunto = assunto.lower()

    if tipo_caixa == "CLIENTE":
        return "CLIENTE"

    if "pagamento" in assunto or "invoice" in assunto:
        return "FINANCEIRO"

    if "cobranÃƒÆ'Ã†â€™a" in assunto or "dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©bito" in assunto:
        return "ALERTA"

    return "OUTROS"

# =========================
# PROCESSAMENTO
# =========================

def processar_email(tipo, assunto):
    pass

    if tipo == "CLIENTE":
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚Â¤ Atendimento / geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de dossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª")

    elif tipo == "FINANCEIRO":
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Registrar pagamento ou dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vida")

    elif tipo == "ALERTA":
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Notificar administraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")

# =========================
# LEITURA
# =========================

def ler_caixa(config):
    pass

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¬ Lendo caixa: {config['nome']}")

    mail = imaplib.IMAP4_SSL(config["imap"])
    mail.login(config["email"], config["senha"])
    mail.select("inbox")

    status, mensagens = mail.search(None, "ALL")
    mensagens = mensagens[0].split()

    for num in mensagens[-5:]:
        pass

        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        assunto, enc = decode_header(msg["Subject"])[0]
        if isinstance(assunto, bytes):
            assunto = assunto.decode(enc if enc else "utf-8")

        tipo = classificar(config["tipo"], assunto)

        print("Assunto:", assunto)
        print("Classificado como:", tipo)

        processar_email(tipo, assunto)

# =========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def executar():
    pass

    for caixa in CAIXAS:
        ler_caixa(caixa)

if __name__ == "__main__":
    executar()


