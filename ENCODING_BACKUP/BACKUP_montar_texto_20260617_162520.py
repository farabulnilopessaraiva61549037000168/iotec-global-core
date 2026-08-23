import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def montar_texto(f_atual, f_nova, pct):
    return f"""
Foi analisado o impacto da adequaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ao piso salarial.

Folha atual: R$ {f_atual:,.2f}
Folha projetada: R$ {f_nova:,.2f}
VariaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {pct:.2f}%

Recomenda-se avaliar estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gia gradual de adequaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o,
considerando impactos financeiros, operacionais e previdenciÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios.
"""



