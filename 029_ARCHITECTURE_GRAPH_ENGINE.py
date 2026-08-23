# ==============================================================================
# IOTEC
# 029_ARCHITECTURE_GRAPH_ENGINE.py
#
# ConstrÃ³i o grafo arquitetural da plataforma
# usando o kernel_registry.json
# ==============================================================================

import json
from collections import defaultdict

# ==============================================================================

class ArchitectureGraph:

    def __init__(self):

        self.modulos = []

        self.grafo = defaultdict(list)

        self.reverse = defaultdict(list)

    # -------------------------------------------------------------------------

    def carregar(self):

        with open(
            "kernel_registry.json",
            "r",
            encoding="utf-8"
        ) as f:

            self.modulos = json.load(f)

    # -------------------------------------------------------------------------

    def construir(self):

        for modulo in self.modulos:

            nome = modulo["nome"]

            for dep in modulo["dependencias"]:

                self.grafo[nome].append(dep)

                self.reverse[dep].append(nome)

    # -------------------------------------------------------------------------

    def imprimir_resumo(self):

        print()

        print("=" * 100)
        print("IOTEC - GRAFO DA ARQUITETURA")
        print("=" * 100)

        print()

        print(f"MÃ³dulos registrados : {len(self.modulos)}")

        print(f"NÃ³s do grafo....... : {len(self.grafo)}")

        print()

        print("=" * 100)

        print("DEPENDÃŠNCIAS")

        print("=" * 100)

        for modulo, deps in sorted(self.grafo.items()):

            print()

            print(modulo)

            if deps:

                for d in deps:

                    print("   â""â"€â"€", d)

            else:

                print("   (sem dependÃªncias)")

        print()

        print("=" * 100)

        print("MÃ"DULOS MAIS UTILIZADOS")

        print("=" * 100)

        ranking = sorted(

            self.reverse.items(),

            key=lambda x: len(x[1]),

            reverse=True

        )

        for dep, usuarios in ranking[:20]:

            print(

                f"{dep:<20} {len(usuarios):>5}"

            )

# ==============================================================================

if __name__ == "__main__":

    g = ArchitectureGraph()

    g.carregar()

    g.construir()

    g.imprimir_resumo()

