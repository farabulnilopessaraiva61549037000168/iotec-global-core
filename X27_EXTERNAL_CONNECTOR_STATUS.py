import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

print("=" * 70)
print("X27 EXTERNAL CONNECTOR STATUS")
print("=" * 70)

fontes = {

    "GOOGLE_MAPS_API": False,
    "GOOGLE_PLACES_API": False,
    "GOOGLE_SEARCH_API": False,
    "LINKEDIN_SOURCE": False,
    "INDUSTRY_DIRECTORY": False,
    "EMAIL_GATEWAY": False,
    "WHATSAPP_GATEWAY": False

}

for nome, status in fontes.items():

    print(
        f"{nome:25}",
        "ONLINE" if status else "OFFLINE"
    )

print()
print("=" * 70)
print("MISSAO")
print("=" * 70)

print("""
O nÃƒÂºcleo possui campanhas.

O nÃƒÂºcleo possui CRM.

O nÃƒÂºcleo possui pipeline.

O nÃƒÂºcleo ainda nÃƒÂ£o possui conectores
para descoberta automÃƒÂ¡tica.

PrÃƒÂ³ximo passo:
Conectar uma fonte externa real.
""")



