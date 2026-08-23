import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def verificar_produto(servico, idioma):
    pass

    if idioma == "en":
        # simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de verificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
        tem_em_ingles = False

        if not tem_em_ingles:
            return {
                "status": "pendente_traducao",
                "mensagem": "Produto precisa ser traduzido para inglÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªs"
            }

    return {"status": "ok"}


