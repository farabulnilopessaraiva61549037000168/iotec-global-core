# ==============================================================================
# IOTEC NATURAL INTELLIGENCE ARCHAEOLOGY ENGINE
# V1.0
# Procura vestÃ­gios de inteligÃªncia natural na IOTEC
# ==============================================================================

import os
from pathlib import Path
from collections import defaultdict

ROOT = Path.home() / "Documents" / "OMEGA_BASE"

EXTENSOES = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".ini",
    ".cfg"
}

INSTINTOS = {

    "ABELHAS":[
        "bee",
        "beehive",
        "hive",
        "abelha",
        "colmeia"
    ],

    "ENXAME":[
        "swarm",
        "enxame",
        "formiga",
        "ant",
        "colony"
    ],

    "BALEIA":[
        "whale",
        "baleia",
        "orca",
        "ocean"
    ],

    "CORVO":[
        "crow",
        "raven",
        "corvo"
    ],

    "CORUJA":[
        "owl",
        "coruja"
    ],

    "FALCAO":[
        "falcon",
        "hawk",
        "falcao"
    ],

    "AGUIA":[
        "eagle",
        "aguia"
    ],

    "GARCA":[
        "heron",
        "garca",
        "egret"
    ],

    "GAIVOTA":[
        "seagull",
        "gaivota"
    ],

    "PARDAL":[
        "sparrow",
        "pardal"
    ],

    "ORNITORRINCO":[
        "platypus",
        "ornitorrinco"
    ],

    "INSTINTO":[
        "instinct",
        "instinto",
        "behavior",
        "behaviour",
        "comportamento",
        "adaptive",
        "adaptativo",
        "bio",
        "nature",
        "natural"
    ]
}

resultado = defaultdict(list)

total = 0

for raiz, _, arquivos in os.walk(ROOT):

    for arquivo in arquivos:

        ext = Path(arquivo).suffix.lower()

        if ext not in EXTENSOES:
            continue

        caminho = Path(raiz) / arquivo

        total += 1

        try:

            texto = caminho.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

        except:
            continue

        for categoria, palavras in INSTINTOS.items():

            for palavra in palavras:

                if palavra.lower() in texto:

                    resultado[categoria].append(str(caminho))
                    break


print("="*80)
print("IOTEC NATURAL INTELLIGENCE REPORT")
print("="*80)

print()

print("Arquivos analisados:", total)
print()

for categoria in sorted(resultado):

    arquivos = sorted(set(resultado[categoria]))

    print(f"[{categoria}]")
    print(f"Encontrados: {len(arquivos)}")

    for a in arquivos[:20]:
        print("   ", a)

    if len(arquivos) > 20:
        print("   ...")

    print()

with open("IOTEC_NATURAL_INTELLIGENCE_REPORT.md","w",encoding="utf-8") as f:

    f.write("# IOTEC Natural Intelligence Report\n\n")

    for categoria in sorted(resultado):

        f.write(f"## {categoria}\n\n")

        arquivos = sorted(set(resultado[categoria]))

        f.write(f"Total: {len(arquivos)}\n\n")

        for a in arquivos:
            f.write("- "+a+"\n")

        f.write("\n")

print("RelatÃ³rio salvo.")

