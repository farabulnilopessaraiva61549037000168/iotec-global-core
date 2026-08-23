"""
======================================================================
IOTEC
029_LEAD_CAPTURE_ENGINE.py

PARTE 1/3

LEAD CAPTURE ENGINE

ResponsÃƒÂ¡vel por registrar novos clientes
e iniciar o funil comercial.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class LeadCaptureEngine:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)
        self.cursor = self.db.cursor()

        self.criar_tabela()

    # =====================================================

    def criar_tabela(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS clientes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,

            empresa TEXT,

            contato TEXT,

            telefone TEXT,

            email TEXT,

            cidade TEXT,

            segmento TEXT,

            necessidade TEXT,

            origem TEXT,

            status TEXT,

            criado_em TEXT

        )

        """)

        self.db.commit()

    # =====================================================

    def proximo_codigo(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM clientes"
        )

        numero = self.cursor.fetchone()[0] + 1

        return f"CLI-{numero:06d}"

    # =====================================================

    def cadastrar_cliente(
            self,
            empresa,
            contato,
            telefone,
            email,
            cidade,
            segmento,
            necessidade,
            origem
    ):

        codigo = self.proximo_codigo()

        self.cursor.execute("""

        INSERT INTO clientes(

            codigo,
            empresa,
            contato,
            telefone,
            email,
            cidade,
            segmento,
            necessidade,
            origem,
            status,
            criado_em

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """,(

            codigo,
            empresa,
            contato,
            telefone,
            email,
            cidade,
            segmento,
            necessidade,
            origem,
            "NOVO",
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        ))

        self.db.commit()

        print()
        print("="*70)
        print("NOVO LEAD CADASTRADO")
        print("="*70)

        print()

        print("CÃƒÂ³digo.......",codigo)
        print("Empresa......",empresa)
        print("Contato......",contato)
        print("Telefone.....",telefone)
        print("Cidade.......",cidade)
        print("Segmento.....",segmento)
        print("Origem.......",origem)
        print("Status....... NOVO")

        print()

    # =====================================================

    def listar_clientes(self):

        self.cursor.execute("""

        SELECT

            codigo,
            empresa,
            cidade,
            segmento,
            status

        FROM clientes

        ORDER BY id DESC

        """)

        dados = self.cursor.fetchall()

        print("="*70)
        print("CLIENTES CADASTRADOS")
        print("="*70)

        print()

        if len(dados)==0:

            print("Nenhum cliente cadastrado.")
            return

        for c in dados:

            print(c[0])

            print("Empresa.....",c[1])

            print("Cidade......",c[2])

            print("Segmento....",c[3])

            print("Status......",c[4])

            print("-"*60)

    # =====================================================

    def fechar(self):

        self.db.close()


if __name__=="__main__":

    sistema = LeadCaptureEngine()

    # EXEMPLO

    sistema.cadastrar_cliente(

        empresa="EMPRESA DEMONSTRAÃƒâ€¡ÃƒÆ'O",

        contato="ResponsÃƒÂ¡vel",

        telefone="(00)00000-0000",

        email="contato@empresa.com",

        cidade="QuixadÃƒÂ¡",

        segmento="Consultoria",

        necessidade="DiagnÃƒÂ³stico Empresarial",

        origem="Sistema"

    )

    sistema.listar_clientes()

    sistema.fechar()


