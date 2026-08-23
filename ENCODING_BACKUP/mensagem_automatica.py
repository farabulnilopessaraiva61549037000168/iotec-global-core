import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_mensagem(plano):
    pass

    return f"""
NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel de anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise recomendado: {plano['nivel']}

Com base nos dados analisados, o cenÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio apresenta complexidade compatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel com o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel {plano['nivel']}, sendo este o mais adequado para garantir uma avaliaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o completa e segura.

{plano['descricao']}

Investimento estimado: R$ {plano['valor']:,.2f}
"""



