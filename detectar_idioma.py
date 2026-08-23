import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def detectar_idioma(texto):
    pass

    ingles = ["the", "and", "how", "what", "can", "you"]



    for palavra in ingles:
        pass

        if palavra in texto.lower():
            pass

            return "en"



    return "pt"






