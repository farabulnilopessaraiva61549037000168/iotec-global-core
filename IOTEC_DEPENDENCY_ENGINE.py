import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
==============================================================================
IOTEC DEPENDENCY ENGINE
VersÃƒÂ£o 1.0

MISSÃƒÆ'O

Descobrir as dependÃƒÂªncias entre os mÃƒÂ³dulos Python da IOTEC.

Nesta primeira versÃƒÂ£o sÃƒÂ£o identificados:

- Arquivos Python
- Imports
- Quantidade de dependÃƒÂªncias

==============================================================================

"""

import os
import ast

ROOT = r"C:\IOTEC"


class DependencyEngine:

    def __init__(self):

        self.modules = {}

    def banner(self):

        print("=" * 70)
        print("IOTEC DEPENDENCY ENGINE")
        print("=" * 70)

    def scan(self):

        print("\nANALISANDO DEPENDÃƒÅ NCIAS...\n")

        for root, _, files in os.walk(ROOT):

            for file in files:

                if not file.endswith(".py"):
                    continue

                path = os.path.join(root, file)

                imports = []

                try:

                    with open(path,
                              "r",
                              encoding="utf-8",
                              errors="ignore") as f:

                        tree = ast.parse(f.read())

                    for node in ast.walk(tree):

                        if isinstance(node, ast.Import):

                            for alias in node.names:
                                imports.append(alias.name)

                        elif isinstance(node, ast.ImportFrom):

                            if node.module:
                                imports.append(node.module)

                except Exception as e:

                    imports.append(f"ERRO: {e}")

                self.modules[path] = imports

    def report(self):

        print("=" * 70)
        print("MAPA DE DEPENDÃƒÅ NCIAS")
        print("=" * 70)

        total = 0

        for module, deps in self.modules.items():

            print(f"\n{module}")

            if deps:

                for dep in sorted(set(deps)):
                    print(f"   -> {dep}")
                    total += 1

            else:

                print("   -> Nenhuma dependÃƒÂªncia encontrada")

        print("\n" + "=" * 70)
        print("RESUMO")
        print("=" * 70)

        print("Arquivos Python :", len(self.modules))
        print("DependÃƒÂªncias    :", total)
        print("=" * 70)


def main():

    engine = DependencyEngine()

    engine.banner()

    engine.scan()

    engine.report()


if __name__ == "__main__":

    main()



