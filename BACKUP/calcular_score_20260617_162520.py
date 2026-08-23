import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def calcular_score(d):
    pass

    score = 0



    # Impacto absoluto

    if d["impacto"] > 100000: score += 2

    elif d["impacto"] > 50000: score += 1



    # Impacto percentual

    if d["percentual"] > 30: score += 2

    elif d["percentual"] > 10: score += 1



    # Risco

    if d["risco"] == "ALTO": score += 2

    elif d["risco"] == "MODERADO": score += 1



    # CenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rios

    if d["cenarios"] >= 3: score += 2

    elif d["cenarios"] == 2: score += 1



    # Operacional

    if d.get("operacional", "NORMAL") == "CRITICO": score += 1



    return score





