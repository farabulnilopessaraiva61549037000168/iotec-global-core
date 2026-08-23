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
        pass

        score += 2

    elif impacto > 50000:
        pass

        score += 1



    if percentual > 30:
        pass

        score += 2

    elif percentual > 10:
        pass

        score += 1



    if risco == "ALTO":
        pass

        score += 2

    elif risco == "MODERADO":
        pass

        score += 1



    if score <= 2:
        pass

        return "Essencial", 3000



    elif score <= 4:
        pass

        return "Profissional", 7000



    else:
        pass

        return "Premium", 15000




