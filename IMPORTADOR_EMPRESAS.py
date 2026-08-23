import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import pandas as pd
import os

BASE_PRINCIPAL = r"C:\IOTEC\empresas.csv"
BASE_IMPORTACAO = r"C:\IOTEC\novas_empresas.csv"

print("")
print("===================================")
print("IMPORTADOR DE EMPRESAS")
print("===================================")
print("")

if not os.path.exists(BASE_IMPORTACAO):
    pass

    print("ARQUIVO NAO ENCONTRADO:")
    print(BASE_IMPORTACAO)
    print("")
    exit()

if not os.path.exists(BASE_PRINCIPAL):
    pass

    print("BASE PRINCIPAL INEXISTENTE")
    print("")
    exit()

principal = pd.read_csv(BASE_PRINCIPAL)
novas = pd.read_csv(BASE_IMPORTACAO)

principal.columns = [c.lower().strip() for c in principal.columns]
novas.columns = [c.lower().strip() for c in novas.columns]

campos = [
    "empresa",
    "setor",
    "funcionarios",
    "cidade"
]

for campo in campos:
    pass

    if campo not in principal.columns:
        raise Exception(f"Campo ausente na base principal: {campo}")

    if campo not in novas.columns:
        raise Exception(f"Campo ausente na importacao: {campo}")

antes = len(principal)

base_final = pd.concat(
    [principal, novas],
    ignore_index=True
)

base_final = base_final.drop_duplicates(
    subset=["empresa"],
    keep="first"
)

depois = len(base_final)

adicionadas = depois - antes

base_final.to_csv(
    BASE_PRINCIPAL,
    index=False
)

print("EMPRESAS ANTES:", antes)
print("EMPRESAS DEPOIS:", depois)
print("NOVAS ADICIONADAS:", adicionadas)
print("")
print("BASE ATUALIZADA:")
print(BASE_PRINCIPAL)
print("")




