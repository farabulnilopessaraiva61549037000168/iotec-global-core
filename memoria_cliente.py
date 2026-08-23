import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def responder(msg, memoria_cliente):
    pass



    tipo = verificar_pergunta(msg)



    nome = memoria_cliente["nome"]

    servico = memoria_cliente["servico"]



    if tipo == "BLOQUEADO":
        pass

        return resposta_segura(nome)



    # fluxo normal

    return f"""

{nome}, entendi sua solicitaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o sobre {servico}.



Estou analisando e jÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ te retorno com precisÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o.

"""






