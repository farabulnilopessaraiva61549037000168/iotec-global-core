import json
import os
from datetime import datetime

# ==========================================================
# IOTEC COMMERCIAL COMMAND CENTER
# ==========================================================

FILES = {

    "companies":"IOTEC_COMPANY_DATABASE.json",

    "opportunities":"IOTEC_OPPORTUNITY_DATABASE.json",

    "crm":"IOTEC_CRM_DATABASE.json",

    "qualified":"IOTEC_QUALIFIED_LEADS.json",

    "contacts":"IOTEC_CONTACT_DATABASE.json",

    "proposals":"IOTEC_PROPOSAL_DATABASE.json"

}


# ==========================================================

def load_count(file):

    if not os.path.exists(file):
        return 0

    try:

        with open(file,"r",encoding="utf-8") as f:

            data=json.load(f)

            if isinstance(data,list):
                return len(data)

            if isinstance(data,dict):
                return len(data)

            return 0

    except:

        return 0


# ==========================================================

companies=load_count(FILES["companies"])

opportunities=load_count(FILES["opportunities"])

crm=load_count(FILES["crm"])

qualified=load_count(FILES["qualified"])

contacts=load_count(FILES["contacts"])

proposals=load_count(FILES["proposals"])

contracts=0

customers=0

revenue=0


# ==========================================================

print("="*90)
print("IOTEC COMMERCIAL COMMAND CENTER")
print("="*90)
print()

print("VISÃƒÆ'O GERAL")
print("-"*90)
print()

print(f"Empresas Descobertas............. {companies}")

print(f"Oportunidades.................... {opportunities}")

print(f"Leads Qualificados............... {qualified}")

print(f"CRM.............................. {crm}")

print(f"Contatos......................... {contacts}")

print(f"Propostas........................ {proposals}")

print(f"Contratos........................ {contracts}")

print(f"Clientes......................... {customers}")

print(f"Receita.......................... R$ {revenue:,.2f}")

print()

print("="*90)
print("GARGALO ATUAL")
print("="*90)
print()

if contacts == 0:

    gargalo="LOCALIZAR CANAIS OFICIAIS"

elif proposals == 0:

    gargalo="GERAR PROPOSTAS"

elif contracts == 0:

    gargalo="NEGOCIAR"

elif revenue == 0:

    gargalo="REALIZAR PRIMEIRA VENDA"

else:

    gargalo="ESCALAR OPERAÃƒâ€¡ÃƒÆ'O"

print(gargalo)

print()

print("="*90)
print("MISSÃƒâ€¢ES PRIORITÃƒÂRIAS")
print("="*90)
print()

missions=[

    "Localizar Website Oficial",

    "Localizar E-mail Corporativo",

    "Localizar Telefone Comercial",

    "Localizar LinkedIn",

    "Enviar PortfÃƒÂ³lio",

    "Enviar Proposta",

    "Registrar Resposta",

    "Converter em Cliente"

]

for i,m in enumerate(missions,1):

    print(f"{i:02d} - {m}")

print()

print("="*90)
print("INDICADORES")
print("="*90)
print()

conversion=0

if crm>0:

    conversion=(qualified/crm)*100

print(f"Taxa de QualificaÃƒÂ§ÃƒÂ£o............ {conversion:.1f}%")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("Toda a operaÃƒÂ§ÃƒÂ£o")

print("comercial")

print("passa agora")

print("a ser acompanhada")

print("por um ÃƒÂºnico")

print("Centro de Comando.")

print()

print("Os gargalos")

print("sÃƒÂ£o identificados")

print("automaticamente")

print("e transformados")

print("em missÃƒÂµes")

print("prioritÃƒÂ¡rias.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Maturidade Comercial..... 82 %")

print("Data.....................",datetime.now())

print()

print("COMMERCIAL COMMAND CENTER OPERACIONAL.")

