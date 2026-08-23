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

ARQUIVO_ENTRADA = (
    ROOT /
    "IOTEC_OFFER_VALUATION_REPORT.json"
)

if not ARQUIVO_ENTRADA.exists():
    pass

    print(
        "RELATORIO DE OFERTAS NAO ENCONTRADO"
    )

    raise SystemExit

with open(
    ARQUIVO_ENTRADA,
    "r",
    encoding="utf-8"
) as f:

    dados = json.load(f)

resultado = {

    "gerado_em": str(datetime.now()),

    "estado":
        "ANALISE_EXECUTABILIDADE",

    "ofertas": []
}

for oferta in dados["ofertas"]:
    pass

    nome = oferta["nome"]

    ticket = oferta["ticket"]

    receita = oferta["receita_maxima"]

    margem = oferta["margem"]

    capacidade = oferta["capacidade"]

    dependencias = []

    risco = "BAIXO"

    prioridade = 5

    if ticket >= 50000:
        pass

        dependencias.append(
            "NEGOCIACAO_COMPLEXA"
        )

        dependencias.append(
            "CLIENTE_GRANDE"
        )

        risco = "ALTO"

        prioridade = 4

    elif ticket >= 10000:
        pass

        dependencias.append(
            "PROSPECÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O"
        )

        risco = "MEDIO"

        prioridade = 2

    else:
        pass

        dependencias.append(
            "VENDA_ESCALAVEL"
        )

        risco = "BAIXO"

        prioridade = 1

    score_execucao = (
        receita *
        margem
    )

    resultado["ofertas"].append({

        "nome":
            nome,

        "ticket":
            ticket,

        "receita_maxima":
            receita,

        "capacidade":
            capacidade,

        "risco":
            risco,

        "dependencias":
            dependencias,

        "prioridade":
            prioridade,

        "score_execucao":
            score_execucao
    })

resultado["ofertas"] = sorted(

    resultado["ofertas"],

    key=lambda x: (
        x["prioridade"],
        -x["score_execucao"]
    )
)

ARQUIVO_SAIDA = (
    ROOT /
    "IOTEC_EXECUTION_CAPACITY_REPORT.json"
)

with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    "\nEXECUTION CAPACITY ENGINE\n"
)

print(
    "OFERTAS ANALISADAS:",
    len(
        resultado["ofertas"]
    )
)

print(
    "\nPRIORIDADES:\n"
)

for item in resultado["ofertas"]:
    pass

    print(
        f"{item['prioridade']} -> "
        f"{item['nome']} | "
        f"RISCO={item['risco']}"
    )

print(
    "\nARQUIVO:"
)

print(
    ARQUIVO_SAIDA
)




