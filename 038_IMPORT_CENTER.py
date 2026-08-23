"""
======================================================================
IOTEC IMPORT CENTER
VERSÃƒÆ'O 1.0
======================================================================

Importa empresas REAIS para o banco da IOTEC.

Autor : IOTEC
"""

import sqlite3
import pandas as pd
import os
from datetime import datetime

DB = "iotec_kernel.db"

ARQUIVO = "empresas.xlsx"


class ImportCenter:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)
        self.cursor = self.db.cursor()

        self.criar_tabela()

    # ======================================================

    def criar_tabela(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS empresas(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT UNIQUE,

            nome TEXT,

            cnpj TEXT,

            segmento TEXT,

            cidade TEXT,

            estado TEXT,

            telefone TEXT,

            whatsapp TEXT,

            email TEXT,

            site TEXT,

            linkedin TEXT,

            maps TEXT,

            contato TEXT,

            cargo TEXT,

            status TEXT,

            produto TEXT,

            potencial REAL,

            origem TEXT,

            criado_em TEXT

        )

        """)

        self.db.commit()

    # ======================================================

    def existe(self,nome):

        self.cursor.execute("""

        SELECT id

        FROM empresas

        WHERE UPPER(nome)=UPPER(?)

        """,(nome,))

        return self.cursor.fetchone() is not None

    # ======================================================

    def codigo(self):

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM empresas

        """)

        numero=self.cursor.fetchone()[0]+1

        return f"EMP-{numero:07d}"

    # ======================================================

    def importar(self):

        print("="*70)
        print("IOTEC IMPORT CENTER")
        print("="*70)
        print()

        if not os.path.exists(ARQUIVO):

            print("Arquivo nÃƒÂ£o encontrado:")
            print()
            print(ARQUIVO)
            print()
            print("Coloque a planilha na pasta C:\\IOTEC")
            return

        df=pd.read_excel(ARQUIVO)

        total=0
        ignoradas=0

        for _,linha in df.iterrows():

            nome=str(linha.get("nome","")).strip()

            if nome=="":

                continue

            if self.existe(nome):

                ignoradas+=1

                continue

            self.cursor.execute("""

            INSERT INTO empresas(

                codigo,

                nome,

                cnpj,

                segmento,

                cidade,

                estado,

                telefone,

                whatsapp,

                email,

                site,

                linkedin,

                maps,

                contato,

                cargo,

                status,

                produto,

                potencial,

                origem,

                criado_em

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

            """,(

                self.codigo(),

                nome,

                str(linha.get("cnpj","")),

                str(linha.get("segmento","")),

                str(linha.get("cidade","")),

                str(linha.get("estado","")),

                str(linha.get("telefone","")),

                str(linha.get("whatsapp","")),

                str(linha.get("email","")),

                str(linha.get("site","")),

                str(linha.get("linkedin","")),

                str(linha.get("maps","")),

                str(linha.get("contato","")),

                str(linha.get("cargo","")),

                "NOVO",

                "",

                0,

                "PLANILHA",

                datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            ))

            total+=1

        self.db.commit()

        print()

        print("="*70)
        print("IMPORTAÃƒâ€¡ÃƒÆ'O FINALIZADA")
        print("="*70)

        print()

        print("Empresas importadas :",total)

        print("Duplicadas..........",ignoradas)

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM empresas

        """)

        print("Total no banco......",self.cursor.fetchone()[0])

        print()

    # ======================================================

    def painel(self):

        print("="*70)
        print("BASE COMERCIAL")
        print("="*70)

        self.cursor.execute("""

        SELECT

        segmento,

        COUNT(*)

        FROM empresas

        GROUP BY segmento

        ORDER BY COUNT(*) DESC

        """)

        print()

        for segmento,total in self.cursor.fetchall():

            print(f"{segmento:<30}{total}")

        print()

    # ======================================================

    def fechar(self):

        self.db.close()


if __name__=="__main__":

    sistema=ImportCenter()

    sistema.importar()

    sistema.painel()

    sistema.fechar()


