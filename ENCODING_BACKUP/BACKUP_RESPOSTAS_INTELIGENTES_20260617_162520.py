import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def responder(tipo, nome, servico):
    pass

    if tipo == "ANALISE":
        return f"""
Perfeito, {nome}.

Vamos iniciar a anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise do seu caso ({servico}).

Nosso sistema irÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ processar os dados e gerar um diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico.
VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª serÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ atualizado em breve.
"""

    elif tipo == "DUVIDA":
        return f"""
Sem problema, {nome}.

Explique sua dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvida e eu te respondo de forma objetiva.
"""

    elif tipo == "STATUS":
        return f"""
{nome}, sua solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ em processamento.

Assim que houver atualizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª serÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ notificado automaticamente.
"""

    elif tipo == "SUPORTE":
        return f"""
{nome}, descreva o problema tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico.

Nosso sistema irÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ analisar e te orientar.
"""

    elif tipo == "REEXPLICAR":
        return f"""
Sem problema, {nome}.

Escolha uma opÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:

1 - Iniciar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise
2 - Tirar dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvidas
3 - Acompanhar pedido
4 - Suporte tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico
"""

    return f"""
{nome}, estou aqui para te ajudar.

Escolha uma opÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ou descreva sua necessidade.
"""


