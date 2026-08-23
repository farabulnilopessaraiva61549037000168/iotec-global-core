import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC DEEP DISCOVERY ENGINE
# ==========================================================

import os
import json
from datetime import datetime
from collections import Counter

print("=" * 70)
print("IOTEC DEEP DISCOVERY ENGINE")
print("=" * 70)

BASE_DIR = "."

print("\nDATA:")
print(datetime.now())

ativos = []
extensoes = Counter()

keywords_receita = [
    "revenue",
    "commercial",
    "lead",
    "proposal",
    "contract",
    "client",
    "payment",
    "billing",
    "invoice"
]

keywords_estrategicas = [
    "dashboard",
    "executive",
    "control",
    "command",
    "war",
    "intelligence",
    "tower",
    "cockpit",
    "pipeline"
]

print("\nESCANEANDO ECOSSISTEMA...")

for raiz, dirs, arquivos in os.walk(BASE_DIR):

    for arquivo in arquivos:

        caminho = os.path.join(raiz, arquivo)

        try:
            tamanho = os.path.getsize(caminho)
        except:
            tamanho = 0

        nome = arquivo.lower()

        score = 0
        categoria = "COMUM"

        for palavra in keywords_receita:

            if palavra in nome:
                score += 40

        for palavra in keywords_estrategicas:

            if palavra in nome:
                score += 25

        if arquivo.endswith(".py"):
            score += 15

        if tamanho > 10000:
            score += 5

        if score >= 70:
            categoria = "CRITICO"

        elif score >= 40:
            categoria = "ESTRATEGICO"

        elif score >= 20:
            categoria = "IMPORTANTE"

        extensao = os.path.splitext(arquivo)[1].upper()

        extensoes[extensao] += 1

        ativos.append({

            "arquivo": arquivo,
            "caminho": caminho,
            "tamanho_kb": round(tamanho / 1024, 2),
            "score": score,
            "categoria": categoria

        })

# ==========================================================
# ORDENAR
# ==========================================================

ativos.sort(
    key=lambda x: x["score"],
    reverse=True
)

top_ativos = ativos[:100]

# ==========================================================
# RELATORIO
# ==========================================================

criticos = len(
    [a for a in ativos if a["categoria"] == "CRITICO"]
)

estrategicos = len(
    [a for a in ativos if a["categoria"] == "ESTRATEGICO"]
)

importantes = len(
    [a for a in ativos if a["categoria"] == "IMPORTANTE"]
)

print("\n" + "=" * 70)
print("RESUMO")
print("=" * 70)

print("ATIVOS ANALISADOS:", len(ativos))
print("CRITICOS:", criticos)
print("ESTRATEGICOS:", estrategicos)
print("IMPORTANTES:", importantes)

print("\n" + "=" * 70)
print("TOP 25 ATIVOS")
print("=" * 70)

for ativo in top_ativos[:25]:

    print(
        ativo["categoria"],
        "|",
        ativo["score"],
        "|",
        ativo["arquivo"]
    )

print("\n" + "=" * 70)
print("EXTENSOES MAIS ENCONTRADAS")
print("=" * 70)

for ext, qtd in extensoes.most_common(20):

    print(ext, "->", qtd)

# ==========================================================
# EXPORTACAO
# ==========================================================

saida = {

    "data": str(datetime.now()),

    "total_ativos": len(ativos),

    "criticos": criticos,

    "estrategicos": estrategicos,

    "importantes": importantes,

    "top_ativos": top_ativos

}

with open(
    "IOTEC_DEEP_DISCOVERY_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        saida,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\n" + "=" * 70)
print("ARQUIVO GERADO")
print("=" * 70)

print("IOTEC_DEEP_DISCOVERY_REPORT.json")

print("\n" + "=" * 70)
print("ORDEM MOR")
print("=" * 70)

print("""
NAO CONTAR ARQUIVOS.

DESCOBRIR VALOR.

NAO ACUMULAR CODIGO.

ACUMULAR CONHECIMENTO.

NAO PROCURAR MAIS ATIVOS.

IDENTIFICAR OS ATIVOS CENTRAIS.
""")

print("\nDEEP DISCOVERY ENGINE ATIVO")



