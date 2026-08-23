import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import datetime

import pandas as pd

import plotly.graph_objects as go



from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.pagesizes import A4

from reportlab.lib.units import cm



# =========================

# CONFIG

# =========================



BASE_DIR = "C:\\IOTEC\\DOSSIER_IOTEC"

os.makedirs(BASE_DIR, exist_ok=True)



# =========================

# DADOS (EXEMPLO)

# =========================



dados = {

    "municipio": "Ibicuitinga",

    "professores": 100,

    "salario": 2500,

    "piso": 3500

}



# =========================

# CÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLCULOS

# =========================



folha_atual = dados["professores"] * dados["salario"]

folha_nova = dados["professores"] * dados["piso"]

aumento_pct = (folha_nova - folha_atual) / folha_atual * 100



# =========================

# PASTA FINAL

# =========================



timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")

PASTA = os.path.join(BASE_DIR, f"DOSSIE_{timestamp}")

os.makedirs(PASTA, exist_ok=True)



# =========================

# GRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂFICO PREMIUM

# =========================



grafico_path = os.path.join(PASTA, "grafico.png")



fig = go.Figure()

fig.add_trace(go.Bar(

    x=["Atual", "Projetado"],

    y=[folha_atual, folha_nova],

    marker_color=["#1E6FFF", "#00C48C"]

))

fig.update_layout(

    title="Impacto Financeiro",

    plot_bgcolor="#0B0F14",

    paper_bgcolor="#0B0F14",

    font=dict(color="white")

)



fig.write_image(grafico_path, width=1400, height=800)



# =========================

# EXCEL

# =========================



excel_path = os.path.join(PASTA, "analise.xlsx")



df = pd.DataFrame({

    "Indicador": ["Folha Atual", "Folha Projetada", "Aumento (%)"],

    "Valor": [folha_atual, folha_nova, aumento_pct]

})



df.to_excel(excel_path, index=False)



# =========================

# TEXTO PROFISSIONAL

# =========================



texto = f"""

Diante do cenÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio analisado, observa-se que a adequaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o ao piso salarial implica aumento relevante da despesa com pessoal.



A folha atual apresenta o valor de R$ {folha_atual:,.2f}, enquanto a projeÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o indica R$ {folha_nova:,.2f}, representando variaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de {aumento_pct:.2f}%.



Nesse contexto, recomenda-se a adoÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de planejamento gradual, com vistas ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡  mitigaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o dos impactos financeiros e preservaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o do equilÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­brio orÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡amentÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio.

"""



# =========================

# PDF PROFISSIONAL

# =========================



pdf_path = os.path.join(PASTA, "relatorio.pdf")



doc = SimpleDocTemplate(

    pdf_path,

    pagesize=A4,

    leftMargin=3*cm,

    rightMargin=2*cm,

    topMargin=3*cm,

    bottomMargin=2*cm

)



styles = getSampleStyleSheet()



estilo = ParagraphStyle(

    name="Justificado",

    parent=styles["Normal"],

    fontName="Times-Roman",

    fontSize=12,

    leading=18,

    alignment=4,

    firstLineIndent=1.25*cm

)



story = []



story.append(Paragraph("RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO TÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°CNICO IOTEC", styles["Title"]))

story.append(Spacer(1, 20))



for p in texto.strip().split("\n\n"):
    pass

    story.append(Paragraph(p, estilo))

    story.append(Spacer(1, 12))



story.append(Image(grafico_path, width=500, height=300))



doc.build(story)



# =========================

# CHECKLIST

# =========================



itens = {

    "pdf": os.path.exists(pdf_path),

    "excel": os.path.exists(excel_path),

    "grafico": os.path.exists(grafico_path)

}



faltando = [k for k, v in itens.items() if not v]



print("\n===== RESULTADO =====")



if faltando:
    pass

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Faltando:", faltando)

else:
    pass

    print("ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ DossiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª completo gerado com sucesso")



print(f"\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â Pasta: {PASTA}")






