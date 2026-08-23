import json
import os
from datetime import datetime

# ==========================================================
# IOTEC CONTROL TOWER
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

def load(file):

    if not os.path.exists(file):
        return []

    try:

        with open(file,"r",encoding="utf-8") as f:

            data=json.load(f)

            if isinstance(data,list):
                return data

    except:
        pass

    return []


# ==========================================================

companies = load(FILES["companies"])
opportunities = load(FILES["opportunities"])
crm = load(FILES["crm"])
qualified = load(FILES["qualified"])
contacts = load(FILES["contacts"])
proposals = load(FILES["proposals"])


qualified_buyers = sum(

    1 for x in qualified

    if x.get("potential_buyer",False)

)

contacts_found = sum(

    1 for x in contacts

    if x.get("status","").upper() != "AGUARDANDO DESCOBERTA"

)

contracts = 0
customers = 0
revenue = 0


# ==========================================================
# DETECÃƒâ€¡ÃƒÆ'O DO GARGALO
# ==========================================================

if qualified_buyers == 0:

    bottleneck = "QUALIFICAR LEADS"

    mission = "Melhorar a qualidade da prospecÃƒÂ§ÃƒÂ£o."

elif contacts_found < qualified_buyers:

    bottleneck = "LOCALIZAR CANAIS OFICIAIS"

    mission = "Descobrir website, e-mail, telefone e LinkedIn."

elif len(proposals) < qualified_buyers:

    bottleneck = "GERAR PROPOSTAS"

    mission = "Gerar propostas comerciais."

elif contracts == 0:

    bottleneck = "NEGOCIAR"

    mission = "Iniciar contato comercial."

elif revenue == 0:

    bottleneck = "PRIMEIRA VENDA"

    mission = "Converter oportunidade em receita."

else:

    bottleneck = "ESCALAR OPERAÃƒâ€¡ÃƒÆ'O"

    mission = "Expandir para novos mercados."


# ==========================================================

health = 100

if contacts_found < qualified_buyers:
    health -= 10

if len(proposals) > qualified_buyers:
    health -= 10

if revenue == 0:
    health -= 10


# ==========================================================

print("="*90)
print("IOTEC CONTROL TOWER")
print("="*90)
print()

print("OBJETIVO ESTRATÃƒâ€°GICO")
print("-"*90)
print()

print("GERAR RECEITA")

print()

print("="*90)
print("PAINEL OPERACIONAL")
print("="*90)
print()

print("Empresas.......................",len(companies))
print("Oportunidades.................",len(opportunities))
print("CRM...........................",len(crm))
print("Compradores...................",qualified_buyers)
print("Contatos Confirmados..........",contacts_found)
print("Propostas.....................",len(proposals))
print("Contratos.....................",contracts)
print("Clientes......................",customers)
print("Receita....................... R$",format(revenue,",.2f"))

print()

print("="*90)
print("MAIOR GARGALO")
print("="*90)
print()

print(bottleneck)

print()

print("="*90)
print("MISSÃƒÆ'O AUTOMÃƒÂTICA")
print("="*90)
print()

print(mission)

print()

print("="*90)
print("SAÃƒÅ¡DE OPERACIONAL")
print("="*90)
print()

print(str(health)+"%")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")

print()

print("A Torre de Controle")

print("identificou")

print("automaticamente")

print("o principal")

print("gargalo")

print("da operaÃƒÂ§ÃƒÂ£o.")

print()

print("Toda a plataforma")

print("passa a trabalhar")

print("na missÃƒÂ£o")

print("prioritÃƒÂ¡ria")

print("atÃƒÂ© que")

print("ela seja")

print("resolvida.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())

print()

print("CONTROL TOWER OPERACIONAL.")

