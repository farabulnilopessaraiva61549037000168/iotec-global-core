import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_CORE_QUEUE_PANEL.py
# Painel central de clientes (fila + prioridade + auditoria)
# ============================================================

import streamlit as st

st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - Central de OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes")
st.subheader("Fila Inteligente de Clientes")

# =========================
# BANCO SIMPLES (memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria)
# =========================

if "clientes" not in st.session_state:
    st.session_state.clientes = []

if "historico" not in st.session_state:
    st.session_state.historico = []

# =========================
# ADICIONAR CLIENTE (simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)
# =========================

def adicionar_cliente(nome, prioridade, servico):
    pass

    st.session_state.clientes.append({
        "nome": nome,
        "prioridade": prioridade,
        "servico": servico,
        "status": "ATIVO"
    })

# =========================
# ORDENAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================

def ordenar():
    pass

    prioridade_map = {
        "ALTA": 1,
        "MEDIA": 2,
        "BAIXA": 3
    }

    st.session_state.clientes.sort(
        key=lambda x: prioridade_map[x["prioridade"]]
    )

# =========================
# CONCLUIR CLIENTE
# =========================

def concluir(index):
    pass

    cliente = st.session_state.clientes.pop(index)

    # envia para auditoria
    st.session_state.historico.append(cliente)

# =========================
# INTERFACE
# =========================

st.markdown("### ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¾ Novo Cliente")

nome = st.text_input("Nome")
prioridade = st.selectbox("Prioridade", ["ALTA", "MEDIA", "BAIXA"])
servico = st.text_input("ServiÃƒÆ'Ã†â€™o")

if st.button("Adicionar Cliente"):
    adicionar_cliente(nome, prioridade, servico)

ordenar()

# =========================
# FILA ATIVA
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Fila Ativa")

for i, c in enumerate(st.session_state.clientes):
    pass

    col1, col2, col3, col4 = st.columns([3,2,2,1])

    col1.write(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å"Ãƒâ€šÃ‚Â¤ {c['nome']}")
    col2.write(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ {c['prioridade']}")
    col3.write(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â¼ {c['servico']}")

    if col4.button("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Concluir", key=i):
        concluir(i)

# =========================
# HISTÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRICO (AUDITORIA)
# =========================

st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¾ Auditoria / HistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico")

for h in st.session_state.historico:
    st.write(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â {h['nome']} - {h['servico']}")


