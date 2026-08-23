# ==========================================================
# 070_OFFICIAL_CONNECTOR_DISCOVERY_ENGINE.py
# IOTEC OFFICIAL CONNECTOR DISCOVERY ENGINE
# ==========================================================

import os

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

TECNOLOGIAS = {

    "PAYPAL":[
        "paypal",
        "checkout",
        "capture",
        "webhook"
    ],

    "EMAIL":[
        "smtp",
        "imap",
        "email",
        "mail",
        "proton"
    ],

    "WHATSAPP":[
        "whatsapp",
        "wa.me",
        "phone_number_id",
        "graph.facebook"
    ],

    "GOOGLE_MAPS":[
        "googlemaps",
        "maps.googleapis",
        "places",
        "geocode",
        "place_id"
    ],

    "LINKEDIN":[
        "linkedin"
    ]

}

BONUS = {

    "route":5,

    "@app.route":10,

    "sqlite":5,

    "cursor.execute":5,

    "requests":10,

    "json":3,

    "post":5,

    "get":5,

    "api":8

}

print("="*70)
print("IOTEC OFFICIAL CONNECTOR DISCOVERY")
print("="*70)
print()

for tecnologia,palavras in TECNOLOGIAS.items():

    print("="*70)
    print(tecnologia)
    print("="*70)

    ranking=[]

    for raiz,pastas,arquivos in os.walk(ROOT):

        pastas[:] = [
            p for p in pastas
            if p not in IGNORE
        ]

        for arquivo in arquivos:

            if not arquivo.endswith(".py"):
                continue

            caminho=os.path.join(raiz,arquivo)

            try:

                texto=open(

                    caminho,

                    encoding="utf-8",

                    errors="ignore"

                ).read().lower()

            except:

                continue

            score=0

            for palavra in palavras:

                score += texto.count(palavra.lower())*5

            for bonus,valor in BONUS.items():

                score += texto.count(bonus.lower())*valor

            if score>0:

                ranking.append((score,arquivo,caminho))

    ranking.sort(reverse=True)

    if len(ranking)==0:

        print("Nenhum candidato encontrado.")
        print()

        continue

    print("TOP 10")
    print()

    for score,arquivo,caminho in ranking[:10]:

        print(f"{score:5}  {arquivo}")

    print()

    vencedor=ranking[0]

    print("CANDIDATO OFICIAL")
    print()

    print("Arquivo :",vencedor[1])

    print("Score   :",vencedor[0])

    print("Local   :",vencedor[2])

    print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia passa")
print("a conhecer")
print("os candidatos")
print("mais fortes")
print("para se tornarem")
print("Conectores Oficiais.")


