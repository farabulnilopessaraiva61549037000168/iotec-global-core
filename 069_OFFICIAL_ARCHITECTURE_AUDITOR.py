# ==========================================================
# 069_OFFICIAL_ARCHITECTURE_AUDITOR.py
# IOTEC OFFICIAL ARCHITECTURE AUDITOR
# ==========================================================

import os
import json

ROOT = r"C:\IOTEC"

CONSTITUTION = os.path.join(ROOT, "IOTEC_CONSTITUTION.json")

print("="*70)
print("IOTEC OFFICIAL ARCHITECTURE AUDITOR")
print("="*70)
print()

if not os.path.exists(CONSTITUTION):
    print("ConstituiÃƒÂ§ÃƒÂ£o nÃƒÂ£o encontrada.")
    raise SystemExit

with open(CONSTITUTION, encoding="utf-8") as f:
    CONST = json.load(f)

IGNORE = {
    "BACKUP",
    "ENCODING_BACKUP",
    "LABORATORIO",
    "DUPLICADOS",
    "FROZEN",
    "venv",
    "__pycache__"
}

print("ARQUITETURA OFICIAL")
print("="*70)
print()

for nome, arquivo in CONST["architecture"].items():

    encontrados=[]

    for raiz,pastas,files in os.walk(ROOT):

        pastas[:] = [
            p for p in pastas
            if p not in IGNORE
        ]

        if arquivo in files:
            encontrados.append(os.path.join(raiz,arquivo))

    print(nome.upper())

    if len(encontrados)==0:

        print("STATUS : AUSENTE")

    elif len(encontrados)==1:

        print("STATUS : OK")
        print(encontrados[0])

    else:

        print("STATUS : DUPLICADO")

        for e in encontrados:
            print(" -",e)

    print("-"*60)

print()
print("="*70)
print("PROCURA POR INTEGRAÃƒâ€¡Ãƒâ€¢ES OFICIAIS")
print("="*70)
print()

PALAVRAS = {

    "Google Maps":[
        "googlemaps",
        "maps.googleapis",
        "places",
        "place_id"
    ],

    "WhatsApp":[
        "whatsapp",
        "wa.me",
        "phone_number_id",
        "graph.facebook"
    ],

    "LinkedIn":[
        "linkedin"
    ],

    "PayPal":[
        "paypal",
        "checkout",
        "capture",
        "webhook"
    ],

    "Email":[
        "smtp",
        "imap",
        "proton",
        "mail"
    ]

}

for titulo,lista in PALAVRAS.items():

    print()
    print(titulo)
    print("-"*50)

    total=0

    for raiz,pastas,files in os.walk(ROOT):

        pastas[:] = [
            p for p in pastas
            if p not in IGNORE
        ]

        for arq in files:

            if not arq.endswith(".py"):
                continue

            caminho=os.path.join(raiz,arq)

            try:

                texto=open(
                    caminho,
                    encoding="utf-8",
                    errors="ignore"
                ).read().lower()

            except:
                continue

            for palavra in lista:

                if palavra.lower() in texto:

                    total+=1
                    print(arq)

                    break

    print()
    print("Arquivos encontrados:",total)

print()
print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia passa")
print("a conhecer apenas")
print("a arquitetura")
print("oficial da empresa.")



