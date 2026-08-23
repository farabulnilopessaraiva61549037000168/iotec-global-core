"""
======================================================================
040_COMMERCIAL_WAR_ROOM.py
======================================================================

IOTEC COMMERCIAL WAR ROOM

Centro de Comando Comercial

VersÃƒÂ£o 1.0
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class CommercialWarRoom:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)
        self.cursor = self.db.cursor()

    # ==========================================================

    def existe(self, tabela):

        self.cursor.execute("""

        SELECT name

        FROM sqlite_master

        WHERE type='table'

        AND name=?

        """,(tabela,))

        return self.cursor.fetchone() is not None

    # ==========================================================

    def contar(self, tabela):

        if not self.existe(tabela):
            return 0

        try:

            self.cursor.execute(

                f"SELECT COUNT(*) FROM {tabela}"

            )

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ==========================================================

    def receita(self):

        if not self.existe("contratos"):
            return 0

        try:

            self.cursor.execute("""

            SELECT IFNULL(SUM(valor),0)

            FROM contratos

            WHERE status='PAGO'

            """)

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ==========================================================

    def painel_frentes(self):

        print("="*70)
        print("FRENTES COMERCIAIS")
        print("="*70)
        print()

        if not self.existe("frentes_comerciais"):

            print("Nenhuma frente cadastrada.")
            return

        self.cursor.execute("""

        SELECT

        codigo,

        nome,

        status

        FROM frentes_comerciais

        ORDER BY nome

        """)

        dados=self.cursor.fetchall()

        empresas=self.contar("empresas")
        propostas=self.contar("propostas")
        contratos=self.contar("contratos")

        for codigo,nome,status in dados:

            print(f"{codigo} - {nome}")

            print("Status........",status)
            print("Empresas......",empresas)
            print("Propostas.....",propostas)
            print("Contratos.....",contratos)

            print("-"*60)

    # ==========================================================

    def missoes(self):

        print()
        print("="*70)
        print("MISSÃƒâ€¢ES AUTOMÃƒÂTICAS")
        print("="*70)
        print()

        empresas=self.contar("empresas")
        propostas=self.contar("propostas")
        contratos=self.contar("contratos")

        if empresas==0:

            print("MISSÃƒÆ'O 001")

            print("Construir base comercial.")

            print()

        if empresas>0 and propostas==0:

            print("MISSÃƒÆ'O 002")

            print("Gerar propostas.")

            print()

        if propostas>0 and contratos==0:

            print("MISSÃƒÆ'O 003")

            print("Converter propostas em contratos.")

            print()

        if contratos>0:

            print("MISSÃƒÆ'O 004")

            print("Executar produÃƒÂ§ÃƒÂ£o.")

            print()

    # ==========================================================

    def painel(self):

        print("="*70)
        print("IOTEC COMMERCIAL WAR ROOM")
        print("="*70)

        print()

        print("Data :",datetime.now().strftime("%d/%m/%Y"))

        print("Hora :",datetime.now().strftime("%H:%M:%S"))

        print()

        print("="*70)
        print("INDICADORES")
        print("="*70)

        print()

        print("Empresas........",self.contar("empresas"))

        print("Produtos........",self.contar("produtos"))

        print("Clientes........",self.contar("clientes"))

        print("Frentes.........",self.contar("frentes_comerciais"))

        print("Propostas.......",self.contar("propostas"))

        print("Contratos.......",self.contar("contratos"))

        print("Receita......... R$ %.2f"%self.receita())

        print()

        self.painel_frentes()

        self.missoes()

        print("="*70)

        print("OBJETIVO")

        print("="*70)

        print()

        print("Transformar empresas")

        print("em contratos.")

        print()

        print("="*70)

    # ==========================================================

    def fechar(self):

        self.db.close()


if __name__=="__main__":

    sistema=CommercialWarRoom()

    sistema.painel()

    sistema.fechar()


