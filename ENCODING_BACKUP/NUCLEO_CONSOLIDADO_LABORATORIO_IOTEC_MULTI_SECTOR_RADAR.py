import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_MULTI_SECTOR_RADAR.py
# Radar multissetorial de oportunidades
# ============================================================

import streamlit as st

st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - Radar Multissetorial")
st.subheader("Mapa inteligente de oportunidades por setor")

# =========================
# BASE DE LEADS (exemplo)
# =========================

if "leads" not in st.session_state:
    st.session_state.leads = [
        {"setor": "PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblico", "entidade": "Prefeitura X", "score": 32},
        {"setor": "PME", "entidade": "Empresa Y", "score": 18},
        {"setor": "Agro", "entidade": "Fazenda Z", "score": 25},
        {"setor": "Tech", "entidade": "Startup A", "score": 12},
        {"setor": "MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dia", "entidade": "Produtora B", "score": 8},
    ]

# =========================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def classificar(score):
    if score >= 30:
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Alta"
    elif score >= 20:
        return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¡ MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia"
    else:
        return "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Âª Baixa"

# =========================
# AGRUPAR POR SETOR
# =========================

setores = {}

for lead in st.session_state.leads:
    setor = lead["setor"]
    if setor not in setores:
        setores[setor] = []
    setores[setor].append(lead)

# =========================
# EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â Setores Monitorados")

cols = st.columns(len(setores))

for i, (setor, leads) in enumerate(setores.items()):
    with cols[i]:
        st.markdown(f"## {setor}")

        for l in leads:
            prioridade = classificar(l["score"])

            st.markdown(f"""
            ---
            **ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ {l['entidade']}**
            Score: {l['score']}
            Prioridade: {prioridade}
            """)

# =========================
# RESUMO GERAL
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Resumo do Radar")

total = len(st.session_state.leads)
alta = len([l for l in st.session_state.leads if l["score"] >= 30])
media = len([l for l in st.session_state.leads if 20 <= l["score"] < 30])
baixa = len([l for l in st.session_state.leads if l["score"] < 20])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", total)
col2.metric("Alta Prioridade", alta)
col3.metric("MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia", media)
col4.metric("Baixa", baixa)


