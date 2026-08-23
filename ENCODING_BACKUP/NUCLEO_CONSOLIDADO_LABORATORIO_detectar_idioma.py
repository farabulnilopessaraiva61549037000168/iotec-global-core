import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def detectar_idioma(texto):
    ingles = ["the", "and", "how", "what", "can", "you"]

    for palavra in ingles:
        if palavra in texto.lower():
            return "en"

    return "pt"


