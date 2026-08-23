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
        return resposta_segura(nome)

    # fluxo normal
    return f"""
{nome}, entendi sua solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o sobre {servico}.

Estou analisando e jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ te retorno com precisÃƒÆ'Ã†â€™o.
"""


