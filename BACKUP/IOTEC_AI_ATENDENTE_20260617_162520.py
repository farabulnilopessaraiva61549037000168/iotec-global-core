import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def interpretar_mensagem(msg):
    pass



    msg = msg.lower()



    if "1" in msg or "anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise" in msg:
        pass

        return "ANALISE"



    elif "2" in msg or "dÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºvida" in msg:
        pass

        return "DUVIDA"



    elif "3" in msg or "acompanhar" in msg:
        pass

        return "STATUS"



    elif "4" in msg or "suporte" in msg:
        pass

        return "SUPORTE"



    elif "nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o entendi" in msg:
        pass

        return "REEXPLICAR"



    return "GERAL"




