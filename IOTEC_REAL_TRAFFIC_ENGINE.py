import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import os
from datetime import datetime

print("")
print("===================================")
print("IOTEC REAL TRAFFIC ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

ARQUIVO_LOG = "IOTEC_TRAFFIC_LOG.json"

if not os.path.exists(ARQUIVO_LOG):
    pass

    estrutura = {

        "visitas": [],
        "formularios": [],
        "leads": []
    }

    with open(
        ARQUIVO_LOG,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            estrutura,
            f,
            indent=4,
            ensure_ascii=False
        )

with open(
    ARQUIVO_LOG,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

visitas = len(
    dados["visitas"]
)

formularios = len(
    dados["formularios"]
)

leads = len(
    dados["leads"]
)

conversao = 0

if visitas > 0:
    pass

    conversao = (
        leads / visitas
    ) * 100

print("")
print("===================================")
print("TRAFEGO REAL")
print("===================================")

print("VISITAS:")
print(visitas)

print("")
print("FORMULARIOS:")
print(formularios)

print("")
print("LEADS:")
print(leads)

print("")
print("CONVERSAO:")
print(
    f"{conversao:.2f}%"
)

print("")
print("===================================")
print("ULTIMOS EVENTOS")
print("===================================")

ultimas_visitas = (
    dados["visitas"][-5:]
)

for evento in ultimas_visitas:
    pass

    print("")
    print(evento)

print("")
print("===================================")
print("FORMULA")
print("===================================")

print("VISITANTE")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("VISITA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("FORMULARIO")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("LEAD")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("PROPOSTA")
print("ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ")
print("RECEITA")

print("")
print("===================================")
print("PERGUNTAS DO NUCLEO")
print("===================================")

perguntas = [

    "QUANTAS VISITAS?",
    "QUANTOS LEADS?",
    "QUAL CONVERSAO?",
    "QUAL PAGINA?",
    "QUAL PRODUTO?",
    "QUAL CANAL?"
]

for pergunta in perguntas:
    pass

    print("-", pergunta)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "SUBSTITUIR HIPOTESES "
    "POR DADOS REAIS."
)

print("")
print("REAL TRAFFIC ENGINE ATIVO")




