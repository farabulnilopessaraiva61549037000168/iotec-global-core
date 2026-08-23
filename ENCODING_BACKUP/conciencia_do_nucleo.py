import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def responder(pergunta, idioma="pt"):
    if idioma == "en":
        return "Your request has been processed."
    else:
        return "Seu pedido foi processado."


