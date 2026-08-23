import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def analisar_cenario(dados):
    pass



    impacto = dados["impacto"]

    percentual = dados["percentual"]

    risco = dados["risco"]

    cenarios = dados.get("cenarios", 1)



    score = 0



    # Impacto financeiro

    if impacto > 100000:
        pass

        score += 2

    elif impacto > 50000:
        pass

        score += 1



    # Impacto percentual

    if percentual > 30:
        pass

        score += 2

    elif percentual > 10:
        pass

        score += 1



    # Risco

    if risco == "ALTO":
        pass

        score += 2

    elif risco == "MODERADO":
        pass

        score += 1



    # CenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios

    if cenarios >= 3:
        pass

        score += 2

    elif cenarios == 2:
        pass

        score += 1



    return score






