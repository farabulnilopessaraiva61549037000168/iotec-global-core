"""
======================================================================
IOTEC

CATÃƒÂLOGO DE PRODUTOS

======================================================================
"""

import sqlite3

from datetime import datetime


class ProductCatalog:

    def __init__(self):

        self.db = sqlite3.connect("iotec_kernel.db")

        self.cursor = self.db.cursor()

        self.criar_tabela()

    # =====================================================

    def criar_tabela(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS produtos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,

            nome TEXT,

            categoria TEXT,

            descricao TEXT,

            problema TEXT,

            publico TEXT,

            preco REAL,

            prazo TEXT,

            status TEXT,

            responsavel TEXT

        )

        """)

        self.db.commit()

    # =====================================================

    def cadastrar(

        self,

        nome,

        categoria,

        descricao,

        problema,

        publico,

        preco,

        prazo,

        responsavel,

        status="PRONTO"

    ):

        self.cursor.execute("""

        INSERT INTO produtos(

            codigo,

            nome,

            categoria,

            descricao,

            problema,

            publico,

            preco,

            prazo,

            status,

            responsavel

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """,(

            "",

            nome,

            categoria,

            descricao,

            problema,

            publico,

            preco,

            prazo,

            status,

            responsavel

        ))

        self.db.commit()

        codigo = f"PRD-{self.cursor.lastrowid:06d}"

        self.cursor.execute("""

        UPDATE produtos

        SET codigo=?

        WHERE id=?

        """,(

            codigo,

            self.cursor.lastrowid

        ))

        self.db.commit()

        print()

        print("Produto cadastrado:",codigo)

    # =====================================================

    def listar(self):

        print()

        print("="*70)

        print("CATÃƒÂLOGO IOTEC")

        print("="*70)

        print()

        self.cursor.execute("""

        SELECT

        codigo,

        nome,

        categoria,

        preco,

        prazo,

        status

        FROM produtos

        ORDER BY nome

        """)

        registros=self.cursor.fetchall()

        for r in registros:

            print()

            print("CÃƒÂ³digo......",r[0])

            print("Produto.....",r[1])

            print("Categoria...",r[2])

            print("PreÃƒÂ§o....... R$",format(r[3],".2f"))

            print("Prazo.......",r[4])

            print("Status......",r[5])

            print("-"*60)

    # =====================================================

    def resumo(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM produtos"

        )

        total=self.cursor.fetchone()[0]

        print()

        print("="*70)

        print("PAINEL DO CATÃƒÂLOGO")

        print("="*70)

        print()

        print("Produtos cadastrados :",total)

        print("Atualizado em :",datetime.now())

        print()

    # =====================================================

    def fechar(self):

        self.db.close()


# ===========================================================

if __name__=="__main__":

    catalogo=ProductCatalog()

    catalogo.cadastrar(

        nome="DiagnÃƒÂ³stico Empresarial",

        categoria="Consultoria",

        descricao="AnÃƒÂ¡lise completa da empresa.",

        problema="IdentificaÃƒÂ§ÃƒÂ£o de gargalos.",

        publico="Empresas",

        preco=500,

        prazo="5 dias",

        responsavel="Comercial"

    )

    catalogo.cadastrar(

        nome="Auditoria TÃƒÂ©cnica",

        categoria="Auditoria",

        descricao="Auditoria especializada.",

        problema="VerificaÃƒÂ§ÃƒÂ£o tÃƒÂ©cnica.",

        publico="Empresas",

        preco=1200,

        prazo="10 dias",

        responsavel="Auditoria"

    )

    catalogo.listar()

    catalogo.resumo()

    catalogo.fechar()


