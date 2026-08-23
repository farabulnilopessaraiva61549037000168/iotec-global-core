import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC LINKEDIN DEPLOYMENT ENGINE
FASE 08

VersÃƒÂ£o 9.0

ImplantaÃƒÂ§ÃƒÂ£o do LinkedIn Corporativo

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class LinkedInDeployment:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS linkedin_config(

            id INTEGER PRIMARY KEY,

            company_name TEXT,

            linkedin_url TEXT,

            slogan TEXT,

            description TEXT,

            logo INTEGER,

            banner INTEGER,

            page_created INTEGER,

            first_post INTEGER,

            followers INTEGER,

            status TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ======================================================

    def executar(self):

        self.criar_tabela()

        print()

        print("="*70)
        print("IOTEC LINKEDIN DEPLOYMENT ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        conn=self.conectar()
        cursor=conn.cursor()

        cursor.execute("SELECT * FROM linkedin_config LIMIT 1")

        dados=cursor.fetchone()

        if dados is None:

            cursor.execute("""

            INSERT INTO linkedin_config(

            company_name,

            linkedin_url,

            slogan,

            description,

            logo,

            banner,

            page_created,

            first_post,

            followers,

            status

            )

            VALUES(?,?,?,?,?,?,?,?,?,?)

            """,(

            "IOTEC",

            "",

            "",

            "",

            0,

            0,

            0,

            0,

            0,

            "EM IMPLANTAÃƒâ€¡ÃƒÆ'O"

            ))

            conn.commit()

            cursor.execute("SELECT * FROM linkedin_config LIMIT 1")

            dados=cursor.fetchone()

        conn.close()

        print()

        print("EMPRESA")

        print(dados[1])

        print()

        print("="*70)

        print("STATUS")

        print()

        print(dados[10])

        print()

        print("="*70)

        print("CHECKLIST")

        print()

        itens=[

            ("PÃƒÂ¡gina criada",dados[7]),

            ("Logo publicada",dados[5]),

            ("Banner publicado",dados[6]),

            ("DescriÃƒÂ§ÃƒÂ£o",1 if dados[4] else 0),

            ("Slogan",1 if dados[3] else 0),

            ("Primeira publicaÃƒÂ§ÃƒÂ£o",dados[8])

        ]

        concluidos=0

        for nome,status in itens:

            if status:

                print("[Ã¢Å"â€œ]",nome)

                concluidos+=1

            else:

                print("[ ]",nome)

        percentual=(concluidos/len(itens))*100

        print()

        print("="*70)

        print("MATURIDADE")

        print()

        print(f"{percentual:.1f}%")

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Preparar o LinkedIn")

        print("como principal canal")

        print("institucional B2B")

        print("da IOTEC.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")

        print()

        print("Criar a pÃƒÂ¡gina oficial")

        print("Publicar logo")

        print("Publicar banner")

        print("Criar primeira postagem")

        print()

        print("="*70)

        print("LINKEDIN DEPLOYMENT ONLINE")

        print("="*70)


if __name__=="__main__":

    LinkedInDeployment().executar()



