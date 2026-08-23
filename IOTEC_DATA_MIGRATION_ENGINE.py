import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO_ORIGINAL = "IOTEC_TRAFFIC_LOG.json"
ARQUIVO_NOVO = "IOTEC_PIPELINE_DATABASE.json"

print("")
print("===================================")
print("IOTEC DATA MIGRATION ENGINE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

with open(
    ARQUIVO_ORIGINAL,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

nova_base = {

    "leads": [],
    "propostas": [],
    "contratos": [],
    "receita": []
}

print("")
print("MIGRANDO LEADS...")

for indice, lead in enumerate(
    dados.get("leads", []),
    start=1
):

    lead_id = f"LEAD_{indice:04d}"

    novo_lead = {

        "id": lead_id,
        "data": lead.get("data"),
        "produto": lead.get("produto"),
        "origem": lead.get("origem")
    }

    nova_base["leads"].append(
        novo_lead
    )

print("OK")

print("")
print("MIGRANDO PROPOSTAS...")

for indice, proposta in enumerate(
    dados.get("propostas", []),
    start=1
):

    lead_ref = None

    if indice <= len(
        nova_base["leads"]
    ):

        lead_ref = (
            nova_base["leads"]
            [indice - 1]["id"]
        )

    proposta_id = (
        f"PROP_{indice:04d}"
    )

    nova_base["propostas"].append({

        "id": proposta_id,
        "lead_id": lead_ref,
        "cliente":
        proposta.get("cliente"),

        "produto":
        proposta.get("produto"),

        "valor":
        proposta.get("valor"),

        "status":
        proposta.get("status"),

        "data":
        proposta.get("data")
    })

print("OK")

print("")
print("MIGRANDO CONTRATOS...")

for indice, contrato in enumerate(
    dados.get("contratos", []),
    start=1
):

    proposta_ref = None

    if indice <= len(
        nova_base["propostas"]
    ):

        proposta_ref = (
            nova_base["propostas"]
            [indice - 1]["id"]
        )

    contrato_id = (
        f"CONT_{indice:04d}"
    )

    nova_base["contratos"].append({

        "id": contrato_id,
        "proposta_id": proposta_ref,

        "cliente":
        contrato.get("cliente"),

        "produto":
        contrato.get("produto"),

        "valor":
        contrato.get("valor"),

        "status":
        contrato.get("status"),

        "data":
        contrato.get("data")
    })

print("OK")

print("")
print("MIGRANDO RECEITA...")

for indice, receita in enumerate(
    dados.get("receita", []),
    start=1
):

    contrato_ref = None

    if indice <= len(
        nova_base["contratos"]
    ):

        contrato_ref = (
            nova_base["contratos"]
            [indice - 1]["id"]
        )

    receita_id = (
        f"REC_{indice:04d}"
    )

    nova_base["receita"].append({

        "id": receita_id,
        "contrato_id": contrato_ref,

        "cliente":
        receita.get("cliente"),

        "valor":
        receita.get("valor"),

        "data":
        receita.get("data")
    })

print("OK")

with open(
    ARQUIVO_NOVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nova_base,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("RESULTADO")
print("===================================")

print("LEADS:")
print(
    len(
        nova_base["leads"]
    )
)

print("PROPOSTAS:")
print(
    len(
        nova_base["propostas"]
    )
)

print("CONTRATOS:")
print(
    len(
        nova_base["contratos"]
    )
)

print("RECEITAS:")
print(
    len(
        nova_base["receita"]
    )
)

print("")
print("ARQUIVO GERADO:")
print(
    ARQUIVO_NOVO
)

print("")
print("MIGRACAO FINALIZADA")




