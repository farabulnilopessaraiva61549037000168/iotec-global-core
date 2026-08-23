import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CRM PIPELINE ENGINE
FASE 10

VersÃƒÂ£o Enterprise 10.0

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class CRMPipeline:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ==========================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS crm_pipeline(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            lead_id INTEGER UNIQUE,

            current_stage TEXT,

            responsible TEXT,

            next_action TEXT,

            next_contact TEXT,

            probability INTEGER,

            updated_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ==========================================================

    def importar_leads(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT id

        FROM leads

        """)

        leads = cursor.fetchall()

        novos = 0

        for lead in leads:

            cursor.execute("""

            SELECT COUNT(*)

            FROM crm_pipeline

            WHERE lead_id=?

            """,(lead[0],))

            if cursor.fetchone()[0] == 0:

                cursor.execute("""

                INSERT INTO crm_pipeline(

                    lead_id,

                    current_stage,

                    responsible,

                    next_action,

                    next_contact,

                    probability,

                    updated_at

                )

                VALUES(?,?,?,?,?,?,?)

                """,(

                    lead[0],

                    "NOVO",

                    "Comercial",

                    "Primeiro contato",

                    "",

                    10,

                    str(datetime.now())

                ))

                novos += 1

        conn.commit()
        conn.close()

        return novos

    # ==========================================================

    def estatisticas(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT current_stage,
               COUNT(*)

        FROM crm_pipeline

        GROUP BY current_stage

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # ==========================================================

    def executar(self):

        self.criar_tabela()

        novos = self.importar_leads()

        print()

        print("="*70)
        print("IOTEC CRM PIPELINE ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("NOVOS LEADS IMPORTADOS.....",novos)

        print()

        print("="*70)
        print("PIPELINE")
        print("="*70)

        for item in self.estatisticas():

            print(f"{item[0]:20} {item[1]}")

        print()

        print("="*70)

        print("ESTÃƒÂGIOS")

        print()

        print("NOVO")
        print("Ã¢â€ â€œ")
        print("CONTATADO")
        print("Ã¢â€ â€œ")
        print("INTERESSADO")
        print("Ã¢â€ â€œ")
        print("REUNIÃƒÆ'O")
        print("Ã¢â€ â€œ")
        print("PROPOSTA")
        print("Ã¢â€ â€œ")
        print("NEGOCIAÃƒâ€¡ÃƒÆ'O")
        print("Ã¢â€ â€œ")
        print("CONTRATO")
        print("Ã¢â€ â€œ")
        print("CLIENTE")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Nenhum Lead")

        print("pode ficar")

        print("sem acompanhamento.")

        print()

        print("="*70)

        print("CRM PIPELINE ONLINE")

        print("="*70)


if __name__ == "__main__":

    CRMPipeline().executar()



