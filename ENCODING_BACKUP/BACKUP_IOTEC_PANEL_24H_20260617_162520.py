import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st
import json
import time

ARQUIVO = "iotec_fluxo.json"

st.set_page_config(layout="wide")

st.title("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC - Sistema Vivo 24h")

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return {"entradas": [], "saidas": [], "bloqueios": []}

dados = carregar()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¥ Entradas")
    for e in dados["entradas"][-5:]:
        st.write(e)

with col2:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­das")
    for s in dados["saidas"][-5:]:
        st.write(s)

with col3:
    st.markdown("### ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Bloqueios")
    for b in dados["bloqueios"][-5:]:
        st.write(b)

st.metric("Total Entradas", len(dados["entradas"]))

time.sleep(5)
st.rerun()


