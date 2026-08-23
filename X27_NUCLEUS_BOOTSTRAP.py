import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

print("=" * 70)
print("X27 NUCLEUS BOOTSTRAP")
print("=" * 70)

if not os.path.exists(ENV_FILE):

    with open(ENV_FILE, "w", encoding="utf-8") as f:

        f.write(
"""GOOGLE_MAPS_API_KEY=

GOOGLE_PLACES_API_KEY=

SMTP_SERVER=

SMTP_USER=

SMTP_PASSWORD=

WHATSAPP_TOKEN=
"""
        )

    print("ARQUIVO CRIADO")
    print(ENV_FILE)

else:

    print("ARQUIVO JA EXISTE")

print()
print("PROXIMO PASSO")
print("CONFIGURAR CREDENCIAIS")



