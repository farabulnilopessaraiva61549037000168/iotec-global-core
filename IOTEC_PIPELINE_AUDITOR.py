import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

ARQUIVO = "IOTEC_TRAFFIC_LOG.json"

with open(
    ARQUIVO,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

print("")
print("===================================")
print("IOTEC PIPELINE AUDITOR")
print("===================================")

print("")
print("VISITAS:", len(dados.get("visitas", [])))
print("FORMULARIOS:", len(dados.get("formularios", [])))
print("LEADS:", len(dados.get("leads", [])))
print("PROPOSTAS:", len(dados.get("propostas", [])))
print("CONTRATOS:", len(dados.get("contratos", [])))
print("RECEITA:", len(dados.get("receita", [])))

receita_total = sum(
    item.get("valor", 0)
    for item in dados.get("receita", [])
)

print("")
print("RECEITA TOTAL:")
print(f"R$ {receita_total:,.2f}")

print("")
print("===================================")
print("DIAGNOSTICO")
print("===================================")

if len(dados.get("leads", [])) > len(dados.get("propostas", [])):
    print("EXISTEM LEADS SEM PROPOSTA")

if len(dados.get("propostas", [])) > len(dados.get("contratos", [])):
    print("EXISTEM PROPOSTAS SEM CONTRATO")

if len(dados.get("contratos", [])) > len(dados.get("receita", [])):
    print("EXISTEM CONTRATOS SEM RECEITA")

print("")
print("AUDITORIA FINALIZADA")




