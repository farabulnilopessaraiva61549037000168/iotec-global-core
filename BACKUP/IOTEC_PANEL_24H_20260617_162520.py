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



st.title("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã¢â‚¬Å¡  IOTEC - Sistema Vivo 24h")



def carregar():
    pass

    try:
        pass

        with open(ARQUIVO, "r") as f:
            pass

            return json.load(f)

    except:
        pass

        return {"entradas": [], "saidas": [], "bloqueios": []}



dados = carregar()



col1, col2, col3 = st.columns(3)



with col1:
    pass

    st.markdown("### ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ Entradas")

    for e in dados["entradas"][-5:]:
        pass

        st.write(e)



with col2:
    pass

    st.markdown("### ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ SaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­das")

    for s in dados["saidas"][-5:]:
        pass

        st.write(s)



with col3:
    pass

    st.markdown("### ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´ Bloqueios")

    for b in dados["bloqueios"][-5:]:
        pass

        st.write(b)



st.metric("Total Entradas", len(dados["entradas"]))



time.sleep(5)

st.rerun()




