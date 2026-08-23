import sys
from pathlib import Path
from datetime import datetime

ENTERPRISE = Path(r"C:\IOTEC\enterprise")

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import CompanyDB, PipelineDB

ETAPAS = [
    "NOVO_LEAD",
    "QUALIFICACAO",
    "PRIMEIRO_CONTATO",
    "DIAGNOSTICO",
    "PROPOSTA",
    "NEGOCIACAO",
    "CONTRATO",
    "CLIENTE"
]

companies = CompanyDB.load()
pipeline = PipelineDB.load()

existentes = {x.get("company_name") for x in pipeline}

novos = 0

for company in companies:

    nome = company.get("company_name")

    if not nome:
        continue

    if nome in existentes:
        continue

    pipeline.append({

        "company_name": nome,

        "pipeline": ETAPAS[0],

        "history":[
            {
                "stage":ETAPAS[0],
                "date":str(datetime.now())
            }
        ],

        "created_at":str(datetime.now()),
        "updated_at":str(datetime.now())

    })

    novos += 1

PipelineDB.save(pipeline)

print("="*70)
print("PIPELINE INITIALIZER")
print("="*70)
print()
print("Empresas :",len(companies))
print("Pipeline :",len(pipeline))
print("Novos    :",novos)


