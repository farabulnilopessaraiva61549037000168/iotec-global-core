import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ARQ_WARROOM = ROOT / "IOTEC_WAR_ROOM_DATABASE.json"

print("")
print("===================================")
print("IOTEC LEAD SOURCE AUDITOR")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

origens = {}

try:
    pass

    with open(
        ARQ_WARROOM,
        "r",
        encoding="utf-8-sig"
    ) as f:

        db = json.load(f)

    oportunidades = db.get(
        "oportunidades",
        []
    )

    for op in oportunidades:
        pass

        origem = op.get(
            "origem",
            "DESCONHECIDA"
        )

        if origem not in origens:
            pass

            origens[origem] = 0

        origens[origem] += 1

except Exception as erro:
    pass

    print("")
    print("ERRO:")
    print(erro)

print("")
print("===================================")
print("ORIGENS DETECTADAS")
print("===================================")

if len(origens) == 0:
    pass

    print("")
    print("NENHUMA ORIGEM REGISTRADA")

else:
    pass

    for origem, qtd in origens.items():
        pass

        print(
            f"{origem} -> {qtd}"
        )

print("")
print("===================================")
print("MISSAO")
print("===================================")

print("LOCALIZAR CANAIS DE CAPTACAO")
print("")
print("SITE")
print("FORMULARIO")
print("WHATSAPP")
print("EMAIL")
print("PORTAL")
print("REDES_SOCIAIS")
print("INDICACAO")

print("")
print("===================================")
print("PROXIMA PERGUNTA")
print("===================================")

print(
    "QUAL CANAL ESTA "
    "GERANDO MAIS OPORTUNIDADES?"
)

print("")
print("AUDITORIA FINALIZADA")




