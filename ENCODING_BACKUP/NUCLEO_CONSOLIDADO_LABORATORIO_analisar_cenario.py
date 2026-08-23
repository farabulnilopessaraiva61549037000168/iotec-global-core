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
        score += 2
    elif impacto > 50000:
        score += 1

    # Impacto percentual
    if percentual > 30:
        score += 2
    elif percentual > 10:
        score += 1

    # Risco
    if risco == "ALTO":
        score += 2
    elif risco == "MODERADO":
        score += 1

    # CenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios
    if cenarios >= 3:
        score += 2
    elif cenarios == 2:
        score += 1

    return score


