import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - VISUALIZADOR ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICO DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# REGULUS ORGANIZER ENGINE v1.0
# EMPRESA: IOTEC
# OBJETIVO:
# ORGANIZAR E VISUALIZAR O ECOSSISTEMA OPERACIONAL
# ============================================================

import os
import json
from datetime import datetime
from collections import defaultdict

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# ============================================================

PASTAS_ANALISE = [
    r"C:\IOTEC",
    r"C:\Users\Bruno Lopes\Downloads",
    r"C:\Users\Bruno Lopes\Desktop\DIVERSOS",
    r"D:\IOTEC"
]

EXTENSOES_SISTEMA = [
    ".py",
    ".html",
    ".css",
    ".js",
    ".json",
    ".tsx",
    ".jsx",
    ".sql"
]

# ============================================================
# ESTRUTURA CENTRAL
# ============================================================

NUCLEO = {
    "empresa": "IOTEC",
    "cidade": "REGULUS_CITY",
    "modo": "organizacao_estrategica",
    "status": "online",
    "timestamp": str(datetime.now())
}

# ============================================================
# CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTELIGENTE
# ============================================================

CLASSIFICACAO = {
    "analytics": [
        "dashboard",
        "analytics",
        "grafico",
        "metricas"
    ],

    "juridico": [
        "juris",
        "legal",
        "adv",
        "processo"
    ],

    "govtech": [
        "governo",
        "prefeitura",
        "gov",
        "transparencia"
    ],

    "financeiro": [
        "finance",
        "pagamento",
        "paypal",
        "pix"
    ],

    "frontend": [
        "html",
        "css",
        "interface",
        "netlify"
    ],

    "backend": [
        "api",
        "server",
        "flask",
        "fastapi"
    ]
}

# ============================================================
# BANCO CENTRAL
# ============================================================

ATIVOS = []
MAPA_SETORIAL = defaultdict(list)

# ============================================================
# DETECTAR SETOR
# ============================================================

def detectar_setor(nome_arquivo):
    pass

    nome = nome_arquivo.lower()

    for setor, palavras in CLASSIFICACAO.items():
        pass

        for palavra in palavras:
            pass

            if palavra in nome:
                return setor

    return "laboratorio"

# ============================================================
# ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def escavar():
    pass

    print("\n======================================================")
    print(" IOTEC VISUALIZADOR ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICO")
    print("======================================================")

    total = 0

    for pasta in PASTAS_ANALISE:
        pass

        print(f"\n[+] ANALISANDO -> {pasta}")

        if not os.path.exists(pasta):
            continue

        for raiz, dirs, arquivos in os.walk(pasta):
            pass

            for arquivo in arquivos:
                pass

                ext = os.path.splitext(arquivo)[1].lower()

                if ext in EXTENSOES_SISTEMA:
                    pass

                    caminho = os.path.join(raiz, arquivo)

                    tamanho = 0

                    try:
                        tamanho = os.path.getsize(caminho)
                    except:
                        pass

                    setor = detectar_setor(arquivo)

                    ativo = {
                        "nome": arquivo,
                        "caminho": caminho,
                        "extensao": ext,
                        "setor": setor,
                        "tamanho_kb": round(tamanho / 1024, 2)
                    }

                    ATIVOS.append(ativo)
                    MAPA_SETORIAL[setor].append(ativo)

                    total += 1

    print("\n======================================================")
    print(" ESCAVAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FINALIZADA")
    print("======================================================")

    print(f"\nATIVOS MAPEADOS: {total}")

# ============================================================
# PAINEL EXECUTIVO
# ============================================================

def painel():
    pass

    print("\n======================================================")
    print(" PAINEL ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICO")
    print("======================================================")

    for setor, ativos in MAPA_SETORIAL.items():
        pass

        tamanho_total = sum(
            item["tamanho_kb"] for item in ativos
        )

        print(f"\nSETOR: {setor.upper()}")
        print(f"ATIVOS: {len(ativos)}")
        print(f"TAMANHO TOTAL: {round(tamanho_total,2)} KB")

# ============================================================
# MATRIZES IMPORTANTES
# ============================================================

def detectar_matrizes():
    pass

    print("\n======================================================")
    print(" MATRIZES IMPORTANTES")
    print("======================================================")

    importantes = []

    for ativo in ATIVOS:
        pass

        nome = ativo["nome"].lower()

        if (
            "core" in nome or
            "engine" in nome or
            "dashboard" in nome or
            "enterprise" in nome or
            "governanca" in nome
        ):

            importantes.append(ativo)

    importantes = sorted(
        importantes,
        key=lambda x: x["tamanho_kb"],
        reverse=True
    )

    for item in importantes[:20]:
        pass

        print(f"\nNOME: {item['nome']}")
        print(f"SETOR: {item['setor']}")
        print(f"TAMANHO: {item['tamanho_kb']} KB")
        print(f"CAMINHO: {item['caminho']}")

# ============================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O JSON
# ============================================================

def exportar():
    pass

    pasta_saida = r"C:\IOTEC\VISUALIZADOR_ESTRATEGICO"

    os.makedirs(pasta_saida, exist_ok=True)

    relatorio = {
        "nucleo": NUCLEO,
        "ativos_total": len(ATIVOS),
        "setores": {}
    }

    for setor, ativos in MAPA_SETORIAL.items():
        pass

        relatorio["setores"][setor] = {
            "quantidade": len(ativos),
            "ativos": ativos[:50]
        }

    arquivo_json = os.path.join(
        pasta_saida,
        "mapa_estrategico.json"
    )

    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)

    print("\n======================================================")
    print(" EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O FINALIZADA")
    print("======================================================")

    print(f"\nJSON -> {arquivo_json}")

# ============================================================
# MAPA DE PRIORIDADES
# ============================================================

def mapa_prioridades():
    pass

    print("\n======================================================")
    print(" MAPA DE PRIORIDADES")
    print("======================================================")

    ranking = []

    for setor, ativos in MAPA_SETORIAL.items():
        pass

        ranking.append({
            "setor": setor,
            "quantidade": len(ativos)
        })

    ranking = sorted(
        ranking,
        key=lambda x: x["quantidade"],
        reverse=True
    )

    for item in ranking:
        pass

        print(
            f"\n{item['setor'].upper()} "
            f"-> {item['quantidade']} ativos"
        )

# ============================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def iniciar():
    pass

    escavar()

    painel()

    detectar_matrizes()

    mapa_prioridades()

    exportar()

    print("\n======================================================")
    print(" NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO ORGANIZADO COM SUCESSO")
    print("======================================================\n")

# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    iniciar()


