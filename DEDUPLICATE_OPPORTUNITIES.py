import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import OpportunityDB

dados = OpportunityDB.load()

print("="*70)
print("IOTEC OPPORTUNITY DEDUPLICATOR")
print("="*70)
print()

print("Registros Originais :", len(dados))

unicos = {}

for registro in dados:

    nome = registro.get("company_name","").strip()

    if not nome:
        continue

    if nome not in unicos:

        registro["updated_at"] = str(datetime.now())
        unicos[nome] = registro

    else:

        atual = unicos[nome]

        for chave, valor in registro.items():

            if valor not in ("", None, [], {}):

                atual[chave] = valor

        atual["updated_at"] = str(datetime.now())

resultado = sorted(

    unicos.values(),

    key=lambda x: x["company_name"]

)

OpportunityDB.save(resultado)

print()

print("Oportunidades Finais :", len(resultado))
print()

print("BANCO CONSOLIDADO")

