import json
import os
from datetime import datetime

INPUT = "IOTEC_QUALIFIED_LEADS.json"
OUTPUT = "IOTEC_CONTACT_DATABASE.json"

# ==========================================================
# IOTEC CONTACT DISCOVERY ENGINE
# ==========================================================

if not os.path.exists(INPUT):

    print("Arquivo nÃƒÂ£o encontrado:")
    print(INPUT)
    raise SystemExit()

with open(INPUT, "r", encoding="utf-8") as f:

    leads = json.load(f)

contacts = []

for lead in leads:

    if not lead.get("potential_buyer", False):
        continue

    registro = {

        "company": lead["company"],

        "segment": lead["segment"],

        "city": lead.get("city",""),

        "lead_score": lead.get("lead_quality_score",0),

        "website": "",

        "email": "",

        "phone": "",

        "linkedin": "",

        "instagram": "",

        "facebook": "",

        "youtube": "",

        "contact_form": "",

        "commercial_contact": "",

        "status":"AGUARDANDO DESCOBERTA",

        "discovery_progress":0,

        "sources_checked":[

            "Website Oficial",

            "Google Business",

            "LinkedIn",

            "Instagram",

            "Facebook",

            "CatÃƒÂ¡logo Empresarial"

        ],

        "created_at":datetime.now().isoformat()

    }

    contacts.append(registro)

with open(

    OUTPUT,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        contacts,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("IOTEC CONTACT DISCOVERY ENGINE")
print("="*90)
print()

print("EMPRESAS ELEGÃƒÂVEIS :",len(contacts))
print()

print("="*90)
print("FILA DE DESCOBERTA")
print("="*90)
print()

for empresa in contacts:

    print(empresa["company"])

    print("Segmento :",empresa["segment"])

    print("Status...:",empresa["status"])

    print("Score....:",empresa["lead_score"])

    print()

print("="*90)
print("CANAIS A LOCALIZAR")
print("="*90)
print()

print("Ã¢Å"â€œ Website Oficial")
print("Ã¢Å"â€œ E-mail Corporativo")
print("Ã¢Å"â€œ Telefone Comercial")
print("Ã¢Å"â€œ LinkedIn")
print("Ã¢Å"â€œ Instagram")
print("Ã¢Å"â€œ Facebook")
print("Ã¢Å"â€œ Canal de Atendimento")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Preparar")
print("o relacionamento")
print("comercial")
print("por meio")
print("de canais")
print("institucionais")
print("pÃƒÂºblicos.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("Os leads")
print("qualificados")
print("foram encaminhados")
print("para o")
print("Centro de Descoberta")
print("de Contatos.")

print()

print("O objetivo")
print("ÃƒÂ© localizar")
print("canais oficiais")
print("para iniciar")
print("o relacionamento")
print("comercial.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Empresas :",len(contacts))
print("Data :",datetime.now())

print()

print("CONTACT DISCOVERY ENGINE OPERACIONAL.")

