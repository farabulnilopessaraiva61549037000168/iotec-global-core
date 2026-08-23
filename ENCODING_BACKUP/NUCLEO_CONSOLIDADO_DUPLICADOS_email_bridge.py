import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import imaplib
import email
from email.header import decode_header

print("INICIANDO EMAIL BRIDGE")

# GMAIL
GMAIL_EMAIL = "brunofarabulini@gmail.com"
GMAIL_SENHA = "hxda xhet ddmt euot"

# PROTON (COLOQUE OS DADOS DO BRIDGE)
PROTON_USER = "COLOQUE_AQUI"
PROTON_PASS = "COLOQUE_AQUI"
PROTON_PORT = 1143

def ler_gmail():
    try:
        print("Conectando Gmail...")
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_EMAIL, GMAIL_SENHA)
        mail.select("inbox")

        status, mensagens = mail.search(None, "ALL")

        for num in mensagens[0].split()[-5:]:
            status, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            assunto = decode_header(msg["Subject"])[0][0]
            if isinstance(assunto, bytes):
                assunto = assunto.decode()

            print("GMAIL:", assunto)

        mail.logout()
    except Exception as e:
        print("ERRO GMAIL:", e)

def ler_proton():
    try:
        print("Conectando Proton...")
        mail = imaplib.IMAP4("127.0.0.1", PROTON_PORT)
        mail.login(PROTON_USER, PROTON_PASS)
        mail.select("inbox")

        status, mensagens = mail.search(None, "ALL")

        for num in mensagens[0].split()[-5:]:
            status, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            assunto = decode_header(msg["Subject"])[0][0]
            if isinstance(assunto, bytes):
                assunto = assunto.decode()

            print("PROTON:", assunto)

        mail.logout()
    except Exception as e:
        print("ERRO PROTON:", e)

ler_gmail()
ler_proton()


