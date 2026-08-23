import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def interpretar_entrada(texto):
    if "licitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o" in texto.lower():
        return "licitacao"
    elif "concurso" in texto.lower():
        return "concurso"
    elif "auditoria" in texto.lower():
        return "auditoria"
    elif "relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio" in texto.lower():
        return "relatorio"
    else:
        return "outros"


