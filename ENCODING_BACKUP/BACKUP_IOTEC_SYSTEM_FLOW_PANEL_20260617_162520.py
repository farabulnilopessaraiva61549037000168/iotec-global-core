import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_SYSTEM_FLOW_PANEL.py
# Painel de fluxo: Entrada ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ DecisÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da
# ============================================================

import streamlit as st
import random
import time

st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - Fluxo do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo")
st.subheader("Entrada ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ DecisÃƒÆ'Ã†â€™o ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da (Sistema Vivo)")

# =========================
# ESTADO
# =========================

if "entradas" not in st.session_state:
    st.session_state.entradas = []

if "decisoes" not in st.session_state:
    st.session_state.decisoes = []

if "saidas" not in st.session_state:
    st.session_state.saidas = []

if "bloqueios" not in st.session_state:
    st.session_state.bloqueios = []

# =========================
# GERAR ENTRADA (simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)
# =========================

def gerar_entrada():
    setores = ["PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblico", "PME", "Agro", "Tech", "MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dia"]
    return {
        "setor": random.choice(setores),
        "score": random.randint(5, 40)
    }

# =========================
# DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def decidir(entrada):
    pass

    score = entrada["score"]

    if score >= 30:
        return "saida"

    elif score >= 20:
        return "monitorar"

    elif score >= 10:
        return "esperar"

    else:
        return "bloqueio"

# =========================
# CICLO
# =========================

def rodar_ciclo():
    pass

    entrada = gerar_entrada()
    st.session_state.entradas.append(entrada)

    decisao = decidir(entrada)
    st.session_state.decisoes.append(decisao)

    if decisao == "saida":
        st.session_state.saidas.append(entrada)

    elif decisao == "bloqueio":
        st.session_state.bloqueios.append(entrada)

# =========================
# BOTÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

if st.button("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Rodar Ciclo"):
    rodar_ciclo()

# =========================
# EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

col1, col2, col3, col4 = st.columns(4)

# ENTRADAS
with col1:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¥ Entradas")
    for e in st.session_state.entradas[-5:]:
        st.write(e)

# DECISÃƒÆ'Ã†â€™ES
with col2:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  DecisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")
    for d in st.session_state.decisoes[-5:]:
        st.write(d)

# SAÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDAS
with col3:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­das")
    for s in st.session_state.saidas[-5:]:
        st.write(s)

# BLOQUEIOS
with col4:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Bloqueios")
    for b in st.session_state.bloqueios[-5:]:
        st.write(b)

# =========================
# RESUMO
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Resumo do Sistema")

total = len(st.session_state.entradas)
saidas = len(st.session_state.saidas)
bloqueios = len(st.session_state.bloqueios)

c1, c2, c3 = st.columns(3)

c1.metric("Entradas", total)
c2.metric("SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­das", saidas)
c3.metric("Bloqueios", bloqueios)


