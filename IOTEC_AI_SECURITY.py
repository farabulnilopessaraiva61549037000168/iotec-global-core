import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def verificar_pergunta(msg):
    pass



    msg = msg.lower()



    palavras_bloqueadas = [

        "como foi feito",

        "como funciona o sistema",

        "cÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³digo",

        "api",

        "arquitetura",

        "como vocÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªs fazem",

        "backend",

        "nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo"

    ]



    for p in palavras_bloqueadas:
        pass

        if p in msg:
            pass

            return "BLOQUEADO"



    return "PERMITIDO"






