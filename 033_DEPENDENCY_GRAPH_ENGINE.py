"""
======================================================================
IOTEC DEPENDENCY GRAPH ENGINE
VERSÃƒÆ'O 1.0
======================================================================
"""

import os
import re
import sqlite3
from pathlib import Path

PASTA = r"C:\IOTEC"
DB = "iotec_kernel.db"


class DependencyGraph:

    def __init__(self):

        self.conn = sqlite3.connect(DB, timeout=30)
        self.cursor = self.conn.cursor()

        self.criar_tabela()

        self.modulos = {}

    # ===============================================================

    def criar_tabela(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS dependency_graph(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            modulo TEXT,

            depende_de TEXT,

            tipo TEXT,

            peso INTEGER

        )

        """)

        self.conn.commit()

    # ===============================================================

    def limpar(self):

        self.cursor.execute(

            "DELETE FROM dependency_graph"

        )

        self.conn.commit()

    # ===============================================================

    def descobrir(self):

        print("="*70)
        print("LENDO DEPENDÃƒÅ NCIAS")
        print("="*70)
        print()

        self.limpar()

        total = 0

        for raiz, _, arquivos in os.walk(PASTA):

            for arquivo in arquivos:

                if not arquivo.endswith(".py"):
                    continue

                caminho = os.path.join(raiz, arquivo)

                try:

                    texto = Path(caminho).read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                except:

                    continue

                imports = re.findall(

                    r'^\s*(?:import|from)\s+([A-Za-z0-9_\.]+)',

                    texto,

                    re.MULTILINE

                )

                self.modulos[arquivo] = imports

                total += 1

                for imp in imports:

                    self.cursor.execute("""

                    INSERT INTO dependency_graph(

                        modulo,

                        depende_de,

                        tipo,

                        peso

                    )

                    VALUES(?,?,?,?)

                    """,(

                        arquivo,

                        imp,

                        "IMPORT",

                        1

                    ))

        self.conn.commit()

        print("Arquivos analisados :", total)

        print()

    # ===============================================================

    def painel(self):

        print("="*70)
        print("DEPENDÃƒÅ NCIAS MAIS COMUNS")
        print("="*70)
        print()

        self.cursor.execute("""

        SELECT

            depende_de,

            COUNT(*)

        FROM dependency_graph

        GROUP BY depende_de

        ORDER BY COUNT(*) DESC

        LIMIT 20

        """)

        dados = self.cursor.fetchall()

        for nome, qtd in dados:

            print(f"{nome:<35}{qtd}")

        print()

        print("="*70)
        print("MÃƒâ€œDULOS ANALISADOS")
        print("="*70)

        print()

        print(len(self.modulos))

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print("="*70)

        print()

        print("PrÃƒÂ³xima etapa:")

        print()

        print("Descobrir dependÃƒÂªncias internas.")

        print("Calcular mÃƒÂ³dulos crÃƒÂ­ticos.")

        print("Construir o mapa da plataforma.")

        print()

        print("="*70)

    # ===============================================================

    def fechar(self):

        self.conn.close()


if __name__ == "__main__":

    sistema = DependencyGraph()

    sistema.descobrir()

    sistema.painel()

    sistema.fechar()


