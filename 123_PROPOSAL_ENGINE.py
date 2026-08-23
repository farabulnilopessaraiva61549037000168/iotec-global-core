import json
import os
from datetime import datetime

INPUT = "IOTEC_CRM_DATABASE.json"
OUTPUT = "IOTEC_PROPOSAL_DATABASE.json"

TEMPLATES = {

    "ENGENHARIA": {
        "proposal": "DiagnÃƒÂ³stico + Dashboard Executivo + Business Intelligence",
        "estimated_value": 8500
    },

    "EDUCACAO": {
        "proposal": "Portal Corporativo + Dashboard Educacional",
        "estimated_value": 6200
    },

    "SAUDE": {
        "proposal": "Business Intelligence + Monitoramento EstratÃƒÂ©gico",
        "estimated_value": 12000
    },

    "INDUSTRIA": {
        "proposal": "Auditoria TecnolÃƒÂ³gica + BI Industrial",
        "estimated_value": 18000
    },

    "GERAL": {
        "proposal": "DiagnÃƒÂ³stico Digital",
        "estimated_value": 3500
    }

}

if not os.path.exists(INPUT):
    print("CRM inexistente.")
    raise SystemExit()

with open(INPUT, "r", encoding="utf-8") as f:
    crm = json.load(f)

proposals = []

for lead in crm:

    segmento = lead["segment"].upper()

    modelo = TEMPLATES.get(
        segmento,
        TEMPLATES["GERAL"]
    )

    proposals.append({

        "company": lead["company"],

        "segment": segmento,

        "proposal": modelo["proposal"],

        "estimated_value": modelo["estimated_value"],

        "status": "AGUARDANDO ENVIO",

        "pipeline": "PROPOSTA",

        "created_at": datetime.now().isoformat()

    })

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        proposals,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*90)
print("IOTEC PROPOSAL ENGINE")
print("="*90)
print()

print("PROPOSTAS GERADAS :",len(proposals))
print()

print("="*90)
print("TOP 10")
print("="*90)
print()

total = 0

for p in proposals[:10]:

    total += p["estimated_value"]

    print(p["company"])
    print("Segmento :",p["segment"])
    print("Produto :",p["proposal"])
    print("Valor Estimado : R$",p["estimated_value"])
    print()

print("="*90)
print("POTENCIAL COMERCIAL")
print("="*90)
print()

print("Valor Total Estimado : R$",total)

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Cada oportunidade")
print("passa a possuir")
print("uma proposta")
print("comercial inicial.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("Todas as empresas")
print("receberam")
print("uma proposta")
print("compatÃƒÂ­vel")
print("com seu")
print("segmento.")

print()

print("A prÃƒÂ³xima etapa")
print("ÃƒÂ© localizar")
print("os canais")
print("de contato")
print("e iniciar")
print("o relacionamento.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Propostas :",len(proposals))
print("Data :",datetime.now())

print()

print("PROPOSAL ENGINE OPERACIONAL.")

