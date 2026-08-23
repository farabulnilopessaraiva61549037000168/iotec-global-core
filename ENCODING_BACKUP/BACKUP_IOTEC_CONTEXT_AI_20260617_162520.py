import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_resposta(memoria_cliente, mensagem):
    pass

    historico = memoria_cliente["historico"]
    nome = memoria_cliente["nome"]
    servico = memoria_cliente["servico"]

    if len(historico) > 5:
        return f"""
{nome}, jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ estamos acompanhando seu caso ({servico}).

Com base nas interaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes anteriores, estamos avanÃƒÆ'Ã†â€™ando no processo.
"""

    return f"""
{nome}, entendi sua mensagem.

Estamos tratando seu caso ({servico}).
"""


