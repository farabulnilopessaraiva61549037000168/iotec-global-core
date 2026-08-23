import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO = "IOTEC_PIPELINE_DATABASE.json"

print("")
print("===================================")
print("IOTEC PIPELINE GUARDIAN")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

leads = dados.get("leads", [])
propostas = dados.get("propostas", [])

ids_leads = {
    lead["id"]
    for lead in leads
}

ids_leads_usados = {
    proposta["lead_id"]
    for proposta in propostas
    if proposta.get("lead_id")
}

leads_disponiveis = ids_leads - ids_leads_usados

print("")
print("===================================")
print("VERIFICACAO")
print("===================================")

print("")
print("LEADS:")
print(len(leads))

print("")
print("PROPOSTAS:")
print(len(propostas))

print("")
print("LEADS DISPONIVEIS:")
print(len(leads_disponiveis))

if len(leads_disponiveis) == 0:
    pass

    print("")
    print("===================================")
    print("ALERTA")
    print("===================================")

    print("")
    print("NAO EXISTEM LEADS")
    print("DISPONIVEIS PARA")
    print("NOVAS PROPOSTAS")

    print("")
    print("OPERACAO BLOQUEADA")

else:
    pass

    print("")
    print("===================================")
    print("AUTORIZACAO")
    print("===================================")

    print("")
    print("EXISTEM LEADS")
    print("DISPONIVEIS")

    print("")
    print("CRIACAO DE")
    print("PROPOSTAS LIBERADA")

    print("")
    print("LEADS LIVRES:")

    for lead in sorted(leads_disponiveis):
        pass

        print("-", lead)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "NENHUMA PROPOSTA "
    "DEVE SER CRIADA "
    "SEM LEAD."
)

print("")
print("PIPELINE GUARDIAN ATIVO")




