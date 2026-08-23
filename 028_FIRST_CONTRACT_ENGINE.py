"""
======================================================================
IOTEC
028_FIRST_CONTRACT_ENGINE.py

PARTE 1/3

FIRST CONTRACT ENGINE

MissÃƒÂ£o:
Conduzir a IOTEC atÃƒÂ© o primeiro contrato comercial.

======================================================================
"""

import sqlite3
from datetime import datetime

# ==========================================================
# BANCO
# ==========================================================

DB = "iotec_kernel.db"


class FirstContractEngine:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)

        self.cursor = self.db.cursor()

        self.criar_tabelas()

    # ======================================================

    def criar_tabelas(self):

        # -------------------------------
        # CLIENTES
        # -------------------------------

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS clientes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,

            empresa TEXT,

            contato TEXT,

            email TEXT,

            telefone TEXT,

            cidade TEXT,

            segmento TEXT,

            origem TEXT,

            status TEXT,

            criado_em TEXT

        )

        """)

        # -------------------------------
        # PROPOSTAS
        # -------------------------------

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS propostas(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,

            cliente TEXT,

            produto TEXT,

            valor REAL,

            status TEXT,

            criado_em TEXT

        )

        """)

        # -------------------------------
        # CONTRATOS
        # -------------------------------

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS contratos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,

            cliente TEXT,

            produto TEXT,

            valor REAL,

            status TEXT,

            criado_em TEXT

        )

        """)

        self.db.commit()

    # ======================================================

    def contar(self, tabela):

        try:

            self.cursor.execute(

                f"SELECT COUNT(*) FROM {tabela}"

            )

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ======================================================

    def contar_status(self, tabela, status):

        try:

            self.cursor.execute(

                f"SELECT COUNT(*) FROM {tabela} WHERE status=?",

                (status,)

            )

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ======================================================

    def painel(self):

        print("="*70)
        print("IOTEC FIRST CONTRACT ENGINE")
        print("="*70)
        print()

        print("Data :",datetime.now().strftime("%d/%m/%Y"))
        print("Hora :",datetime.now().strftime("%H:%M:%S"))

        print()

        print("="*70)
        print("META PRINCIPAL")
        print("="*70)

        print()

        print("FECHAR O PRIMEIRO CONTRATO DA IOTEC")

        print()

        print("="*70)
        print("INDICADORES")
        print("="*70)

        print()

        produtos = self.contar("produtos")

        clientes = self.contar("clientes")

        propostas = self.contar("propostas")

        contratos = self.contar("contratos")

        print(f"Produtos............... {produtos}")

        print(f"Clientes............... {clientes}")

        print(f"Propostas.............. {propostas}")

        print(f"Contratos.............. {contratos}")

        print()

        print("="*70)

    # ======================================================

    def fechar(self):

        self.db.close()


# ==========================================================

if __name__=="__main__":

    sistema=FirstContractEngine()

    sistema.painel()

    sistema.fechar()


