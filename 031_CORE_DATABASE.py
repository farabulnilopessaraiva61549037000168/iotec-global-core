import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORE DATABASE
FASE 05
ETAPA 001

VersÃƒÂ£o 6.0

ÃƒÅ¡NICO MÃƒâ€œDULO AUTORIZADO A ACESSAR O SQLITE

======================================================================
"""

import sqlite3

from pathlib import Path

from datetime import datetime


class CoreDatabase:

    VERSION = "6.0"

    def __init__(self, banco="iotec.db"):

        self.banco = Path(banco)

        self.conn = None

        self.cur = None

    # ------------------------------------------------------------

    def conectar(self):

        self.conn = sqlite3.connect(self.banco)

        self.conn.row_factory = sqlite3.Row

        self.cur = self.conn.cursor()

    # ------------------------------------------------------------

    def fechar(self):

        if self.conn:

            self.conn.close()

    # ------------------------------------------------------------

    def consultar(self, sql, parametros=()):

        self.cur.execute(sql, parametros)

        return self.cur.fetchall()

    # ------------------------------------------------------------

    def consultar_um(self, sql, parametros=()):

        self.cur.execute(sql, parametros)

        return self.cur.fetchone()

    # ------------------------------------------------------------

    def executar(self, sql, parametros=()):

        self.cur.execute(sql, parametros)

        self.conn.commit()

    # ------------------------------------------------------------

    def contar(self, tabela):

        try:

            self.cur.execute(

                f"SELECT COUNT(*) TOTAL FROM {tabela}"

            )

            return self.cur.fetchone()["TOTAL"]

        except:

            return 0

    # ------------------------------------------------------------

    def existe_tabela(self, tabela):

        self.cur.execute("""

            SELECT name

            FROM sqlite_master

            WHERE type='table'

            AND name=?

        """,(tabela,))

        return self.cur.fetchone() is not None

    # ------------------------------------------------------------

    def resumo(self):

        print()

        print("="*70)

        print("IOTEC CORE DATABASE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        tabelas=[

            "companies",

            "leads",

            "campaigns",

            "contracts",

            "products",

            "payments"

        ]

        for tabela in tabelas:

            if self.existe_tabela(tabela):

                total=self.contar(tabela)

                print(f"{tabela:20} {total}")

            else:

                print(f"{tabela:20} NÃƒÆ'O EXISTE")

        print()

        print("="*70)

        print("CORE DATABASE ONLINE")

        print("="*70)


# ===================================================================

if __name__=="__main__":

    core=CoreDatabase()

    core.conectar()

    core.resumo()

    core.fechar()



