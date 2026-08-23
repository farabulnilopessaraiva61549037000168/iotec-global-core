import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import urllib.parse

def gerar_whatsapp(nome, telefone, servico):
    pass

    mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {nome},

Recebemos sua solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o sobre:
{servico}

Para agilizar, escolha uma opÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:

1 - Iniciar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise
2 - Tirar dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvidas
3 - Acompanhar pedido
4 - Suporte tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico

Equipe IOTEC
"""

    texto = urllib.parse.quote(mensagem)

    link = f"https://wa.me/55{telefone}?text={texto}"

    return link



