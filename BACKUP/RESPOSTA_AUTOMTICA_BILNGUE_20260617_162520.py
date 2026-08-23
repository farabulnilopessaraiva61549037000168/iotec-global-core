import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from idioma import detectar_idioma



def responder(pergunta):
    pass

    idioma = detectar_idioma(pergunta)



    if idioma == "en":
        pass

        return {

            "idioma": "en",

            "resposta": "Your request has been received. We are processing your service."

        }

    else:
        pass

        return {

            "idioma": "pt",

            "resposta": "Seu pedido foi recebido. Estamos processando seu serviÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o."

        }




