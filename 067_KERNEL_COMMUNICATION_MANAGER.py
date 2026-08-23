import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KERNEL COMMUNICATION MANAGER
FASE 09

VersÃƒÂ£o 10.0

Registro Oficial dos Canais de ComunicaÃƒÂ§ÃƒÂ£o

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class KernelCommunicationManager:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =====================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS communication_channels(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            channel TEXT UNIQUE,

            company_name TEXT,

            identifier TEXT,

            description TEXT,

            status TEXT,

            integration_level TEXT,

            api_ready INTEGER,

            kernel_enabled INTEGER,

            created_at TEXT,

            updated_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # =====================================================

    def registrar_padrao(self):

        canais = [

            (
                "WhatsApp",
                "IOTEC",
                "+55 88 99306-4168",
                "Canal oficial de atendimento",
                "ONLINE",
                "MANUAL",
                0,
                1
            ),

            (
                "Email",
                "IOTEC",
                "iotec.bl@proton.me",
                "E-mail corporativo",
                "ONLINE",
                "SMTP",
                0,
                1
            ),

            (
                "LinkedIn",
                "IOTEC",
                "",
                "PÃƒÂ¡gina Corporativa",
                "OFFLINE",
                "NENHUMA",
                0,
                0
            ),

            (
                "Portal",
                "IOTEC",
                "",
                "Portal Institucional",
                "OFFLINE",
                "NENHUMA",
                0,
                0
            ),

            (
                "Google Business",
                "IOTEC",
                "",
                "Perfil Empresarial",
                "OFFLINE",
                "NENHUMA",
                0,
                0
            )

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for canal in canais:

            cursor.execute("""

            INSERT OR IGNORE INTO communication_channels(

                channel,
                company_name,
                identifier,
                description,
                status,
                integration_level,
                api_ready,
                kernel_enabled,
                created_at,
                updated_at

            )

            VALUES(?,?,?,?,?,?,?,?,?,?)

            """,(

                canal[0],
                canal[1],
                canal[2],
                canal[3],
                canal[4],
                canal[5],
                canal[6],
                canal[7],
                str(datetime.now()),
                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    # =====================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        channel,
        identifier,
        status,
        integration_level,
        api_ready,
        kernel_enabled

        FROM communication_channels

        ORDER BY channel

        """)

        canais = cursor.fetchall()

        conn.close()

        print()
        print("=" * 70)
        print("IOTEC KERNEL COMMUNICATION MANAGER")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()
        print("REGISTRO OFICIAL DOS CANAIS")
        print()

        online = 0

        for canal in canais:

            print(canal[0])

            print("Identificador....", canal[1] if canal[1] else "-")
            print("Status...........", canal[2])
            print("IntegraÃƒÂ§ÃƒÂ£o.......", canal[3])
            print("API..............", "SIM" if canal[4] else "NÃƒÆ'O")
            print("Kernel...........", "ATIVO" if canal[5] else "INATIVO")
            print()

            if canal[2] == "ONLINE":
                online += 1

        print("=" * 70)

        print("RESUMO")
        print()

        print("Canais...........", len(canais))
        print("Online...........", online)
        print("Offline..........", len(canais) - online)

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O DO KERNEL")
        print()

        print("Toda comunicaÃƒÂ§ÃƒÂ£o")
        print("deverÃƒÂ¡ utilizar")
        print("apenas canais")
        print("registrados")
        print("nesta central.")

        print()

        print("=" * 70)

        print("PRÃƒâ€œXIMA EVOLUÃƒâ€¡ÃƒÆ'O")
        print()

        print("Ã¢â‚¬Â¢ API WhatsApp Business")
        print("Ã¢â‚¬Â¢ SMTP Corporativo")
        print("Ã¢â‚¬Â¢ LinkedIn API")
        print("Ã¢â‚¬Â¢ Google Business API")
        print("Ã¢â‚¬Â¢ Portal API")

        print()

        print("=" * 70)

        print("KERNEL COMMUNICATION MANAGER ONLINE")
        print("=" * 70)

    # =====================================================

    def executar(self):

        self.criar_tabela()
        self.registrar_padrao()
        self.mostrar()


if __name__ == "__main__":

    KernelCommunicationManager().executar()



