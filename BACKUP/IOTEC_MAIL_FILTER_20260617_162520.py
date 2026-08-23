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

        "cliente", "contrataÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o", "serviÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

        "anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise", "analysis", "proposta"

    ]



    # =========================

    # PALAVRAS DE PROPAGANDA

    # =========================



    palavras_spam = [

        "promoÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o", "desconto", "oferta",

        "newsletter", "marketing",

        "unsubscribe", "clique aqui"

    ]



    # =========================

    # VERIFICAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

    # =========================



    if any(p in assunto or p in corpo for p in palavras_spam):
        pass

        return "SPAM"



    if any(p in assunto or p in corpo for p in palavras_relevantes):
        pass

        return "RELEVANTE"



    # =========================

    # DOMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂNIO SUSPEITO

    # =========================



    if "@" in remetente:
        pass

        dominio = remetente.split("@")[-1]



        if any(x in dominio for x in ["promo", "ads", "marketing"]):
            pass

            return "SPAM"



    return "NEUTRO"




