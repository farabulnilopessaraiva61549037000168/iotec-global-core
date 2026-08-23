# ==============================================================================
# 122_CONTACT_ENRICHMENT_ENGINE.py
# IOTEC CONTACT ENRICHMENT ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CONTACT ENRICHMENT ENGINE")
print("MOTOR DE ENRIQUECIMENTO DE CONTATOS")
print("="*90)
print()

ARQUIVO="IOTEC_CONTACT_DISCOVERY_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("Base de contatos nÃƒÂ£o encontrada.")
    raise SystemExit()

empresas=banco.get("empresas",[])

print("="*90)
print("ANÃƒÂLISE")
print("="*90)
print()

for empresa in empresas:

    if not empresa["site"]:
        empresa["site_status"]="AGUARDANDO BUSCA"

    if not empresa["telefone"]:
        empresa["telefone_status"]="AGUARDANDO BUSCA"

    if not empresa["email"]:
        empresa["email_status"]="AGUARDANDO BUSCA"

    if not empresa["linkedin"]:
        empresa["linkedin_status"]="AGUARDANDO BUSCA"

    empresa["responsavel_status"]="AGUARDANDO IDENTIFICAÃƒâ€¡ÃƒÆ'O"

    empresa["pipeline"]="CONTACT_ENRICHMENT"

    print("="*70)
    print(empresa["empresa"])
    print()
    print("Site...............",empresa["site_status"])
    print("Telefone...........",empresa["telefone_status"])
    print("Email..............",empresa["email_status"])
    print("LinkedIn...........",empresa["linkedin_status"])
    print("ResponsÃƒÂ¡vel........",empresa["responsavel_status"])
    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CONTACT_ENRICHMENT_ENGINE",

    "version":"1.0",

    "total":len(empresas),

    "empresas":empresas

}

with open(

    "IOTEC_CONTACT_ENRICHMENT_DATABASE.json",

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
print("PRÃƒâ€œXIMOS AGENTES")
print("="*90)
print()

print("SITE_AGENT .............. Buscar site oficial")
print("PHONE_AGENT ............. Buscar telefone")
print("EMAIL_AGENT ............. Buscar e-mail")
print("LINKEDIN_AGENT .......... Buscar LinkedIn")
print("DECISION_AGENT .......... Identificar decisor")
print("CRM_AGENT ............... Registrar relacionamento")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Empresas..............",len(empresas))
print("Pipeline.............. CONTACT_ENRICHMENT")
print("Arquivo............... IOTEC_CONTACT_ENRICHMENT_DATABASE.json")
print()
print("CONTACT ENRICHMENT OPERACIONAL.")

