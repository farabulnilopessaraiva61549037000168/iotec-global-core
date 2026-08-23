import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="IOTEC CORE SYSTEM",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("IOTEC CORE SYSTEM")
st.subheader("Painel Executivo do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Inteligente")

# =========================
# MENU
# =========================
menu = st.sidebar.selectbox("Ambiente", [
    "VisÃƒÆ'Ã†â€™o do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo",
    "Arquitetura",
    "CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "MonetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "Valuation",
    "SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "ConclusÃƒÆ'Ã†â€™o"
])

# =========================
# DADOS (conectar com core depois)
# =========================
data = {
    "leads": 1543,
    "usuarios": 2988,
    "produtos": 100,
    "receita": 146873,
    "lucro": 138000,
    "valuation": 3400000,
    "ticket": 49.4,
    "conversao": 5.4
}

# =========================
# PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂGINAS
# =========================

if menu == "VisÃƒÆ'Ã†â€™o do NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo":
    st.markdown("""
    ### NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Inteligente AutÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´nomo

    Sistema estruturado para:
    - CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica
    - Processamento de dados
    - GeraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de produtos
    - MonetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o escalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel
    """)

elif menu == "Arquitetura":
    st.markdown("""
    ### Estrutura do Sistema

    - Camada de CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
    - Camada de Processamento
    - Camada de ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
    - Camada de MonetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
    - Camada de Valuation
    """)

elif menu == "CaptaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
    st.metric("Leads captados", data["leads"])
    st.markdown("Sistema automatizado de aquisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de dados.")

elif menu == "ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
    st.metric("Produtos gerados", data["produtos"])
    st.markdown("GeraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automatizada de conteÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºdo e soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.")

elif menu == "MonetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
    col1, col2 = st.columns(2)
    col1.metric("UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios", data["usuarios"])
    col2.metric("Receita", f"R$ {data['receita']}")

    st.metric("Lucro", f"R$ {data['lucro']}")

elif menu == "Valuation":
    st.metric("Valuation estimado", f"R$ {data['valuation']}")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Receita", "Lucro", "Valuation"],
        y=[data["receita"], data["lucro"], data["valuation"]]
    ))
    st.plotly_chart(fig, use_container_width=True)

elif menu == "SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":
    st.markdown("### Ajuste de parÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢metros")

    usuarios = st.slider("UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios", 0, 10000, data["usuarios"])
    ticket = st.slider("Ticket", 10, 100, int(data["ticket"]))

    receita = usuarios * ticket
    st.metric("Receita simulada", f"R$ {receita}")

elif menu == "ConclusÃƒÆ'Ã†â€™o":
    st.markdown("""
    ### ConclusÃƒÆ'Ã†â€™o Executiva

    O IOTEC CORE representa um sistema integrado de geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor digital,
    com capacidade de operar de forma autÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´noma, escalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel e com alta margem.

    Estrutura pronta para expansÃƒÆ'Ã†â€™o e monetizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o em mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltiplos mercados.
    """)

# =========================
# RODAPÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°
# =========================
st.markdown("---")
st.caption("Sistema IOTEC CORE - RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio Executivo Automatizado")


