"""
======================================================================
IOTEC CAPABILITY GENOME ENGINE
VERSÃƒÆ'O 1.0
======================================================================

O DNA da IOTEC.

Descobre capacidades.
Organiza conhecimento.
ConstrÃƒÂ³i o mapa genÃƒÂ©tico da plataforma.

======================================================================
"""

import os
import sqlite3
from pathlib import Path
from collections import defaultdict
from datetime import datetime

PASTA = r"C:\IOTEC"
DB = "iotec_kernel.db"


class GenomeEngine:

    def __init__(self):

        self.conn = sqlite3.connect(DB, timeout=30)
        self.cursor = self.conn.cursor()

        self.criar_tabelas()

        self.capacidades = defaultdict(int)

        self.modulos = []

    # ============================================================

    def criar_tabelas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS genome(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            arquivo TEXT,

            linhas INTEGER,

            categoria TEXT,

            capacidade TEXT,

            maturidade INTEGER,

            receita INTEGER,

            atualizado TEXT

        )

        """)

        self.conn.commit()

    # ============================================================

    def classificar(self, texto):

        texto = texto.upper()

        regras = {

            "COMERCIAL":"COMERCIAL",

            "CRM":"CRM",

            "FINANCEIRO":"FINANCEIRO",

            "CONTRATO":"JURIDICO",

            "JURIDICO":"JURIDICO",

            "LOGIST":"LOGISTICA",

            "PRODUTO":"PRODUTOS",

            "CATALOGO":"PRODUTOS",

            "KERNEL":"KERNEL",

            "MISSION":"MISSOES",

            "AGENTE":"AGENTES",

            "INTELIG":"INTELIGENCIA",

            "DASHBOARD":"DASHBOARD",

            "AUDITOR":"AUDITORIA"

        }

        categorias = []

        for palavra, categoria in regras.items():

            if palavra in texto:

                categorias.append(categoria)

        if len(categorias) == 0:

            categorias.append("GERAL")

        return list(set(categorias))

    # ============================================================

    def analisar(self):

        print("="*70)
        print("LENDO DNA DA IOTEC")
        print("="*70)
        print()

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

                categorias = self.classificar(texto)

                linhas = len(texto.splitlines())

                total += 1

                for categoria in categorias:

                    self.capacidades[categoria] += 1

                    self.cursor.execute("""

                    INSERT INTO genome(

                        arquivo,

                        linhas,

                        categoria,

                        capacidade,

                        maturidade,

                        receita,

                        atualizado

                    )

                    VALUES(?,?,?,?,?,?,?)

                    """,(

                        arquivo,

                        linhas,

                        categoria,

                        categoria,

                        0,

                        0,

                        datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                    ))

        self.conn.commit()

        print("Arquivos analisados:", total)
        print()

    # ============================================================

    def painel(self):

        print("="*70)
        print("GENOMA DA IOTEC")
        print("="*70)
        print()

        for nome, quantidade in sorted(self.capacidades.items()):

            print(f"{nome:<20}{quantidade}")

        print()

        print("="*70)
        print("MISSÃƒÆ'O")
        print("="*70)
        print()

        print("Agora o Kernel conhece")
        print("o DNA tecnolÃƒÂ³gico da IOTEC.")
        print()

        print("PrÃƒÂ³xima etapa:")
        print()

        print("Descobrir maturidade.")

        print("Descobrir receita.")

        print("Descobrir produtos.")

        print("Descobrir integraÃƒÂ§ÃƒÂµes.")

        print()

        print("="*70)

    # ============================================================

    def fechar(self):

        self.conn.close()


if __name__ == "__main__":

    sistema = GenomeEngine()

    sistema.analisar()

    sistema.painel()

    sistema.fechar()


