import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def enviar_via_whatsapp(numero, mensagem):
    print(f"Enviando para {numero} no WhatsApp: {mensagem}")



