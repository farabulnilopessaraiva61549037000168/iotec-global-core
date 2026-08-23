# ==========================================================
# C:\IOTEC\CONTACT_DISCOVERY_WORKER.py
# IOTEC CONTACT DISCOVERY WORKER
# ==========================================================

import sys
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CRMDB

QUEUE = ROOT / "CONTACT_DISCOVERY_QUEUE.json"

if not QUEUE.exists():

    print("="*70)
    print("CONTACT DISCOVERY WORKER")
    print("="*70)
    print()
    print("Fila nÃƒÂ£o encontrada.")
    sys.exit()

with open(QUEUE, encoding="utf-8") as f:

    fila = json.load(f)

crm = CRMDB.load()

indice = {}

for empresa in crm:

    indice[empresa["company_name"]] = empresa

processadas = 0

for tarefa in fila:

    nome = tarefa["company_name"]

    if nome not in indice:
        continue

    registro = indice[nome]

    if not registro.get("website"):
        registro["website"] = "PENDENTE"

    if not registro.get("email"):
        registro["email"] = "PENDENTE"

    if not registro.get("phone"):
        registro["phone"] = "PENDENTE"

    if not registro.get("linkedin"):
        registro["linkedin"] = "PENDENTE"

    registro["contact_status"] = "AGUARDANDO_COLETOR"

    registro["updated_at"] = str(datetime.now())

    tarefa["status"] = "PROCESSADO"

    tarefa["processed_at"] = str(datetime.now())

    processadas += 1

CRMDB.save(crm)

with open(

    QUEUE,

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
print("CONTACT DISCOVERY WORKER")
print("="*70)
print()

print("Empresas CRM...........",len(crm))
print("Fila...................",len(fila))
print("Processadas............",processadas)

print()

print("CRM atualizado.")

print("Fila atualizada.")

print()

print("STATUS")

print("AGUARDANDO COLETOR REAL DE CONTATOS")

