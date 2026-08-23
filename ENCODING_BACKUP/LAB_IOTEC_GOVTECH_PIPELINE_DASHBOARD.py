import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_GOVTECH_PIPELINE_DASHBOARD.py
# Painel visual do fluxo completo (pagamento ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ entrega)
# IOTEC - GovTech Premium
# ============================================================

import streamlit as st
import time

# =========================
# CONFIG UI
# =========================
st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC GovTech Premium")
st.subheader("Painel de Processamento e Entrega de DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico")

# =========================
# ESTADOS DO PROCESSO
# =========================
if "status" not in st.session_state:
    st.session_state.status = "INICIADO"

# =========================
# FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES DO PROCESSO
# =========================

def pagamento():
    st.session_state.status = "PAGAMENTO_CONFIRMADO"

def processar():
    st.session_state.status = "EM_PROCESSAMENTO"

def validar():
    st.session_state.status = "VALIDANDO_DOSSIE"
    time.sleep(1)

    # SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o completa
    paginas = 22
    graficos = 7
    tabelas = 9

    completo = (
        paginas >= 20 and
        graficos >= 6 and
        tabelas >= 8
    )

    if completo:
        st.session_state.status = "APROVADO"
    else:
        st.session_state.status = "INCOMPLETO"

def liberar():
    if st.session_state.status == "APROVADO":
        st.session_state.status = "LIBERADO"

# =========================
# MAPA DE STATUS
# =========================

status_map = {
    "INICIADO": "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Âª Iniciado",
    "PAGAMENTO_CONFIRMADO": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â³ Pagamento Confirmado",
    "EM_PROCESSAMENTO": "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Em Processamento",
    "VALIDANDO_DOSSIE": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Validando DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª",
    "APROVADO": "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Aprovado",
    "INCOMPLETO": "ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Incompleto",
    "LIBERADO": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¤ Liberado ao Cliente"
}

# =========================
# EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE STATUS
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Status Atual do Processo")
st.info(status_map[st.session_state.status])

# =========================
# TIMELINE VISUAL
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Linha do Processo")

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("1", "Entrada")
col2.metric("2", "Pagamento")
col3.metric("3", "Processo")
col4.metric("4", "ValidaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")
col5.metric("5", "AprovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o")
col6.metric("6", "Entrega")

# =========================
# BOTÃƒÆ'Ã†â€™ES DE AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Controle do Processo")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â³ Confirmar Pagamento"):
        pagamento()

with c2:
    if st.button("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Processar"):
        processar()

with c3:
    if st.button("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Validar DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª"):
        validar()

with c4:
    if st.button("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¤ Liberar Cliente"):
        liberar()

# =========================
# DETALHES DO DOSSIÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â 
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ VerificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª")

colA, colB, colC = st.columns(3)

colA.metric("PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ginas", "22")
colB.metric("GrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ficos", "7")
colC.metric("Tabelas", "9")

st.success("DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª atende aos critÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rios mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nimos de qualidade IOTEC")

# =========================
# ALERTA FINAL
# =========================

if st.session_state.status == "LIBERADO":
    st.success("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª liberado e pronto para envio ao cliente")

elif st.session_state.status == "INCOMPLETO":
    st.error("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª incompleto. CorreÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria antes da liberaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")


