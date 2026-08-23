import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC INVENTORY ENGINE
# ==========================================================

import os
import json
from datetime import datetime

print("=" * 70)
print("IOTEC INVENTORY ENGINE")
print("=" * 70)

DATA_DIR = "."

inventario = []

print()
print("DATA:")
print(datetime.now())

print()
print("=" * 70)
print("ESCANEANDO ECOSSISTEMA")
print("=" * 70)

for raiz, diretorios, arquivos in os.walk(DATA_DIR):

    for arquivo in arquivos:

        caminho = os.path.join(raiz, arquivo)

        try:
            tamanho = os.path.getsize(caminho)

        except:
            tamanho = 0

        extensao = os.path.splitext(arquivo)[1].upper()

        tipo = "OUTROS"

        if extensao == ".PY":
            tipo = "SCRIPT"

        elif extensao in [".HTML", ".HTM"]:
            tipo = "INTERFACE"

        elif extensao == ".JSON":
            tipo = "DATABASE"

        elif extensao == ".CSV":
            tipo = "DADOS"

        elif extensao == ".DOCX":
            tipo = "DOCUMENTO"

        elif extensao == ".PDF":
            tipo = "PDF"

        registro = {

            "nome": arquivo,
            "caminho": caminho,
            "tipo": tipo,
            "tamanho_kb": round(tamanho / 1024, 2),
            "status": "NAO_CLASSIFICADO",
            "gera_receita": False,
            "prontidao": 0,
            "data_inventario": str(datetime.now())

        }

        inventario.append(registro)

print()
print("ARQUIVOS ENCONTRADOS:", len(inventario))

# ==========================================================
# RESUMO
# ==========================================================

scripts = len([x for x in inventario if x["tipo"] == "SCRIPT"])
interfaces = len([x for x in inventario if x["tipo"] == "INTERFACE"])
databases = len([x for x in inventario if x["tipo"] == "DATABASE"])
documentos = len([x for x in inventario if x["tipo"] == "DOCUMENTO"])

print()
print("=" * 70)
print("RESUMO")
print("=" * 70)

print("SCRIPTS:", scripts)
print("INTERFACES:", interfaces)
print("DATABASES:", databases)
print("DOCUMENTOS:", documentos)

# ==========================================================
# EXPORTACAO
# ==========================================================

saida = {

    "data": str(datetime.now()),
    "total_ativos": len(inventario),
    "inventario": inventario

}

with open(
    "IOTEC_MASTER_INVENTORY.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        saida,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("=" * 70)
print("ARQUIVO GERADO")
print("=" * 70)

print("IOTEC_MASTER_INVENTORY.json")

print()
print("=" * 70)
print("PROXIMA MISSAO")
print("=" * 70)

print("""
CLASSIFICAR ATIVOS

IDENTIFICAR:
- O QUE GERA RECEITA
- O QUE ESTA ABANDONADO
- O QUE ESTA PRONTO
- O QUE PRECISA EVOLUIR

TRANSFORMAR ARQUIVOS
EM PATRIMONIO DIGITAL
""")

print()
print("INVENTORY ENGINE ATIVO")



