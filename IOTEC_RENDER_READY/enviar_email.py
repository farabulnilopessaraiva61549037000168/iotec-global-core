import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import smtplib

from email.mime.text import MIMEText



def enviar_email(nome, email, mensagem):
    pass

    corpo = f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}"



    msg = MIMEText(corpo)

    msg['Subject'] = "Novo Lead IOTEC"

    msg['From'] = "iotec.bl@proton.me"

    msg['To'] = "iotec.bl@proton.me"



    server = smtplib.SMTP("127.0.0.1", 1025)

    server.send_message(msg)

    server.quit()





