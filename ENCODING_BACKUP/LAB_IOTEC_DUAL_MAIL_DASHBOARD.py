import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_DUAL_MAIL_DASHBOARD.py
# Painel visual com duas caixas de e-mail (Pessoal + Comercial)
# IOTEC - NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Inteligente
# ============================================================

import streamlit as st
import imaplib
import email
from email.header import decode_header

st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¬ IOTEC - Painel de E-mails Inteligente")
st.subheader("Caixa Pessoal + Caixa Comercial (triagem automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica)")

# =========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DAS CAIXAS
# =========================

CAIXAS = [
    {
        "nome": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Caixa Pessoal (Operacional)",
        "email": "seu@gmail.com",
        "senha": "senha_app",
        "imap": "imap.gmail.com",
        "tipo": "OPERACIONAL"
    },
    {
        "nome": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ Caixa Comercial (Clientes)",
        "email": "seu@gmail.com",  # Proton encaminhado
        "senha": "senha_app",
        "imap": "imap.gmail.com",
        "tipo": "CLIENTE"
    }
]

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def classificar_email(tipo_caixa, assunto):
    pass

    assunto = assunto.lower()

    if tipo_caixa == "CLIENTE":
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚Â¤ CLIENTE"

    if "paypal" in assunto or "payment" in assunto:
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â³ PAGAMENTO"

    if "invoice" in assunto or "cobranÃƒÆ'Ã†â€™a" in assunto:
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° FINANCEIRO"

    if "promo" in assunto or "newsletter" in assunto:
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« SPAM"

    return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ OUTROS"

# =========================
# LEITURA DE EMAIL
# =========================

def ler_caixa(config):
    pass

    resultados = []

    try:
        mail = imaplib.IMAP4_SSL(config["imap"])
        mail.login(config["email"], config["senha"])
        mail.select("inbox")

        status, mensagens = mail.search(None, "ALL")
        mensagens = mensagens[0].split()

        for num in mensagens[-5:]:
            pass

            status, msg_data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            assunto, enc = decode_header(msg["Subject"])[0]
            if isinstance(assunto, bytes):
                assunto = assunto.decode(enc if enc else "utf-8")

            remetente = msg.get("From")

            tipo = classificar_email(config["tipo"], assunto)

            resultados.append({
                "assunto": assunto,
                "remetente": remetente,
                "tipo": tipo
            })

    except Exception as e:
        resultados.append({
            "assunto": "Erro ao conectar",
            "remetente": str(e),
            "tipo": "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ERRO"
        })

    return resultados

# =========================
# EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

col1, col2 = st.columns(2)

for i, caixa in enumerate(CAIXAS):
    pass

    dados = ler_caixa(caixa)

    with (col1 if i == 0 else col2):
        pass

        st.markdown(f"### {caixa['nome']}")

        for item in dados:
            pass

            st.markdown(f"""
            ---
            **Tipo:** {item['tipo']}
            **Assunto:** {item['assunto']}
            **Remetente:** {item['remetente']}
            """)

# =========================
# BOTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ATUALIZAR
# =========================

if st.button("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ Atualizar Caixa"):
    st.rerun()


