# ==========================================================
# 074_PAYPAL_OFFICIAL_CONNECTOR.py
# IOTEC PAYPAL OFFICIAL CONNECTOR
# ==========================================================

import os
import re

ROOT = r"C:\IOTEC"

IGNORE = {
    "venv",
    "__pycache__",
    "BACKUP",
    "ENCODING_BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "FROZEN"
}

PADROES = {

    "CREATE_ORDER":[
        "create_order",
        "/create-order",
        "checkout"
    ],

    "CAPTURE":[
        "capture",
        "/capture"
    ],

    "WEBHOOK":[
        "webhook",
        "PAYMENT.CAPTURE.COMPLETED",
        "CHECKOUT.ORDER.APPROVED"
    ],

    "REQUESTS":[
        "requests.post",
        "requests.get"
    ],

    "DATABASE":[
        "sqlite3",
        "cursor.execute"
    ],

    "FLASK":[
        "@app.route",
        "Flask("
    ]

}

print("="*70)
print("IOTEC PAYPAL OFFICIAL CONNECTOR")
print("="*70)
print()

candidatos=[]

for raiz,pastas,arquivos in os.walk(ROOT):

    pastas[:] = [p for p in pastas if p not in IGNORE]

    for arq in arquivos:

        if not arq.endswith(".py"):
            continue

        caminho=os.path.join(raiz,arq)

        try:

            texto=open(
                caminho,
                encoding="utf-8",
                errors="ignore"
            ).read()

        except:
            continue

        score=0

        evidencias=[]

        texto_lower=texto.lower()

        for grupo,palavras in PADROES.items():

            qtd=0

            for p in palavras:

                qtd+=texto_lower.count(p.lower())

            if qtd:

                evidencias.append((grupo,qtd))
                score+=qtd*10

        if score>0:

            candidatos.append(

                (
                    score,
                    arq,
                    caminho,
                    evidencias
                )

            )

candidatos.sort(reverse=True)

print("TOP 20")
print()

for score,arquivo,caminho,evidencias in candidatos[:20]:

    print("="*60)
    print(arquivo)
    print("Score :",score)
    print()

    for grupo,qtd in evidencias:

        print(f"{grupo:<15} {qtd}")

print()

print("="*70)
print("CONECTOR MAIS FORTE")
print("="*70)
print()

if candidatos:

    score,arquivo,caminho,evidencias=candidatos[0]

    print("Arquivo :")
    print(arquivo)
    print()

    print("Local :")
    print(caminho)
    print()

    print("Score :",score)

else:

    print("Nenhum candidato encontrado.")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia inicia")
print("a eleiÃƒÂ§ÃƒÂ£o")
print("do Conector")
print("Oficial do PayPal.")


