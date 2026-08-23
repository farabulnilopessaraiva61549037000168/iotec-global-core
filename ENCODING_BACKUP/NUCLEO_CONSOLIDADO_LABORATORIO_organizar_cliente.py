import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def organizar_cliente(dados):
    pass

    cliente = {
        "nome": dados.get("nome"),
        "empresa": dados.get("empresa"),
        "telefone": dados.get("telefone"),
        "problema": dados.get("problema"),
        "status": "NOVO"
    }

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Cliente organizado no nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo:")
    print(cliente)

    # Aqui vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode:
    # - salvar em banco
    # - enviar para painel
    # - iniciar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica



