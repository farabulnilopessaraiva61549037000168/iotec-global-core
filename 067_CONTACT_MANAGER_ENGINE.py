import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CONTACT MANAGER ENGINE
FASE 09

VersÃƒÂ£o 10.0

Gerenciador Corporativo de Contatos

======================================================================
"""

import sqlite3
from datetime import datetime

DB="iotec.db"


class ContactManager:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabela(self):

        conn=self.conectar()
        cursor=conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS contacts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            contact_name TEXT,

            department TEXT,

            email TEXT,

            phone TEXT,

            whatsapp TEXT,

            city TEXT,

            state TEXT,

            country TEXT,

            source TEXT,

            status TEXT,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ======================================================

    def resumo(self):

        conn=self.conectar()

        cursor=conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM contacts

        """)

        total=cursor.fetchone()[0]

        conn.close()

        return total

    # ======================================================

    def executar(self):

        self.criar_tabela()

        total=self.resumo()

        print()

        print("="*70)
        print("IOTEC CONTACT MANAGER ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("BASE COMERCIAL")

        print()

        print("Contatos...........",total)

        print()

        print("="*70)

        print("ESTRUTURA")

        print()

        print("Empresa")

        print("Nome")

        print("Departamento")

        print("Email")

        print("Telefone")

        print("WhatsApp")

        print("Cidade")

        print("Estado")

        print("PaÃƒÂ­s")

        print("Origem")

        print("Status")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Toda campanha")

        print("deverÃƒÂ¡ possuir")

        print("um pÃƒÂºblico")

        print("definido.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA EVOLUÃƒâ€¡ÃƒÆ'O")

        print()

        print("ImportaÃƒÂ§ÃƒÂ£o CSV")

        print("ImportaÃƒÂ§ÃƒÂ£o Excel")

        print("ImportaÃƒÂ§ÃƒÂ£o CRM")

        print("ImportaÃƒÂ§ÃƒÂ£o API")

        print()

        print("="*70)

        print("CONTACT MANAGER ONLINE")

        print("="*70)


if __name__=="__main__":

    ContactManager().executar()



