import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 SUPPLIER NETWORK
# ============================================================

from datetime import datetime

FORNECEDORES = [

    {
        "nome": "COMPANHIA_REGIONAL_AGUA",
        "tipo": "AGUA",
        "capacidade": "500000 L/DIA",
        "status": "ATIVO"
    },

    {
        "nome": "HOSPITAL_PARCEIRO_REGIONAL",
        "tipo": "SAUDE",
        "capacidade": "120 LEITOS",
        "status": "ATIVO"
    },

    {
        "nome": "OPERADORA_SATELITAL",
        "tipo": "COMUNICACAO",
        "capacidade": "LINK_EMERGENCIAL",
        "status": "ATIVO"
    }

]

print("\n================================================")
print("X27 SUPPLIER NETWORK")
print("================================================")
print(f"DATA : {datetime.now()}")

for fornecedor in FORNECEDORES:
    pass

    print("\n------------------------------------------------")

    print(f"NOME       : {fornecedor['nome']}")

    print(f"TIPO       : {fornecedor['tipo']}")

    print(f"CAPACIDADE : {fornecedor['capacidade']}")

    print(f"STATUS     : {fornecedor['status']}")

print("\n================================================")
print("REDE DE FORNECIMENTO OPERACIONAL")
print("================================================")


