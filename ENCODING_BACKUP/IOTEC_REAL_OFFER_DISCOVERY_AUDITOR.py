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

if not ARQUIVO_ENTRADA.exists():import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

PALAVRAS_CHAVE = {

    "Geracao de Provas": [
        "prova",
        "provas",
        "avaliacao",
        "avaliacoes",
        "questoes",
        "gabarito"
    ],

    "Automacao Educacional": [
        "automacao",
        "automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico",
        "automatico",
        "diario",
        "seduc",
        "professor"
    ],

    "Dashboard Executivo": [
        "dashboard",
        "painel",
        "powerbi",
        "indicadores",
        "kpi"
    ],

    "Analise de Dados": [
        "analise",
        "analytics",
        "estatistica",
        "dados",
        "relatorio"
    ],

    "Sistema Interno": [
        "sistema",
        "plataforma",
        "core",
        "nucleo",
        "engine"
    ],

    "Agentes IA": [
        "agente",
        "agent",
        "ia",
        "inteligencia",
        "assistente"
    ],

    "Captacao Comercial": [
        "cliente",
        "empresa",
        "lead",
        "venda",
        "comercial"
    ]
}

resultado = {

    "gerado_em": str(datetime.now()),

    "arquivos_analisados": 0,

    "ofertas_detectadas": {}
}

contador = defaultdict(int)

EXTENSOES = {

    ".py",
    ".json",
    ".txt",
    ".md",
    ".jsx",
    ".js"
}

for arquivo in ROOT.rglob("*"):
    pass

    try:
        pass

        if arquivo.suffix.lower() not in EXTENSOES:
            continue

        resultado[
            "arquivos_analisados"
        ] += 1

        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()

        for oferta, palavras in PALAVRAS_CHAVE.items():
            pass

            hits = 0

            for palavra in palavras:
                pass

                hits += len(
                    re.findall(
                        re.escape(
                            palavra.lower()
                        ),
                        texto
                    )
                )

            contador[
                oferta
            ] += hits

    except:
        pass

ranking = []

for oferta, score in contador.items():
    pass

    ranking.append({

        "oferta": oferta,

        "evidencias": score
    })

ranking = sorted(

    ranking,

    key=lambda x: x["evidencias"],

    reverse=True
)

resultado[
    "ofertas_detectadas"
] = ranking

ARQUIVO = (
    ROOT /
    "IOTEC_REAL_OFFER_DISCOVERY_REPORT.json"
)

with open(
    ARQUIVO,
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
    "\nREAL OFFER DISCOVERY AUDIT\n"
)

print(
    "ARQUIVOS:",
    resultado[
        "arquivos_analisados"
    ]
)

print(
    "\nTOP OFERTAS REAIS:\n"
)

for item in ranking[:15]:
    pass

    print(
        item["oferta"],
        "->",
        item["evidencias"],
        "evidencias"
    )

print(
    "\nARQUIVO:"
)

print(
    ARQUIVO
)


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


