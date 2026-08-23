"""
======================================================================
IOTEC
024_ARCHITECTURE_DISCOVERY_ENGINE.py

ARCHITECTURE DISCOVERY ENGINE
PARTE 1

Descobre automaticamente toda a arquitetura da plataforma.

======================================================================
"""

import os
import ast
from pathlib import Path
from datetime import datetime

PASTA_RAIZ = r"C:\IOTEC"


class ArchitectureDiscoveryEngine:

    def __init__(self):

        self.modulos = []

        self.total_classes = 0
        self.total_funcoes = 0
        self.total_imports = 0
        self.total_linhas = 0
        self.total_erros = 0

    # ======================================================

    def analisar_pasta(self):

        print("=" * 70)
        print("IOTEC ARCHITECTURE DISCOVERY ENGINE")
        print("=" * 70)
        print()

        print("Procurando mÃƒÂ³dulos...")
        print()

        for raiz, _, arquivos in os.walk(PASTA_RAIZ):

            for arquivo in arquivos:

                if arquivo.endswith(".py"):

                    caminho = os.path.join(raiz, arquivo)

                    self.analisar_arquivo(caminho)

        print()

        print("Arquivos encontrados:", len(self.modulos))
        print()

    # ======================================================

    def analisar_arquivo(self, caminho):

        try:

            texto = Path(caminho).read_text(
                encoding="utf-8",
                errors="ignore"
            )

        except Exception:

            return

        linhas = len(texto.splitlines())

        tamanho = round(
            os.path.getsize(caminho) / 1024,
            2
        )

        self.total_linhas += linhas

        try:

            arvore = ast.parse(texto)

        except SyntaxError:

            self.total_erros += 1

            self.modulos.append({

                "arquivo": os.path.basename(caminho),

                "linhas": linhas,

                "kb": tamanho,

                "classes": 0,

                "funcoes": 0,

                "imports": 0,

                "status": "ERRO DE SINTAXE"

            })

            return

        classes = 0
        funcoes = 0
        imports = 0

        for node in ast.walk(arvore):

            if isinstance(node, ast.ClassDef):
                classes += 1

            elif isinstance(node, ast.FunctionDef):
                funcoes += 1

            elif isinstance(node, ast.Import):
                imports += len(node.names)

            elif isinstance(node, ast.ImportFrom):
                imports += len(node.names)

        self.total_classes += classes
        self.total_funcoes += funcoes
        self.total_imports += imports

        self.modulos.append({

            "arquivo": os.path.basename(caminho),

            "linhas": linhas,

            "kb": tamanho,

            "classes": classes,

            "funcoes": funcoes,

            "imports": imports,

            "status": "OK"

        })

    # ======================================================

    def painel(self):

        print("=" * 70)
        print("RESUMO DA ARQUITETURA")
        print("=" * 70)
        print()

        print(f"MÃƒÂ³dulos............. {len(self.modulos)}")
        print(f"Classes............ {self.total_classes}")
        print(f"FunÃƒÂ§ÃƒÂµes............ {self.total_funcoes}")
        print(f"Imports............ {self.total_imports}")
        print(f"Linhas............. {self.total_linhas}")
        print(f"Erros.............. {self.total_erros}")

        print()

        print("=" * 70)
        print("PRIMEIROS 20 MÃƒâ€œDULOS")
        print("=" * 70)
        print()

        for modulo in self.modulos[:20]:

            print(f"{modulo['arquivo']:<40}", end="")

            print(
                f"C:{modulo['classes']:>3}  "
                f"F:{modulo['funcoes']:>3}  "
                f"I:{modulo['imports']:>3}  "
                f"L:{modulo['linhas']:>5}  "
                f"{modulo['status']}"
            )

        print()

        print("=" * 70)

        print()

        print("RelatÃƒÂ³rio gerado em:")

        print(datetime.now())

        print("=" * 70)


# ==========================================================

if __name__ == "__main__":

    engine = ArchitectureDiscoveryEngine()

    engine.analisar_pasta()

    engine.painel()


