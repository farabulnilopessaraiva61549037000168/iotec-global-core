import sys
from pathlib import Path
from datetime import datetime
import json

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CRMDB

crm = CRMDB.load()

fila = []

for empresa in crm:

    if (
        empresa.get("website")
        and empresa.get("email")
        and empresa.get("phone")
        and empresa.get("linkedin")
    ):
        continue

    fila.append({

        "company_name": empresa["company_name"],

        "website": empresa.get("website",""),

        "email": empresa.get("email",""),

        "phone": empresa.get("phone",""),

        "linkedin": empresa.get("linkedin",""),

        "priority":"CRITICA",

        "status":"PENDENTE",

        "created_at":str(datetime.now())

    })

arquivo = ROOT / "CONTACT_DISCOVERY_QUEUE.json"

with open(
    arquivo,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        fila,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*70)
print("CONTACT DISCOVERY SERVICE")
print("="*70)
print()

print("Empresas no CRM.......",len(crm))
print("Fila Gerada...........",len(fila))
print()

print("Arquivo")
print(arquivo)

