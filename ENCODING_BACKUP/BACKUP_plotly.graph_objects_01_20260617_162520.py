import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="IoTec EDU - Executive Dashboard",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("IoTec EDU")
st.subheader("Ativo Digital - RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio Executivo")

# =========================
# SIDEBAR (NAVEGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O)
# =========================
st.sidebar.title("Menu")
page = st.sidebar.radio("NavegaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", [
    "VisÃƒÆ'Ã†â€™o Geral",
    "Indicadores",
    "SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "Valuation",
    "ConclusÃƒÆ'Ã†â€™o"
])

# =========================
# DADOS MOCK (ligar no core depois)
# =========================
usuarios = 2988
receita = 146873
lucro = 138000
ticket = 49.4
conversao = 5.4
valuation = 3400000

# =========================
# PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂGINAS
# =========================

if page == "VisÃƒÆ'Ã†â€™o Geral":
    st.markdown("### Plataforma SaaS com geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o recorrente e escalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel")
    st.markdown("Sistema com automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, captaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o e monetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o integradas.")

elif page == "Indicadores":
    col1, col2, col3 = st.columns(3)

    col1.metric("UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios", usuarios)
    col2.metric("Receita Mensal", f"R$ {receita}")
    col3.metric("Lucro", f"R$ {lucro}")

    st.metric("Ticket MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dio", f"R$ {ticket}")
    st.metric("ConversÃƒÆ'Ã†â€™o", f"{conversao}%")

elif page == "SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
    st.markdown("### Ajuste parÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢metros")

    usuarios_sim = st.slider("UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios", 0, 10000, usuarios)
    ticket_sim = st.slider("Ticket", 10, 100, int(ticket))
    conversao_sim = st.slider("ConversÃƒÆ'Ã†â€™o (%)", 1, 10, int(conversao))

    receita_sim = usuarios_sim * ticket_sim

    st.metric("Receita Simulada", f"R$ {receita_sim}")

elif page == "Valuation":
    st.metric("Valuation Estimado", f"R$ {valuation}")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Receita", "Lucro", "Valuation"],
        y=[receita, lucro, valuation]
    ))
    st.plotly_chart(fig, use_container_width=True)

elif page == "ConclusÃƒÆ'Ã†â€™o":
    st.markdown("""
    ### Ativo digital com alto potencial

    - Receita recorrente
    - Escalabilidade
    - Baixa dependÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia operacional
    - Modelo validado
    """)

# =========================
# RODAPÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°
# =========================
st.markdown("---")
st.caption("RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio gerado automaticamente pelo nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo IoTec")


