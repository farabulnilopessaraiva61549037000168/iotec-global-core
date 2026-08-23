import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC COMPANY IMPORT ENGINE
FASE 05
ETAPA 004

VersÃƒÂ£o 6.0

Importador Oficial de Empresas

======================================================================
"""

import sqlite3
import csv
from pathlib import Path
from datetime import datetime


class CompanyImportEngine:

    def __init__(self, banco="iotec.db"):

        self.conn = sqlite3.connect(banco)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

        self.importadas = 0
        self.duplicadas = 0
        self.erros = 0

    # =========================================================

    def existe(self, empresa):

        self.cur.execute("""

            SELECT id

            FROM companies

            WHERE UPPER(company_name)=UPPER(?)

        """,(empresa,))

        return self.cur.fetchone() is not None

    # =========================================================

    def cadastrar(self,dados):

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

            dados.get("company_name",""),

            dados.get("segment",""),

            dados.get("city",""),

            dados.get("state",""),

            dados.get("country","Brasil"),

            dados.get("website",""),

            dados.get("linkedin",""),

            dados.get("phone",""),

            dados.get("email",""),

            "NOVA",

            50,

            ""

        ))

        self.conn.commit()

    # =========================================================

    def importar(self,arquivo):

        arquivo = Path(arquivo)

        if not arquivo.exists():

            print()

            print("Arquivo nÃƒÂ£o encontrado.")

            return

        with open(

            arquivo,

            encoding="utf-8-sig",

            newline=""

        ) as csvfile:

            leitor = csv.DictReader(csvfile)

            for linha in leitor:

                try:

                    empresa = linha.get("company_name","").strip()

                    if empresa=="":

                        continue

                    if self.existe(empresa):

                        self.duplicadas += 1

                        continue

                    self.cadastrar(linha)

                    self.importadas += 1

                except Exception:

                    self.erros += 1

    # =========================================================

    def resumo(self):

        print()

        print("="*70)

        print("IOTEC COMPANY IMPORT ENGINE")

        print("="*70)

        print()

        print("Importadas........",self.importadas)

        print("Duplicadas........",self.duplicadas)

        print("Erros.............",self.erros)

        print()

        print("="*70)

        print("IMPORTAÃƒâ€¡ÃƒÆ'O FINALIZADA")

        print("="*70)

    # =========================================================

    def fechar(self):

        self.conn.close()


# ================================================================

if __name__=="__main__":

    print()

    print("="*70)

    print("IOTEC COMPANY IMPORT ENGINE")

    print("="*70)

    print()

    caminho=input(

        "CSV das empresas: "

    ).strip()

    engine=CompanyImportEngine()

    engine.importar(caminho)

    engine.resumo()

    engine.fechar()



