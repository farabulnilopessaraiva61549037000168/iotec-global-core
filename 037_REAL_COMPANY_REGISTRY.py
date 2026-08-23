import sqlite3
import csv
import os
from datetime import datetime

DB = "iotec_kernel.db"
CSV = "empresas.csv"


class RealCompanyRegistry:

    def __init__(self):

        self.conn = sqlite3.connect(DB, timeout=30)
        self.cursor = self.conn.cursor()

        self.criar_tabela()

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

            email TEXT,

            site TEXT,

            linkedin TEXT,

            google_maps TEXT,

            origem TEXT,

            status TEXT,

            criado_em TEXT

        )

        """)

        self.conn.commit()

    def proximo_codigo(self):

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM empresas

        """)

        numero = self.cursor.fetchone()[0] + 1

        return f"EMP-{numero:06d}"

    def empresa_existe(self, nome):

        self.cursor.execute("""

        SELECT id

        FROM empresas

        WHERE UPPER(nome)=UPPER(?)

        """, (nome,))

        return self.cursor.fetchone() is not None

    def importar_csv(self):

        if not os.path.exists(CSV):

            print("=" * 70)
            print("ARQUIVO NÃƒÆ'O ENCONTRADO")
            print("=" * 70)
            print()
            print("Coloque um arquivo chamado:")
            print()
            print(CSV)
            print()
            print("na pasta C:\\IOTEC")
            print()

            return

        total = 0

        with open(CSV, encoding="utf-8-sig") as arquivo:

            leitor = csv.DictReader(arquivo)

            for linha in leitor:

                nome = linha.get("nome", "").strip()

                if nome == "":
                    continue

                if self.empresa_existe(nome):
                    continue

                codigo = self.proximo_codigo()

                self.cursor.execute("""

                INSERT INTO empresas(

                    codigo,

                    nome,

                    cnpj,

                    segmento,

                    cidade,

                    estado,

                    telefone,

                    email,

                    site,

                    linkedin,

                    google_maps,

                    origem,

                    status,

                    criado_em

                )

                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)

                """, (

                    codigo,

                    nome,

                    linha.get("cnpj", ""),

                    linha.get("segmento", ""),

                    linha.get("cidade", ""),

                    linha.get("estado", ""),

                    linha.get("telefone", ""),

                    linha.get("email", ""),

                    linha.get("site", ""),

                    linha.get("linkedin", ""),

                    linha.get("google_maps", ""),

                    "CSV",

                    "NOVO",

                    datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                ))

                total += 1

        self.conn.commit()

        print("=" * 70)
        print("IMPORTAÃƒâ€¡ÃƒÆ'O FINALIZADA")
        print("=" * 70)
        print()

        print("Empresas importadas:", total)
        print()

    def painel(self):

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM empresas

        """)

        total = self.cursor.fetchone()[0]

        print("=" * 70)
        print("REAL COMPANY REGISTRY")
        print("=" * 70)
        print()

        print("Empresas cadastradas:", total)

        print()

        self.cursor.execute("""

        SELECT

            codigo,

            nome,

            cidade,

            segmento

        FROM empresas

        ORDER BY nome

        LIMIT 20

        """)

        for empresa in self.cursor.fetchall():

            print()

            print(empresa[0])

            print(empresa[1])

            print(empresa[2])

            print(empresa[3])

            print("-" * 50)

    def fechar(self):

        self.conn.close()


if __name__ == "__main__":

    sistema = RealCompanyRegistry()

    sistema.importar_csv()

    sistema.painel()

    sistema.fechar()


