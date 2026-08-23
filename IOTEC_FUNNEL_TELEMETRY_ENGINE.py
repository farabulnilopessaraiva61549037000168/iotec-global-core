import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO = "IOTEC_TRAFFIC_LOG.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

visitas = len(dados["visitas"])
formularios = len(dados["formularios"])
leads = len(dados["leads"])

taxa_formulario = 0
taxa_lead = 0

if visitas > 0:
    pass

    taxa_formulario = (
        formularios / visitas
    ) * 100

    taxa_lead = (
        leads / visitas
    ) * 100

print("")
print("===================================")
print("IOTEC FUNNEL TELEMETRY ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

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
print("TAXA FORMULARIO:")
print(f"{taxa_formulario:.2f}%")

print("")
print("TAXA LEAD:")
print(f"{taxa_lead:.2f}%")

print("")
print("===================================")
print("FUNIL")
print("===================================")

print("VISITAS")
print(visitas)

print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("FORMULARIOS")
print(formularios)

print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")

print("LEADS")
print(leads)

print("")
print("NUCLEO DE TELEMETRIA ATIVO")




