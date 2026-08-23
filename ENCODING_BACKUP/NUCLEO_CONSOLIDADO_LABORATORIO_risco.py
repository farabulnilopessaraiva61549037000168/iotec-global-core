import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def avaliar_risco(aumento_percentual):
    if aumento_percentual < 10:
        return "BAIXO"
    elif aumento_percentual < 30:
        return "MODERADO"
    else:
        return "ALTO"


