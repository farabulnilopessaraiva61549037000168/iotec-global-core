import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def classify_project(score):
    pass

    if score < 100:
        return "PULSEIRA"

    elif score < 500:
        return "COLAR"

    elif score < 1500:
        return "JOIA_RARA"

    elif score < 5000:
        return "COROA_REAL"

    return "ARTEFATO_UNICO"




