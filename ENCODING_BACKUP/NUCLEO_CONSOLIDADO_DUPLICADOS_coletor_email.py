import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import imaplib
import email
import json
import os
from datetime import datetime

USER = "iotec.bl@proton.me"
PASS = "vYgir09kMpxz5ipRqAXHeA"
PORT = 1143

BASE = "C:\\IOTEC\\CORE"

def salvar_evento(evento):
    caminho = os.path.join(BASE, "eventos.json")

    if not os.path.exists(caminho):
        lista = []
    else:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except:
            lista = []

    lista.append(evento)

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2)

def coletar():
    print("?? Conectando ao Proton...")

    mail = imaplib.IMAP4("127.0.0.1", PORT)
    mail.starttls()
    mail.login(USER, PASS)

    mail.select("inbox")

    status, mensagens = mail.search(None, "ALL")

    for num in mensagens[0].split()[-10:]:
        pass

        status, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        assunto = str(msg["Subject"])

        evento = {
            "tipo": "email",
            "assunto": assunto,
            "status": "novo",
            "hora": datetime.now().strftime("%H:%M:%S")
        }

        salvar_evento(evento)

    print("? Coleta funcionando 100%")
    mail.logout()

if __name__ == "__main__":
    coletar()


