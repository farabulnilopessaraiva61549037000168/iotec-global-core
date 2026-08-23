# ==============================================================================
# 121_CONTACT_DISCOVERY_ENGINE.py
# IOTEC CONTACT DISCOVERY ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CONTACT DISCOVERY ENGINE")
print("MOTOR DE DESCOBERTA DE CONTATOS")
print("="*90)
print()

ARQUIVO="IOTEC_COMPANY_DATABASE.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("Banco corporativo nÃƒÂ£o encontrado.")
    raise SystemExit()

empresas=banco.get("empresas",[])

print("="*90)
print("EMPRESAS")
print("="*90)
print()

for empresa in empresas:

    empresa["site_status"]="PENDENTE"
    empresa["telefone_status"]="PENDENTE"
    empresa["email_status"]="PENDENTE"
    empresa["linkedin_status"]="PENDENTE"
    empresa["responsavel_status"]="PENDENTE"

    empresa["pipeline"]="CONTACT_DISCOVERY"

    print("="*70)
    print(empresa["empresa"])
    print()

    print("Site.............",empresa["site_status"])
    print("Telefone.........",empresa["telefone_status"])
    print("Email............",empresa["email_status"])
    print("LinkedIn.........",empresa["linkedin_status"])
    print("ResponsÃƒÂ¡vel......",empresa["responsavel_status"])
    print()

saida={

    "generated_at":datetime.now().isoformat(),

    "total":len(empresas),

    "empresas":empresas

}

with open(

    "IOTEC_CONTACT_DISCOVERY_DATABASE.json",

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
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Toda empresa")
print("deve possuir")
print("informaÃƒÂ§ÃƒÂµes")
print("de contato.")

print()

print("O Kernel")
print("prepara")
print("a estrutura")
print("para futuras")
print("integraÃƒÂ§ÃƒÂµes.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_CONTACT_DISCOVERY_DATABASE.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CONTACT DISCOVERY OPERACIONAL.")

