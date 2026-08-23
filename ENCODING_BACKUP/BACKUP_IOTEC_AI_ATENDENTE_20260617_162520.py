import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def interpretar_mensagem(msg):
    pass

    msg = msg.lower()

    if "1" in msg or "anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise" in msg:
        return "ANALISE"

    elif "2" in msg or "dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvida" in msg:
        return "DUVIDA"

    elif "3" in msg or "acompanhar" in msg:
        return "STATUS"

    elif "4" in msg or "suporte" in msg:
        return "SUPORTE"

    elif "nÃƒÆ'Ã†â€™o entendi" in msg:
        return "REEXPLICAR"

    return "GERAL"


