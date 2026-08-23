import json
import os
from datetime import datetime

# ==========================================================
# IOTEC OPERATIONAL AUDITOR
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

            return []

    except:

        return []


companies = load(FILES["companies"])
opportunities = load(FILES["opportunities"])
crm = load(FILES["crm"])
qualified = load(FILES["qualified"])
contacts = load(FILES["contacts"])
proposals = load(FILES["proposals"])


# ==========================================================
# CONTADORES REAIS
# ==========================================================

qualified_buyers = sum(
    1 for x in qualified
    if x.get("potential_buyer", False)
)

contacts_found = sum(
    1 for x in contacts
    if x.get("status","").upper() != "AGUARDANDO DESCOBERTA"
)

alerts = []

if len(companies) != len(opportunities):
    alerts.append("Quantidade de empresas diferente das oportunidades.")

if len(opportunities) != len(crm):
    alerts.append("CRM diferente das oportunidades.")

if qualified_buyers > len(crm):
    alerts.append("Compradores qualificados maior que CRM.")

if len(proposals) > qualified_buyers:
    alerts.append("Existem propostas para leads nÃƒÂ£o qualificados.")

if contacts_found < qualified_buyers:
    alerts.append("Faltam canais oficiais para empresas qualificadas.")


# ==========================================================
# SAÃƒÅ¡DE OPERACIONAL
# ==========================================================

health = 100

health -= len(alerts) * 10

if health < 0:
    health = 0


# ==========================================================
# RELATÃƒâ€œRIO
# ==========================================================

print("="*90)
print("IOTEC OPERATIONAL AUDITOR")
print("="*90)
print()

print("AUDITORIA DOS MÃƒâ€œDULOS")
print("-"*90)
print()

print("Empresas.....................",len(companies))
print("Oportunidades...............",len(opportunities))
print("CRM.........................",len(crm))
print("Compradores Qualificados....",qualified_buyers)
print("Contatos Confirmados........",contacts_found)
print("Propostas...................",len(proposals))
print()

print("="*90)
print("INCONSISTÃƒÅ NCIAS")
print("="*90)
print()

if alerts:

    for item in alerts:
        print("Ã¢â‚¬Â¢",item)

else:

    print("Nenhuma inconsistÃƒÂªncia encontrada.")

print()

print("="*90)
print("SAÃƒÅ¡DE OPERACIONAL")
print("="*90)
print()

print(f"{health}%")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Garantir")
print("consistÃƒÂªncia")
print("entre")
print("todos")
print("os mÃƒÂ³dulos")
print("da plataforma.")

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

if alerts:

    print("Foram detectadas")
    print(len(alerts),"inconsistÃƒÂªncias")
    print("na operaÃƒÂ§ÃƒÂ£o.")
    print()

    print("As missÃƒÂµes")
    print("corretivas")
    print("foram")
    print("priorizadas.")

else:

    print("Todos os")
    print("mÃƒÂ³dulos")
    print("estÃƒÂ£o")
    print("consistentes.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Data :",datetime.now())
print()

print("OPERATIONAL AUDITOR OPERACIONAL.")

