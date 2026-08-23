import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_pacote(dados, base_dir):
    pass

    df, f_atual, f_nova, pct = montar_dados(dados)



    img = f"{base_dir}/grafico.png"

    xls = f"{base_dir}/analise.xlsx"

    pdf = f"{base_dir}/relatorio.pdf"



    salvar_grafico(f_atual, f_nova, img)

    gerar_excel(df, xls)



    texto = montar_texto(f_atual, f_nova, pct)

    gerar_pdf(pdf, texto, img)



    return {"pdf": pdf, "excel": xls, "grafico": img}







