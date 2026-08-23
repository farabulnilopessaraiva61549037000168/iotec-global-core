"""
======================================================================
IOTEC ECOSYSTEM DISCOVERY ENGINE
VERSÃƒÆ'O 1.0
======================================================================

Descobre ecossistemas naturais da plataforma.

======================================================================
"""

import os
from pathlib import Path
from collections import defaultdict

PASTA = r"C:\IOTEC"

# ============================================================

GRUPOS = {

    "COMERCIAL":[

        "COMMERCIAL",

        "LEAD",

        "CRM",

        "CATALOG",

        "CATÃƒÂLOGO",

        "SHOWCASE",

        "PIPELINE",

        "CONTRACT",

        "PROPOSTA",

        "CLIENTE"

    ],

    "PRODUCAO":[

        "PRODUCTION",

        "QUALITY",

        "PRODUTO",

        "PROJETO",

        "DELIVERY",

        "ENTREGA"

    ],

    "KERNEL":[

        "KERNEL",

        "MISSION",

        "EVENT",

        "DATABASE",

        "CONTROL",

        "BRAIN"

    ],

    "INTELIGENCIA":[

        "GENOME",

        "DISCOVERY",

        "INTELLIGENCE",

        "INTELIGENCIA",

        "OBSERVATORY",

        "ANALYSIS"

    ],

    "FINANCEIRO":[

        "FINANCE",

        "PAYMENT",

        "PIX",

        "FATURA",

        "RECEITA",

        "CUSTO"

    ],

    "LOGISTICA":[

        "LOGISTICS",

        "TRUCK",

        "TRANSPORT",

        "WAREHOUSE",

        "FROTA"

    ]

}

# ============================================================

class EcosystemEngine:

    def __init__(self):

        self.ecossistemas = defaultdict(list)

    # ========================================================

    def analisar(self):

        print("="*70)
        print("IOTEC ECOSYSTEM DISCOVERY ENGINE")
        print("="*70)
        print()

        total = 0

        for raiz, _, arquivos in os.walk(PASTA):

            for arquivo in arquivos:

                if not arquivo.endswith(".py"):
                    continue

                total += 1

                caminho = os.path.join(raiz, arquivo)

                try:

                    texto = Path(caminho).read_text(
                        encoding="utf-8",
                        errors="ignore"
                    ).upper()

                except:
                    continue

                for grupo, palavras in GRUPOS.items():

                    for palavra in palavras:

                        if palavra in texto:

                            self.ecossistemas[grupo].append(arquivo)
                            break

        print("Arquivos analisados:", total)
        print()

    # ========================================================

    def painel(self):

        print("="*70)
        print("ECOSSISTEMAS DA IOTEC")
        print("="*70)
        print()

        for nome in sorted(self.ecossistemas):

            arquivos = sorted(set(self.ecossistemas[nome]))

            print(f"{nome} ({len(arquivos)} mÃƒÂ³dulos)")

            print("-"*60)

            for arq in arquivos[:15]:

                print("Ã¢â‚¬Â¢", arq)

            if len(arquivos) > 15:

                print(f"... + {len(arquivos)-15} mÃƒÂ³dulos")

            print()

        print("="*70)
        print("ANÃƒÂLISE DO KERNEL")
        print("="*70)
        print()

        maior = ""

        qtd = 0

        for eco in self.ecossistemas:

            atual = len(set(self.ecossistemas[eco]))

            if atual > qtd:

                qtd = atual
                maior = eco

        print("Maior Ecossistema :", maior)
        print("MÃƒÂ³dulos :", qtd)

        print()

        print("MissÃƒÂ£o seguinte:")

        print()

        print("Descobrir as ligaÃƒÂ§ÃƒÂµes")

        print("entre os ecossistemas.")

        print()

        print("="*70)


# ============================================================

if __name__ == "__main__":

    sistema = EcosystemEngine()

    sistema.analisar()

    sistema.painel()


