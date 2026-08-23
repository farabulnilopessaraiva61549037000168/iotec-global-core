import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def analisar_cenario(d):
    pass

    score = 0

    if d["impacto"] > 100000: score += 2

    elif d["impacto"] > 50000: score += 1



    if d["percentual"] > 30: score += 2

    elif d["percentual"] > 10: score += 1



    if d["risco"] == "ALTO": score += 2

    elif d["risco"] == "MODERADO": score += 1



    if d["cenarios"] >= 3: score += 2

    elif d["cenarios"] == 2: score += 1



    return score



def recomendar_plano(score):
    pass

    if score <= 2:
        pass

        return {"nivel": "Essencial", "valor": 3000}

    elif score <= 5:
        pass

        return {"nivel": "Profissional", "valor": 7000}

    else:
        pass

        return {"nivel": "Premium", "valor": 15000}




