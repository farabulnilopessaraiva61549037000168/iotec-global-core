import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_PAYPAL_MONITOR.py
import imaplib, email, re

IMAP_SERVER = "imap.gmail.com"
EMAIL = "seu_email@gmail.com"
SENHA = "sua_senha_app"  # use senha de app

def checar():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, SENHA)
    mail.select("inbox")

    status, data = mail.search(None, '(UNSEEN SUBJECT "PayPal")')
    for num in data[0].split():
        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        assunto = msg["subject"]
        corpo = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    corpo = part.get_payload(decode=True).decode(errors="ignore")
        else:
            corpo = msg.get_payload(decode=True).decode(errors="ignore")

        if "pagamento recebido" in corpo.lower():
            print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° PAGAMENTO DETECTADO")

    mail.logout()

if __name__ == "__main__":
    checar()


