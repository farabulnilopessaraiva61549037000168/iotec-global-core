import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

print("=" * 70)
print("X27 CONNECTOR SETUP")
print("=" * 70)
print()

configs = {

    "GOOGLE_MAPS_API_KEY":
        os.getenv("GOOGLE_MAPS_API_KEY"),

    "GOOGLE_PLACES_API_KEY":
        os.getenv("GOOGLE_PLACES_API_KEY"),

    "SMTP_SERVER":
        os.getenv("SMTP_SERVER"),

    "SMTP_USER":
        os.getenv("SMTP_USER"),

    "SMTP_PASSWORD":
        os.getenv("SMTP_PASSWORD"),

    "WHATSAPP_TOKEN":
        os.getenv("WHATSAPP_TOKEN")

}

online = 0
offline = 0

for nome, valor in configs.items():

    if valor:

        status = "ONLINE"
        online += 1

    else:

        status = "OFFLINE"
        offline += 1

    print(f"{nome:30} {status}")

print()
print("=" * 70)

print("ONLINE :", online)
print("OFFLINE:", offline)

print()
print("=" * 70)
print("ANALISE")
print("=" * 70)

if offline == len(configs):

    print("""
NENHUMA INTEGRACAO CONFIGURADA

O nÃƒÂºcleo estÃƒÂ¡ operando apenas
com recursos locais.

PrÃƒÂ³ximo passo:

1 - Google Maps
2 - Google Places
3 - Email
4 - WhatsApp
""")

elif offline > 0:

    print("""
EXISTEM INTEGRACOES PARCIAIS

Completar configuracao restante.
""")

else:

    print("""
TODAS AS INTEGRACOES ESTAO
CONFIGURADAS.

O nÃƒÂºcleo pode iniciar operacoes
externas.
""")

print()
print("=" * 70)
print("FIM")
print("=" * 70)



