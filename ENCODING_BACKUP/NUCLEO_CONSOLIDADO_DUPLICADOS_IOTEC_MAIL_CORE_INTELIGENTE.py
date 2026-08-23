import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_MAIL_CORE_INTELIGENTE.py
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo que lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª e-mail, identifica origem e classifica
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
# DETECTAR PAÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂS
# =========================

def detectar_origem(remetente):
    pass

    remetente = remetente.lower()

    if ".br" in remetente:
        return "Brasil"
    elif ".us" in remetente:
        return "EUA"
    elif ".de" in remetente:
        return "Alemanha"
    elif ".pt" in remetente:
        return "Portugal"
    else:
        return "Internacional"

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def classificar(assunto, remetente):
    pass

    assunto = assunto.lower()

    if "paypal" in remetente or "payment" in assunto:
        return "PAGAMENTO"

    elif "formulÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio" in assunto or "analysis" in assunto:
        return "SOLICITACAO"

    elif "support" in assunto or "contato" in assunto:
        return "CLIENTE"

    elif "invoice" in assunto or "cobranÃƒÆ'Ã†â€™a" in assunto:
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
            assunto = assunto.decode(enc if enc else "utf-8")

        remetente = msg.get("From")

        origem = detectar_origem(remetente)
        tipo = classificar(assunto, remetente)

        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© NOVA ENTRADA")
        print("Origem:", origem)
        print("Tipo:", tipo)
        print("Assunto:", assunto)

        # =========================
        # AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES AUTOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICAS
        # =========================

        if tipo == "PAGAMENTO":
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Confirmar pagamento e liberar fluxo")

        elif tipo == "SOLICITACAO":
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Gerar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise e alimentar painel")

        elif tipo == "CLIENTE":
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚Â¤ Enviar para atendimento")

        elif tipo == "FINANCEIRO":
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Enviar para setor administrativo")

# =========================
# EXECUTAR
# =========================

if __name__ == "__main__":
    ler_emails()


