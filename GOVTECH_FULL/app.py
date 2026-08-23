import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st

from engine import analisar_cenario, recomendar_plano

from dossie import gerar_dossie

from pagamentos import gerar_links_pagamento



st.set_page_config(layout="wide")

st.title("IOTEC GovTech Premium")



# Inputs

prof = st.number_input("Professores", value=100)

sal = st.number_input("SalÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio atual", value=2500)

piso = st.number_input("Piso", value=3500)



impacto = prof * (piso - sal)

percentual = ((piso - sal) / sal) * 100



dados = {

    "impacto": impacto,

    "percentual": percentual,

    "risco": "ALTO" if percentual > 20 else "MODERADO",

    "cenarios": 3

}



score = analisar_cenario(dados)

plano = recomendar_plano(score)



st.subheader("Plano recomendado")

st.write(plano)



if st.button("Gerar DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª"):
    pass

    gerar_dossie(dados)

    st.success("DossiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª gerado em C:\\IOTEC")



links = gerar_links_pagamento(plano["valor"])



st.subheader("Pagamento")

st.markdown(f"[Pagar via PayPal]({links['paypal']})")

st.write("Pix:", links["pix"])




