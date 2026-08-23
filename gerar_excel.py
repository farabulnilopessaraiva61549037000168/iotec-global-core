import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_excel(df, caminho):
    pass

    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        pass

        df.to_excel(writer, sheet_name="Resumo", index=False)







