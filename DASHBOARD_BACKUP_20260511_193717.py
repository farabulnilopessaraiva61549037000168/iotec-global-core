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

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

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

# CONEXÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

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

# CABEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ALHO

# ============================================================



st.title("IOTEC LIVE CONTROL TOWER")



st.caption(

    "GovernanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡a Operacional Viva"

)



# ============================================================

# STATUS OPERACIONAL

# ============================================================



st.success("NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEO OPERACIONAL ONLINE")



# ============================================================

# MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°TRICAS

# ============================================================



col1, col2, col3, col4 = st.columns(4)



col1.metric(

    "CLIENTES",

    len(clients)

)



col2.metric(

    "SOLICITAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES",

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

# SOLICITAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# ============================================================



st.divider()



st.subheader("SOLICITAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES")



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

# RODAPÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°

# ============================================================



st.divider()



st.caption(

    "IOTEC ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ LIVE OPERATIONAL GOVERNANCE"

)



# ============================================================

# FIM

# ============================================================






