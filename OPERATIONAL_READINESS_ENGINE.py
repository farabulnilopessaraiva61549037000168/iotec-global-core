import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC OPERATIONAL READINESS ENGINE
VersÃƒÂ£o Enterprise 10.0

O Kernel somente entra em operaÃƒÂ§ÃƒÂ£o
quando existirem canais realmente disponÃƒÂ­veis.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class OperationalReadiness:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ============================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS integration_status(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            integration TEXT UNIQUE,

            configured INTEGER,

            authenticated INTEGER,

            validated INTEGER,

            operational INTEGER,

            kernel_enabled INTEGER,

            last_check TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ============================================================

    def registrar_padrao(self):

        itens = [

            ("WhatsApp Business",1,0,0,0,0),
            ("Email Corporativo",1,0,0,0,0),
            ("LinkedIn",1,0,0,0,0),
            ("Portal Institucional",0,0,0,0,0),
            ("Google Business",0,0,0,0,0),
            ("CRM",1,1,1,1,1),
            ("Banco Corporativo",1,1,1,1,1)

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for item in itens:

            cursor.execute("""

            INSERT OR IGNORE INTO integration_status(

                integration,
                configured,
                authenticated,
                validated,
                operational,
                kernel_enabled,
                last_check

            )

            VALUES(?,?,?,?,?,?,?)

            """,(

                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    # ============================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            integration,
            configured,
            authenticated,
            validated,
            operational,
            kernel_enabled

        FROM integration_status

        ORDER BY integration

        """)

        dados = cursor.fetchall()

        conn.close()

        total = len(dados)
        operacionais = 0

        print()
        print("="*70)
        print("IOTEC OPERATIONAL READINESS ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)
        print()

        for item in dados:

            print(item[0])

            print("Configurado.....", "SIM" if item[1] else "NÃƒÆ'O")
            print("Autenticado.....", "SIM" if item[2] else "NÃƒÆ'O")
            print("Validado........", "SIM" if item[3] else "NÃƒÆ'O")
            print("Operacional.....", "SIM" if item[4] else "NÃƒÆ'O")
            print("Kernel..........", "ATIVO" if item[5] else "INATIVO")

            print()

            if item[4]:
                operacionais += 1

        percentual = round((operacionais / total) * 100, 1) if total else 0

        print("="*70)

        print("RESUMO")
        print()

        print("IntegraÃƒÂ§ÃƒÂµes........", total)
        print("Operacionais.......", operacionais)
        print("ProntidÃƒÂ£o..........", f"{percentual}%")

        print()

        print("="*70)

        if percentual >= 80:

            print("MODO DO KERNEL")
            print()
            print(">>> OPERAÃƒâ€¡ÃƒÆ'O COMERCIAL LIBERADA <<<")

        else:

            print("MODO DO KERNEL")
            print()
            print(">>> IMPLANTAÃƒâ€¡ÃƒÆ'O <<<")

        print()

        print("="*70)

        print("FILOSOFIA")
        print()

        print("Cada integraÃƒÂ§ÃƒÂ£o")
        print("abre uma porta")
        print("para um novo")
        print("canal comercial.")
        print()
        print("Quando uma integraÃƒÂ§ÃƒÂ£o")
        print("torna-se operacional,")
        print("o Kernel pode")
        print("utilizÃƒÂ¡-la com seguranÃƒÂ§a.")

        print()

        print("="*70)
        print("OPERATIONAL READINESS ONLINE")
        print("="*70)

    # ============================================================

    def executar(self):

        self.criar_tabela()

        self.registrar_padrao()

        self.mostrar()


if __name__ == "__main__":

    OperationalReadiness().executar()



