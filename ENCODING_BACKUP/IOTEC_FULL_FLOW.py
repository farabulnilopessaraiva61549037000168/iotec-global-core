import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import urllib.parse

# =========================
# GERAR WHATSAPP
# =========================

def gerar_link(nome, telefone, servico):
    pass

    mensagem = f"""
OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ {nome},

Recebemos sua solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o sobre:
{servico}

Responda com o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºmero da opÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:

1 - Iniciar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise
2 - Tirar dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvidas
3 - Acompanhar pedido
4 - Suporte tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico
"""

    texto = urllib.parse.quote(mensagem)

    return f"https://wa.me/55{telefone}?text={texto}"

# =========================
# IA - INTERPRETAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def interpretar(msg):
    pass

    msg = msg.lower()

    if "1" in msg:
        return "ANALISE"
    elif "2" in msg:
        return "DUVIDA"
    elif "3" in msg:
        return "STATUS"
    elif "4" in msg:
        return "SUPORTE"

    return "GERAL"

# =========================
# IA - RESPOSTA
# =========================

def responder(tipo, nome, servico):
    pass

    respostas = {
        "ANALISE": f"{nome}, iniciando anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise do seu caso ({servico}).",
        "DUVIDA": f"{nome}, descreva sua dÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºvida que eu te ajudo.",
        "STATUS": f"{nome}, sua solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ em andamento.",
        "SUPORTE": f"{nome}, descreva o problema tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico.",
        "GERAL": f"{nome}, escolha uma opÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para continuar."
    }

    return respostas.get(tipo)

# =========================
# SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE FLUXO
# =========================

cliente = {
    "nome": "Bruno",
    "telefone": "88999999999",
    "servico": "AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise financeira"
}

link = gerar_link(cliente["nome"], cliente["telefone"], cliente["servico"])

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â² WhatsApp:", link)

# SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de resposta do cliente
msg = "1"

tipo = interpretar(msg)
resposta = responder(tipo, cliente["nome"], cliente["servico"])

print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å" IA:", resposta)


