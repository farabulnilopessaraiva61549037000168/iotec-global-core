import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CONTACT IMPORT ENGINE
FASE 09

VersÃƒÂ£o 10.0

Importador Corporativo de Contatos

======================================================================
"""

import sqlite3
import csv
import os
from datetime import datetime

DB = "iotec.db"


class ContactImportEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =====================================================

    def importar_csv(self, arquivo):

        if not os.path.exists(arquivo):

            print()
            print("Arquivo nÃƒÂ£o encontrado.")
            return

        conn = self.conectar()
        cursor = conn.cursor()

        total = 0

        with open(arquivo, encoding="utf-8-sig") as csvfile:

            leitor = csv.DictReader(csvfile)

            for linha in leitor:

                cursor.execute("""

                INSERT INTO contacts(

                    company,
                    contact_name,
                    department,
                    email,
                    phone,
                    whatsapp,
                    city,
                    state,
                    country,
                    source,
                    status,
                    created_at

                )

                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

                """,(

                    linha.get("company",""),
                    linha.get("contact_name",""),
                    linha.get("department",""),
                    linha.get("email",""),
                    linha.get("phone",""),
                    linha.get("whatsapp",""),
                    linha.get("city",""),
                    linha.get("state",""),
                    linha.get("country","Brasil"),
                    "CSV",
                    "ATIVO",
                    str(datetime.now())

                ))

                total += 1

        conn.commit()
        conn.close()

        print()

        print("="*70)
        print("IMPORTAÃƒâ€¡ÃƒÆ'O FINALIZADA")
        print("="*70)

        print()

        print("Arquivo........",arquivo)

        print("Contatos.......",total)

        print()

        print("="*70)

    # =====================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC CONTACT IMPORT ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("IMPORTAÃƒâ€¡ÃƒÆ'O")

        print()

        print("Formato esperado:")

        print()

        print("company")
        print("contact_name")
        print("department")
        print("email")
        print("phone")
        print("whatsapp")
        print("city")
        print("state")
        print("country")

        print()

        arquivo = input("Arquivo CSV: ").strip()

        self.importar_csv(arquivo)

        print("CONTACT IMPORT ONLINE")

        print("="*70)


if __name__ == "__main__":

    ContactImportEngine().executar()



