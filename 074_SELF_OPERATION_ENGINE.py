import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC SELF OPERATION ENGINE
VersÃƒÂ£o Enterprise 10.0

A IOTEC ÃƒÂ© o primeiro laboratÃƒÂ³rio
de suas prÃƒÂ³prias tecnologias.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class SelfOperationEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =========================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS self_operation(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            technology TEXT,

            version TEXT,

            status TEXT,

            validated INTEGER,

            commercial_release INTEGER,

            observations TEXT,

            created_at TEXT,

            updated_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # =========================================================

    def registrar_tecnologias(self):

        tecnologias = [

            ("Kernel IOTEC","10.0","EM USO",1,1),

            ("Executive Reasoning","10.0","EM USO",1,1),

            ("Corporate Dossier","10.0","EM USO",1,1),

            ("Campaign Engine","10.0","EM USO",1,1),

            ("Lead Engine","10.0","EM USO",1,1),

            ("CRM Pipeline","10.0","EM USO",1,1),

            ("Knowledge Core","10.0","EM USO",1,1),

            ("Adaptive Motors","1.0","EM PESQUISA",0,0),

            ("Learning Engine","1.0","EM PESQUISA",0,0),

            ("Technology Licensing","1.0","PLANEJADO",0,0)

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for item in tecnologias:

            cursor.execute("""

            INSERT OR IGNORE INTO self_operation(

                technology,

                version,

                status,

                validated,

                commercial_release,

                observations,

                created_at,

                updated_at

            )

            VALUES(?,?,?,?,?,?,?,?)

            """,(

                item[0],

                item[1],

                item[2],

                item[3],

                item[4],

                "Tecnologia utilizada internamente.",

                str(datetime.now()),

                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    # =========================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        technology,

        version,

        status,

        validated,

        commercial_release

        FROM self_operation

        ORDER BY technology

        """)

        dados = cursor.fetchall()

        conn.close()

        print()

        print("="*70)
        print("IOTEC SELF OPERATION ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("TECNOLOGIAS")

        print()

        for t in dados:

            print(t[0])

            print("VersÃƒÂ£o.............",t[1])
            print("Status.............",t[2])
            print("Validada...........", "SIM" if t[3] else "NÃƒÆ'O")
            print("Liberada...........", "SIM" if t[4] else "NÃƒÆ'O")

            print()

        print("="*70)

        print("PRINCÃƒÂPIO")

        print()

        print("Toda tecnologia")

        print("desenvolvida")

        print("pela IOTEC")

        print("deverÃƒÂ¡ ser")

        print("utilizada")

        print("internamente")

        print("antes da")

        print("implantaÃƒÂ§ÃƒÂ£o")

        print("em clientes.")

        print()

        print("="*70)

        print("BENEFÃƒÂCIOS")

        print()

        print("Ã¢Å"â€œ ValidaÃƒÂ§ÃƒÂ£o")

        print("Ã¢Å"â€œ Aprendizagem")

        print("Ã¢Å"â€œ EvoluÃƒÂ§ÃƒÂ£o")

        print("Ã¢Å"â€œ Estudos de Caso")

        print("Ã¢Å"â€œ Credibilidade")

        print("Ã¢Å"â€œ DemonstraÃƒÂ§ÃƒÂ£o Comercial")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("A IOTEC")

        print("nÃƒÂ£o vende")

        print("tecnologias")

        print("que nÃƒÂ£o")

        print("utiliza.")

        print()

        print("="*70)

        print("SELF OPERATION ONLINE")

        print("="*70)

    # =========================================================

    def executar(self):

        self.criar_tabela()

        self.registrar_tecnologias()

        self.mostrar()


if __name__ == "__main__":

    SelfOperationEngine().executar()



