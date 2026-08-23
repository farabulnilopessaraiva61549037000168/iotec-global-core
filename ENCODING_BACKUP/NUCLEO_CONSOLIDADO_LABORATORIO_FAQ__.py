import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
FAQ = {}

def registrar_faq(pergunta, resposta):
    FAQ[pergunta.lower()] = resposta

def consultar_faq(pergunta):
    return FAQ.get(pergunta.lower(), "Desculpe, essa informaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o nÃƒÆ'Ã†â€™o estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ registrada ainda.")



