# ==========================================================
# C:\IOTEC\DEDUPLICATE_CRM.py
# ==========================================================

import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CRMDB


crm = CRMDB.load()

print("=" * 70)
print("IOTEC CRM DEDUPLICATOR")
print("=" * 70)
print()

print("Registros Originais :", len(crm))

unicos = {}

duplicados = 0

for registro in crm:

    nome = registro.get("company_name", "").strip()

    if nome == "":
        continue

    if nome not in unicos:

        registro["updated_at"] = str(datetime.now())

        unicos[nome] = registro

    else:

        antigo = unicos[nome]

        # mantÃƒÂ©m o registro mais completo

        for campo in registro:

            valor = registro.get(campo)

            if valor not in ("", None, [], {}):

                antigo[campo] = valor

        antigo["updated_at"] = str(datetime.now())

        duplicados += 1


crm_limpo = sorted(

    list(unicos.values()),

    key=lambda x: x["company_name"]

)

CRMDB.save(crm_limpo)

print()

print("Duplicados Removidos :", duplicados)

print("CRM Final............", len(crm_limpo))

print()

print("STATUS")

print("CRM CONSOLIDADO COM SUCESSO")

print()

