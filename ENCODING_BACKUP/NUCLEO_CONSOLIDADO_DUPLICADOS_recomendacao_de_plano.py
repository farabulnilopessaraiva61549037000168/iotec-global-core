import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def recomendar_plano(score):
    pass

    if score <= 2:
        return {
            "nivel": "ESSENCIAL",
            "valor": 3000,
            "descricao": "AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise objetiva para cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios de baixa complexidade."
        }

    elif score <= 5:
        return {
            "nivel": "PROFISSIONAL",
            "valor": 7000,
            "descricao": "Recomendado para cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios com impacto relevante e necessidade de simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica."
        }

    else:
        return {
            "nivel": "PREMIUM",
            "valor": 15000,
            "descricao": "Indicado para cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos, com alto risco e necessidade de suporte aprofundado."
        }


