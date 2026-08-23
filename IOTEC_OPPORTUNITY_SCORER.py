import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_OPPORTUNITY_SCORER.py

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

ENTRADA = ROOT / "RAW_ENTITIES.json"

SAIDA = ROOT / "RANKED_OPPORTUNITIES.json"

PESOS = {

    "empresa": 20,

    "site": 20,

    "email": 15,

    "telefone": 15,

    "segmento": 10,

    "cidade": 5,

    "estado": 5,

    "cnpj": 10
}

def calcular_score(registro):
    pass

    score = 0

    for campo, peso in PESOS.items():
        pass

        valor = registro.get(campo)

        if valor:
            pass

            score += peso

    return score

def classificar(score):
    pass

    if score >= 80:
        return "A"

    if score >= 50:
        return "B"

    return "C"

if not ENTRADA.exists():
    pass

    print("RAW_ENTITIES.json nÃƒÆ'Ã†â€™o encontrado")

    raise SystemExit

with open(
    ENTRADA,
    "r",
    encoding="utf-8"
) as f:

    entidades = json.load(f)

resultado = []

for item in entidades:
    pass

    score = calcular_score(item)

    classe = classificar(score)

    item["score"] = score

    item["classe"] = classe

    resultado.append(item)

resultado.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open(
    SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        {
            "gerado_em": str(datetime.now()),
            "total": len(resultado),
            "entidades": resultado
        },
        f,
        indent=4,
        ensure_ascii=False
    )

print()

print("OPPORTUNITY SCORER")

print()

print("TOTAL:", len(resultado))

print("CLASSE A:",
      sum(1 for x in resultado
          if x["classe"] == "A"))

print("CLASSE B:",
      sum(1 for x in resultado
          if x["classe"] == "B"))

print("CLASSE C:",
      sum(1 for x in resultado
          if x["classe"] == "C"))

print()

print("ARQUIVO:")

print(SAIDA)




