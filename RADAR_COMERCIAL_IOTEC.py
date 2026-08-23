import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import pandas as pd

ARQUIVO = r"C:\IOTEC\empresas.csv"

print("")
print("===================================")
print("RADAR COMERCIAL IOTEC")
print("===================================")
print("")

df = pd.read_csv(ARQUIVO)

def score_empresa(row):
    pass

    score = 0

    setor = str(row["setor"]).upper()
    funcionarios = int(row["funcionarios"])

    if funcionarios > 20:
        score += 10

    if funcionarios > 100:
        score += 20

    if "INDUSTR" in setor:
        score += 20

    if "SAUDE" in setor:
        score += 15

    if "CONTABIL" in setor:
        score += 10

    return score

df["lead_score"] = df.apply(
    score_empresa,
    axis=1
)

df = df.sort_values(
    by="lead_score",
    ascending=False
)

saida = r"C:\IOTEC\fila_comercial.csv"

df.to_csv(
    saida,
    index=False
)

print("EMPRESAS ANALISADAS:", len(df))
print("")
print("TOP OPORTUNIDADES")
print("")

for _, row in df.head(10).iterrows():
    pass

    print(
        f"{row['empresa']} | "
        f"{row['setor']} | "
        f"SCORE={row['lead_score']}"
    )

print("")
print("ARQUIVO GERADO:")
print(saida)
print("")




