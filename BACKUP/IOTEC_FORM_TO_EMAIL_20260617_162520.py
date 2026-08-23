import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import smtplib

from email.mime.text import MIMEText



EMAIL_REMETENTE = "seuemail@gmail.com"

SENHA = "senha_app"

EMAIL_DESTINO = "seuemail@gmail.com"



def enviar_formulario(nome, empresa, telefone, problema):
    pass



    corpo = f"""

[IOTEC_FORM]



NOME: {nome}

EMPRESA: {empresa}

TELEFONE: {telefone}

PROBLEMA: {problema}

"""



    msg = MIMEText(corpo)

    msg["Subject"] = "Novo FormulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio - Cliente"

    msg["From"] = EMAIL_REMETENTE

    msg["To"] = EMAIL_DESTINO



    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login(EMAIL_REMETENTE, SENHA)

    server.send_message(msg)

    server.quit()



    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© FormulÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio enviado para o e-mail")





