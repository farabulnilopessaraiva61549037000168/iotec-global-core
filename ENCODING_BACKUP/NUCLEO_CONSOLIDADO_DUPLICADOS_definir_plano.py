import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def definir_plano(dados):
    pass

    impacto = dados["impacto"]
    percentual = dados["percentual"]
    risco = dados["risco"]

    score = 0

    if impacto > 100000:
        score += 2
    elif impacto > 50000:
        score += 1

    if percentual > 30:
        score += 2
    elif percentual > 10:
        score += 1

    if risco == "ALTO":
        score += 2
    elif risco == "MODERADO":
        score += 1

    if score <= 2:
        return "Essencial", 3000

    elif score <= 4:
        return "Profissional", 7000

    else:
        return "Premium", 15000


