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
IOTEC ARCHITECTURE SCANNER
VERSÃƒÆ'O 1.0

MISSÃƒÆ'O

Escanear automaticamente toda a arquitetura da IOTEC.

Descobrir:

Ã¢â‚¬Â¢ Arquivos Python
Ã¢â‚¬Â¢ Pastas
Ã¢â‚¬Â¢ Quantidade de linhas
Ã¢â‚¬Â¢ Tamanho dos arquivos
Ã¢â‚¬Â¢ Estrutura do projeto
==============================================================================

"""

import os

ROOT = r"C:\IOTEC"


class ArchitectureScanner:

    def __init__(self):

        self.total_files = 0
        self.total_lines = 0
        self.total_size = 0

    def banner(self):

        print("=" * 70)
        print("IOTEC ARCHITECTURE SCANNER")
        print("=" * 70)

    def scan(self):

        print("\nESCANEANDO PROJETO...\n")

        for root, dirs, files in os.walk(ROOT):

            print(f"\nPASTA: {root}")

            for file in files:

                path = os.path.join(root, file)

                self.total_files += 1

                size = os.path.getsize(path)
                self.total_size += size

                lines = 0

                if file.endswith(".py"):

                    try:

                        with open(path,
                                  "r",
                                  encoding="utf-8",
                                  errors="ignore") as f:

                            lines = len(f.readlines())

                    except:

                        pass

                self.total_lines += lines

                print(
                    f"   {file:45} {lines:6} linhas   {size:10} bytes"
                )

    def summary(self):

        print("\n")
        print("=" * 70)
        print("RESUMO")
        print("=" * 70)

        print("Arquivos encontrados :", self.total_files)
        print("Linhas de cÃƒÂ³digo     :", self.total_lines)
        print("EspaÃƒÂ§o utilizado     :", round(self.total_size / 1024 / 1024, 2), "MB")

        print("=" * 70)


def main():

    scanner = ArchitectureScanner()

    scanner.banner()

    scanner.scan()

    scanner.summary()


if __name__ == "__main__":

    main()



