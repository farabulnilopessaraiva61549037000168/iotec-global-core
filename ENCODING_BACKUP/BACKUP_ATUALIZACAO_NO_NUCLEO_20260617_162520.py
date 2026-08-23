import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import smtplib
from email.mime.text import MIMEText

EMAIL_REMETENTE = "seu_email@gmail.com"
SENHA_APP = "sua_senha_app"

def notificar_cliente(pedido, email_destino="seu_email@gmail.com"):
    pass

    mensagem = f"""
IOTEC - ENTREGA

Pedido: {pedido['id']}
ServiÃƒÆ'Ã†â€™o: {pedido['servico']}

Seu serviÃƒÆ'Ã†â€™o foi processado com sucesso.

Obrigado por utilizar a IOTEC.
"""

    msg = MIMEText(mensagem)
    msg["Subject"] = "Entrega IOTEC"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = email_destino

    try:
        servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(msg)
        servidor.quit()

        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© E-mail enviado com sucesso")

    except Exception as e:
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Erro ao enviar e-mail:", e)


