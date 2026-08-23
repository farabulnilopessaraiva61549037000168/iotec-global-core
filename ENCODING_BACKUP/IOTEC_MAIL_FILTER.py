import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_MAIL_FILTER.py
# Filtro inteligente de e-mails (relevante vs propaganda)
# ============================================================

def classificar_email(remetente, assunto, corpo):
    pass

    assunto = assunto.lower()
    corpo = corpo.lower()
    remetente = remetente.lower()

    # =========================
    # PALAVRAS RELEVANTES
    # =========================

    palavras_relevantes = [
        "pagamento", "payment", "invoice",
        "cliente", "contrataÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "serviÃƒÆ'Ã†â€™o",
        "anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise", "analysis", "proposta"
    ]

    # =========================
    # PALAVRAS DE PROPAGANDA
    # =========================

    palavras_spam = [
        "promoÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "desconto", "oferta",
        "newsletter", "marketing",
        "unsubscribe", "clique aqui"
    ]

    # =========================
    # VERIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # =========================

    if any(p in assunto or p in corpo for p in palavras_spam):
        return "SPAM"

    if any(p in assunto or p in corpo for p in palavras_relevantes):
        return "RELEVANTE"

    # =========================
    # DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIO SUSPEITO
    # =========================

    if "@" in remetente:
        dominio = remetente.split("@")[-1]

        if any(x in dominio for x in ["promo", "ads", "marketing"]):
            return "SPAM"

    return "NEUTRO"


