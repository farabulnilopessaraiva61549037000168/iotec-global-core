import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def recomendar_plano(dados):
    score = calcular_score(dados)

    if score <= 2:
        return {
            "plano": "Essencial",
            "ticket": 3000,
            "mensagem": "AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise objetiva para cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios de baixa complexidade."
        }
    elif score <= 5:
        return {
            "plano": "Profissional",
            "ticket": 7000,
            "mensagem": "Recomendado para decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes com impacto relevante e necessidade de cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios."
        }
    else:
        return {
            "plano": "Premium",
            "ticket": 15000,
            "mensagem": "Indicado para cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos, com alto risco e necessidade de suporte estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gico."
        }


