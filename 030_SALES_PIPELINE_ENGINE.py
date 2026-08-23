"""
======================================================================
IOTEC
030_SALES_PIPELINE_ENGINE.py

SALES PIPELINE ENGINE

Gerencia automaticamente o funil comercial.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class SalesPipeline:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)

        self.cursor = self.db.cursor()

    # ============================================================

    def listar(self):

        self.cursor.execute("""

        SELECT

            codigo,
            empresa,
            status

        FROM clientes

        ORDER BY id

        """)

        return self.cursor.fetchall()

    # ============================================================

    def atualizar_status(self,codigo,novo_status):

        self.cursor.execute("""

        UPDATE clientes

        SET status=?

        WHERE codigo=?

        """,(novo_status,codigo))

        self.db.commit()

        print()
        print("="*60)
        print("STATUS ATUALIZADO")
        print("="*60)

        print()

        print("Cliente :",codigo)

        print("Novo Status :",novo_status)

        print()

    # ============================================================

    def painel(self):

        print("="*70)
        print("IOTEC SALES PIPELINE")
        print("="*70)

        etapas=[

            "NOVO",

            "CONTATO",

            "REUNIÃƒÆ'O",

            "PROPOSTA",

            "NEGOCIAÃƒâ€¡ÃƒÆ'O",

            "CONTRATO",

            "PRODUÃƒâ€¡ÃƒÆ'O",

            "ENTREGUE"

        ]

        print()

        total=0

        for etapa in etapas:

            self.cursor.execute(

                """

                SELECT COUNT(*)

                FROM clientes

                WHERE status=?

                """,

                (etapa,)

            )

            qtd=self.cursor.fetchone()[0]

            total+=qtd

            print(f"{etapa:<15}{qtd}")

        print()

        print("="*70)

        print(f"TOTAL DE CLIENTES : {total}")

        print("="*70)

    # ============================================================

    def mostrar_clientes(self):

        print()

        print("="*70)

        print("CLIENTES")

        print("="*70)

        print()

        clientes=self.listar()

        if len(clientes)==0:

            print("Nenhum cliente.")

            return

        for c in clientes:

            print(c[0])

            print("Empresa :",c[1])

            print("Status  :",c[2])

            print("-"*50)

    # ============================================================

    def fechar(self):

        self.db.close()


# ================================================================

if __name__=="__main__":

    sistema=SalesPipeline()

    sistema.painel()

    sistema.mostrar_clientes()

    #
    # DEMONSTRAÃƒâ€¡ÃƒÆ'O
    #
    sistema.atualizar_status(

        "CLI-000001",

        "CONTATO"

    )

    sistema.painel()

    sistema.fechar()


