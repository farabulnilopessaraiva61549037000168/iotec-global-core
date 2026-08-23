import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC LIVE CONTROL TOWER
# ============================================================

import streamlit as st
import sqlite3
import pandas as pd
import time

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

st.set_page_config(

    page_title="IOTEC CONTROL TOWER",

    layout="wide"
)

# ============================================================
# AUTO REFRESH
# ============================================================

st.autorefresh(
    interval=5000,
    key="iotec_refresh"
)

# ============================================================
# CONEXÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

conn = sqlite3.connect(
    "iotec_operational.db"
)

# ============================================================
# LEITURA DE DADOS
# ============================================================

clients = pd.read_sql_query(
    "SELECT * FROM clients",
    conn
)

requests = pd.read_sql_query(
    "SELECT * FROM requests",
    conn
)

payments = pd.read_sql_query(
    "SELECT * FROM payments",
    conn
)

logs = pd.read_sql_query(
    "SELECT * FROM logs",
    conn
)

# ============================================================
# TOTAL FINANCEIRO
# ============================================================

if len(payments) > 0:
    pass

    total_revenue = payments["amount"].sum()

else:
    pass

    total_revenue = 0

# ============================================================
# CABEÃƒÆ'Ã†â€™ALHO
# ============================================================

st.title("IOTEC LIVE CONTROL TOWER")

st.caption(
    "GovernanÃƒÆ'Ã†â€™a Operacional Viva"
)

# ============================================================
# STATUS OPERACIONAL
# ============================================================

st.success("NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO OPERACIONAL ONLINE")

# ============================================================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TRICAS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "CLIENTES",
    len(clients)
)

col2.metric(
    "SOLICITAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES",
    len(requests)
)

col3.metric(
    "PAGAMENTOS",
    len(payments)
)

col4.metric(
    "RECEITA TOTAL",
    f"R$ {total_revenue:,.2f}"
)

# ============================================================
# CLIENTES
# ============================================================

st.divider()

st.subheader("CLIENTES")

st.dataframe(
    clients,
    width="stretch"
)

# ============================================================
# SOLICITAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

st.divider()

st.subheader("SOLICITAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES")

st.dataframe(
    requests,
    width="stretch"
)

# ============================================================
# PAGAMENTOS
# ============================================================

st.divider()

st.subheader("PAGAMENTOS")

st.dataframe(
    payments,
    width="stretch"
)

# ============================================================
# LOGS OPERACIONAIS
# ============================================================

st.divider()

st.subheader("LOGS OPERACIONAIS")

if len(logs) > 0:
    pass

    logs = logs.sort_values(
        by="id",
        ascending=False
    )

st.dataframe(
    logs,
    width="stretch"
)

# ============================================================
# RODAPÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°
# ============================================================

st.divider()

st.caption(
    "IOTEC ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ LIVE OPERATIONAL GOVERNANCE"
)

# ============================================================
# FIM
# ============================================================


