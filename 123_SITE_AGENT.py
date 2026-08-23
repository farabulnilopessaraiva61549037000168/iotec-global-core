# ==============================================================================
# 123_SITE_AGENT.py
# IOTEC SITE AGENT
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC SITE AGENT")
print("AGENTE DE DESCOBERTA DE SITES")
print("="*90)
print()

ARQUIVO="IOTEC_CONTACT_ENRICHMENT_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("Banco nÃƒÂ£o encontrado.")
    raise SystemExit()

empresas=banco.get("empresas",[])

print("="*90)
print("PROCESSAMENTO")
print("="*90)
print()

for empresa in empresas:

    print("="*70)
    print(empresa["empresa"])
    print()

    if empresa["site"]=="":

        empresa["site_status"]="BUSCA PENDENTE"

    else:

        empresa["site_status"]="LOCALIZADO"

    print("Site...........",empresa["site"])
    print("Status.........",empresa["site_status"])
    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"SITE_AGENT",

    "version":"1.0",

    "total":len(empresas),

    "empresas":empresas

}

with open(

    "IOTEC_SITE_DATABASE.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("FILA DOS PRÃƒâ€œXIMOS AGENTES")
print("="*90)
print()

print("124_PHONE_AGENT")
print("125_EMAIL_AGENT")
print("126_LINKEDIN_AGENT")
print("127_DECISION_AGENT")
print("128_CRM_AGENT")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("SITE AGENT OPERACIONAL.")

