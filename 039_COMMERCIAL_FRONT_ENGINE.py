"""
======================================================================
IOTEC COMMERCIAL FRONT ENGINE
======================================================================

Gerencia as Frentes Comerciais da IOTEC.

NÃƒÂ£o cria empresas.
NÃƒÂ£o gera dados fictÃƒÂ­cios.

Cada frente representa um mercado onde a IOTEC atua.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class CommercialFrontEngine:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)
        self.cursor = self.db.cursor()

        self.criar_tabelas()

    # ==========================================================

    def criar_tabelas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS frentes_comerciais(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT UNIQUE,

            nome TEXT,

            descricao TEXT,

            hunter TEXT,

            consultor TEXT,

            negociador TEXT,

            status TEXT,

            criado_em TEXT

        )

        """)

        self.db.commit()

    # ==========================================================

    def existe(self,nome):

        self.cursor.execute("""

        SELECT id

        FROM frentes_comerciais

        WHERE nome=?

        """,(nome,))

        return self.cursor.fetchone() is not None

    # ==========================================================

    def cadastrar(self,nome,descricao):

        if self.existe(nome):
            return

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM frentes_comerciais

        """)

        numero=self.cursor.fetchone()[0]+1

        codigo=f"FRT-{numero:03d}"

        self.cursor.execute("""

        INSERT INTO frentes_comerciais(

            codigo,

            nome,

            descricao,

            hunter,

            consultor,

            negociador,

            status,

            criado_em

        )

        VALUES(?,?,?,?,?,?,?,?)

        """,(

            codigo,

            nome,

            descricao,

            "HUNTER",

            "CONSULTOR",

            "NEGOCIADOR",

            "ATIVA",

            datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        ))

        self.db.commit()

    # ==========================================================

    def instalar(self):

        self.cadastrar(
            "CONTABILIDADE",
            "EscritÃƒÂ³rios de contabilidade"
        )

        self.cadastrar(
            "CLÃƒÂNICAS",
            "ClÃƒÂ­nicas mÃƒÂ©dicas e odontolÃƒÂ³gicas"
        )

        self.cadastrar(
            "INDÃƒÅ¡STRIAS",
            "Empresas industriais"
        )

        self.cadastrar(
            "PREFEITURAS",
            "Ãƒâ€œrgÃƒÂ£os pÃƒÂºblicos municipais"
        )

        self.cadastrar(
            "CONSTRUÃƒâ€¡ÃƒÆ'O CIVIL",
            "Construtoras e engenharia"
        )

        self.cadastrar(
            "AGRONEGÃƒâ€œCIO",
            "Produtores e cooperativas"
        )

        self.cadastrar(
            "EDUCAÃƒâ€¡ÃƒÆ'O",
            "Escolas e instituiÃƒÂ§ÃƒÂµes de ensino"
        )

        self.cadastrar(
            "COMÃƒâ€°RCIO",
            "Empresas comerciais"
        )

    # ==========================================================

    def painel(self):

        print("="*70)
        print("IOTEC COMMERCIAL FRONT ENGINE")
        print("="*70)
        print()

        self.cursor.execute("""

        SELECT

        codigo,

        nome,

        status

        FROM frentes_comerciais

        ORDER BY nome

        """)

        dados=self.cursor.fetchall()

        print("FRENTES COMERCIAIS")

        print("-"*70)

        for codigo,nome,status in dados:

            print(f"{codigo:<10}{nome:<30}{status}")

        print()

        print("="*70)

        print("TOTAL :",len(dados))

        print("="*70)

        print()

        print("MISSÃƒÆ'O")

        print()

        print("Todas as frentes estÃƒÂ£o prontas.")

        print("Aguardando empresas reais.")

        print("Aguardando distribuiÃƒÂ§ÃƒÂ£o para Hunters.")

        print()

    # ==========================================================

    def fechar(self):

        self.db.close()


if __name__=="__main__":

    sistema=CommercialFrontEngine()

    sistema.instalar()

    sistema.painel()

    sistema.fechar()


