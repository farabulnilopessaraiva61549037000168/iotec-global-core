import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_texto_contextual(tipo, dados):
    pass

    if tipo == "juridico":
        return f"""
Observa-se, a partir da anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise realizada, que a adequaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ao novo cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio pode implicar aumento da exposiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o a riscos administrativos e financeiros.

Sugere-se a adoÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de medidas preventivas, com vistas ÃƒÆ'Ã†â€™  mitigaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de possÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis impactos futuros.
"""

    elif tipo == "publico":
        return f"""
A anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise indica aumento significativo da despesa com pessoal.

Recomenda-se planejamento estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gico para adequaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, evitando comprometimento do equilÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­brio orÃƒÆ'Ã†â€™amentÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio.
"""

    elif tipo == "privado":
        return f"""
A projeÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o aponta aumento nos custos operacionais.

ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° recomendada a adoÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de medidas de ajuste para preservar a sustentabilidade financeira.
"""


