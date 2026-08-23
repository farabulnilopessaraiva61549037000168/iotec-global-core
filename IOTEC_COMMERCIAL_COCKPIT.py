import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO = "IOTEC_TRAFFIC_LOG.json"

try:
    pass

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as f:

        dados = json.load(f)

except:
    pass

    dados = {

        "visitas": [],
        "formularios": [],
        "leads": [],
        "propostas": [],
        "contratos": [],
        "receita": []
    }

visitas = len(dados.get("visitas", []))
formularios = len(dados.get("formularios", []))
leads = len(dados.get("leads", []))
propostas = len(dados.get("propostas", []))
contratos = len(dados.get("contratos", []))

receita_total = 0

for item in dados.get("receita", []):
    pass

    receita_total += item.get(
        "valor",
        0
    )

taxa_formulario = 0
taxa_lead = 0
taxa_proposta = 0
taxa_contrato = 0

if visitas > 0:
    pass

    taxa_formulario = (
        formularios / visitas
    ) * 100

    taxa_lead = (
        leads / visitas
    ) * 100

if leads > 0:
    pass

    taxa_proposta = (
        propostas / leads
    ) * 100

if propostas > 0:
    pass

    taxa_contrato = (
        contratos / propostas
    ) * 100

print("")
print("===================================")
print("IOTEC COMMERCIAL COCKPIT")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("===================================")
print("FUNIL COMERCIAL")
print("===================================")

print("")
print("VISITAS:")
print(visitas)

print("")
print("FORMULARIOS:")
print(formularios)

print("")
print("LEADS:")
print(leads)

print("")
print("PROPOSTAS:")
print(propostas)

print("")
print("CONTRATOS:")
print(contratos)

print("")
print("===================================")
print("CONVERSAO")
print("===================================")

print("")
print("VISITA -> FORMULARIO:")
print(f"{taxa_formulario:.2f}%")

print("")
print("VISITA -> LEAD:")
print(f"{taxa_lead:.2f}%")

print("")
print("LEAD -> PROPOSTA:")
print(f"{taxa_proposta:.2f}%")

print("")
print("PROPOSTA -> CONTRATO:")
print(f"{taxa_contrato:.2f}%")

print("")
print("===================================")
print("RECEITA")
print("===================================")

print("")
print("RECEITA TOTAL:")
print(
    f"R$ {receita_total:,.2f}"
)

print("")
print("===================================")
print("MAPA OPERACIONAL")
print("===================================")

print("VISITA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("FORMULARIO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("LEAD")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("CONTRATO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("RECEITA")

print("")
print("===================================")
print("STATUS")
print("===================================")

if leads > 0:
    pass

    print("LEADS DETECTADOS")

else:
    pass

    print("SEM LEADS")

if propostas > 0:
    pass

    print("PROPOSTAS DETECTADAS")

else:
    pass

    print("SEM PROPOSTAS")

if contratos > 0:
    pass

    print("CONTRATOS DETECTADOS")

else:
    pass

    print("SEM CONTRATOS")

if receita_total > 0:
    pass

    print("RECEITA DETECTADA")

else:
    pass

    print("SEM RECEITA")

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "TRANSFORMAR VISITAS "
    "EM RECEITA."
)

print("")
print("COMMERCIAL COCKPIT ATIVO")




