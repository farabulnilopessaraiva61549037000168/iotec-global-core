# ======================================================================================
# 100_CORPORATE_DATA_CATALOG.py
# IOTEC CORPORATE DATA CATALOG
# ======================================================================================

import os
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

IGNORAR = {

    "node_modules",
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "env",
    "Lib",
    "Scripts",
    "site-packages",
    "dist",
    "build",
    "cache",
    ".idea",
    ".vscode"

}

PALAVRAS = {

    "COMERCIAL":[
        "PRODUCT",
        "CATALOG",
        "REVENUE",
        "PIPELINE",
        "COMMERCIAL",
        "CLIENT",
        "CUSTOMER",
        "SALES",
        "PROPOSAL"
    ],

    "CONHECIMENTO":[
        "KNOWLEDGE",
        "LIBRARY",
        "GENOME",
        "WAREHOUSE",
        "ACADEMIC",
        "CODE"
    ],

    "INFRAESTRUTURA":[
        "INFRA",
        "EXECUTION",
        "RUNTIME",
        "DEPLOY",
        "GRID",
        "SERVER",
        "STATUS"
    ],

    "FINANCEIRO":[
        "FINANCIAL",
        "PAYPAL",
        "PAYMENT",
        "CAIXA",
        "REVENUE"
    ],

    "INTELIGENCIA":[
        "DISCOVERY",
        "INTELLIGENCE",
        "NEURAL",
        "BRAIN",
        "OPPORTUNITY",
        "LEARNING"
    ],

    "OPERACIONAL":[
        "CONTROL",
        "LEDGER",
        "AUDIT",
        "REPORT",
        "MISSION",
        "ENGINE"
    ]

}

print("="*90)
print("IOTEC CORPORATE DATA CATALOG")
print("CATÃƒÂLOGO CORPORATIVO DE DADOS")
print("="*90)
print()

catalogo = {

    "generated_at":datetime.now().isoformat(),
    "assets":[]

}

contagem = {}

for pasta, diretorios, arquivos in os.walk(ROOT):

    diretorios[:] = [d for d in diretorios if d not in IGNORAR]

    for arquivo in arquivos:

        if not arquivo.lower().endswith(".json"):
            continue

        if not arquivo.upper().startswith("IOTEC"):
            continue

        caminho = os.path.join(pasta,arquivo)

        categoria="GERAL"

        nome=arquivo.upper()

        for grupo,palavras in PALAVRAS.items():

            for palavra in palavras:

                if palavra in nome:

                    categoria=grupo
                    break

            if categoria!="GERAL":
                break

        estrelas=3

        if categoria in ["COMERCIAL","INTELIGENCIA"]:
            estrelas=5

        elif categoria in ["CONHECIMENTO","INFRAESTRUTURA"]:
            estrelas=4

        tamanho=os.path.getsize(caminho)

        catalogo["assets"].append({

            "arquivo":arquivo,
            "categoria":categoria,
            "prioridade":estrelas,
            "bytes":tamanho,
            "path":caminho

        })

        contagem[categoria]=contagem.get(categoria,0)+1

catalogo["assets"].sort(

    key=lambda x:(

        -x["prioridade"],
        x["categoria"],
        x["arquivo"]

    )

)

with open(

    "IOTEC_CORPORATE_DATA_CATALOG.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        catalogo,

        f,

        indent=4,

        ensure_ascii=False

    )

print("ATIVOS CORPORATIVOS")
print("="*90)
print()

print("Total :",len(catalogo["assets"]))
print()

print("POR CATEGORIA")
print("-"*90)

for k in sorted(contagem):

    print(f"{k:20}",contagem[k])

print()

print("="*90)
print("TOP 30")
print("="*90)
print()

for item in catalogo["assets"][:30]:

    estrelas="Ã¢Ëœâ€¦"*item["prioridade"]

    print(

        f"{estrelas:5} "

        f"{item['categoria']:18} "

        f"{item['arquivo']}"

    )

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CORPORATE_DATA_CATALOG.json")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("O Kernel passa")
print("a conhecer")
print("somente")
print("o patrimÃƒÂ´nio")
print("corporativo")
print("da IOTEC.")
print()

print("Bibliotecas externas")
print("deixam de")
print("interferir")
print("na inteligÃƒÂªncia")
print("corporativa.")
print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CATÃƒÂLOGO CORPORATIVO OPERACIONAL.")


