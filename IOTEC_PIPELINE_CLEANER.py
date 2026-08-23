import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from datetime import datetime

ARQUIVO_BASE = "IOTEC_PIPELINE_DATABASE.json"
ARQUIVO_HISTORICO = "IOTEC_PIPELINE_ARCHIVE.json"

print("")
print("===================================")
print("IOTEC PIPELINE CLEANER")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

with open(
    ARQUIVO_BASE,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

try:
    pass

    with open(
        ARQUIVO_HISTORICO,
        "r",
        encoding="utf-8"
    ) as f:

        historico = json.load(f)

except:
    pass

    historico = {
        "propostas_arquivadas": []
    }

propostas_validas = []
arquivadas = 0

for proposta in dados["propostas"]:
    pass

    if proposta.get("lead_id"):
        pass

        propostas_validas.append(
            proposta
        )

    else:
        pass

        proposta["motivo"] = "SEM_LEAD"

        proposta[
            "data_arquivamento"
        ] = str(datetime.now())

        historico[
            "propostas_arquivadas"
        ].append(
            proposta
        )

        arquivadas += 1

        print("")
        print("ARQUIVADA:")
        print(proposta["id"])

dados["propostas"] = propostas_validas

with open(
    ARQUIVO_BASE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dados,
        f,
        indent=4,
        ensure_ascii=False
    )

with open(
    ARQUIVO_HISTORICO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        historico,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("===================================")
print("RESUMO")
print("===================================")

print("")
print("PROPOSTAS ARQUIVADAS:")
print(arquivadas)

print("")
print("BASE ATIVA:")
print(len(dados["propostas"]))
print("PROPOSTAS")

print("")
print("ARQUIVO HISTORICO:")
print(ARQUIVO_HISTORICO)

print("")
print("===================================")
print("ORDEM MOR")
print("===================================")

print(
    "REMOVER DA OPERACAO "
    "REGISTROS SEM ORIGEM "
    "VALIDA."
)

print("")
print("PIPELINE CLEANER ATIVO")




