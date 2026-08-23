import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC COMPANY REPOSITORY
FASE 05
ETAPA 003

VersÃƒÂ£o 6.0

ResponsÃƒÂ¡vel pela tabela companies

======================================================================
"""

import sqlite3
from datetime import datetime


class CompanyRepository:

    def __init__(self, banco="iotec.db"):

        self.conn = sqlite3.connect(banco)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

    # ==========================================================
    # CADASTRAR
    # ==========================================================

    def cadastrar(

        self,

        company_name,
        segment="",
        city="",
        state="",
        country="Brasil",
        website="",
        linkedin="",
        phone="",
        email="",
        status="NOVA",
        opportunity_score=50,
        notes=""

    ):

        self.cur.execute("""

        INSERT INTO companies(

            created_at,

            company_name,

            segment,

            city,

            state,

            country,

            website,

            linkedin,

            phone,

            email,

            status,

            opportunity_score,

            notes

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?,?,?,?,?

        )

        """,(

            str(datetime.now()),

            company_name,

            segment,

            city,

            state,

            country,

            website,

            linkedin,

            phone,

            email,

            status,

            opportunity_score,

            notes

        ))

        self.conn.commit()

    # ==========================================================
    # LISTAR
    # ==========================================================

    def listar(self):

        self.cur.execute("""

            SELECT *

            FROM companies

            ORDER BY company_name

        """)

        return self.cur.fetchall()

    # ==========================================================
    # PESQUISAR
    # ==========================================================

    def pesquisar(self,nome):

        self.cur.execute("""

            SELECT *

            FROM companies

            WHERE company_name LIKE ?

            ORDER BY company_name

        """,(f"%{nome}%",))

        return self.cur.fetchall()

    # ==========================================================
    # ATUALIZAR STATUS
    # ==========================================================

    def atualizar_status(self,id_empresa,status):

        self.cur.execute("""

            UPDATE companies

            SET status=?

            WHERE id=?

        """,(status,id_empresa))

        self.conn.commit()

    # ==========================================================
    # REMOVER
    # ==========================================================

    def remover(self,id_empresa):

        self.cur.execute("""

            DELETE FROM companies

            WHERE id=?

        """,(id_empresa,))

        self.conn.commit()

    # ==========================================================
    # FECHAR
    # ==========================================================

    def fechar(self):

        self.conn.close()


# ======================================================================

if __name__=="__main__":

    repo = CompanyRepository()

    print()

    print("="*70)

    print("IOTEC COMPANY REPOSITORY")

    print("="*70)

    print()

    print("Empresas cadastradas:")

    print()

    empresas = repo.listar()

    if not empresas:

        print("Nenhuma empresa cadastrada.")

    else:

        for empresa in empresas:

            print(

                empresa["id"],

                empresa["company_name"],

                empresa["city"],

                empresa["status"]

            )

    print()

    print("="*70)

    print("COMPANY REPOSITORY ONLINE")

    print("="*70)

    repo.fechar()



