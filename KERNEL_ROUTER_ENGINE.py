import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KERNEL ROUTER ENGINE
FASE 09

VersÃƒÂ£o 10.0

Kernel Central de Roteamento

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class KernelRouter:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS channel_executors(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            channel TEXT UNIQUE,

            executor TEXT,

            priority INTEGER,

            active INTEGER,

            description TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ======================================================

    def registrar_executores(self):

        executores = [

            ("WhatsApp",
             "WHATSAPP_EXECUTOR_ENGINE",
             1,
             1,
             "Executor Oficial WhatsApp"),

            ("Email",
             "EMAIL_EXECUTOR_ENGINE",
             2,
             1,
             "Executor SMTP"),

            ("LinkedIn",
             "LINKEDIN_EXECUTOR_ENGINE",
             3,
             0,
             "Executor LinkedIn"),

            ("Portal",
             "PORTAL_EXECUTOR_ENGINE",
             4,
             0,
             "Executor Portal"),

            ("Google Business",
             "GOOGLE_BUSINESS_EXECUTOR_ENGINE",
             5,
             0,
             "Executor Google Business")

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for item in executores:

            cursor.execute("""

            INSERT OR IGNORE INTO channel_executors(

                channel,
                executor,
                priority,
                active,
                description

            )

            VALUES(?,?,?,?,?)

            """, item)

        conn.commit()
        conn.close()

    # ======================================================

    def campanhas_prontas(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            campaign,
            channel,
            priority,
            status

        FROM dispatch_queue

        WHERE status='PRONTA'

        ORDER BY id

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # ======================================================

    def localizar_executor(self, canal):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            executor,
            priority,
            active

        FROM channel_executors

        WHERE channel=?

        """, (canal,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    # ======================================================

    def executar(self):

        self.criar_tabela()

        self.registrar_executores()

        print()

        print("=" * 70)
        print("IOTEC KERNEL ROUTER ENGINE")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        campanhas = self.campanhas_prontas()

        if not campanhas:

            print()
            print("Nenhuma campanha aguardando roteamento.")
            print()

        else:

            print()
            print("CAMPANHAS")
            print()

            for campanha in campanhas:

                executor = self.localizar_executor(campanha[1])

                print("Campanha.........", campanha[0])
                print("Canal............", campanha[1])

                if executor:

                    print("Executor.........", executor[0])
                    print("Prioridade.......", executor[1])

                    if executor[2]:

                        print("Status........... PRONTO")

                    else:

                        print("Status........... EXECUTOR INATIVO")

                else:

                    print("Executor......... NÃƒÆ'O CADASTRADO")

                print()

        print("=" * 70)

        print("EXECUTORES REGISTRADOS")
        print()

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            channel,
            executor,
            active

        FROM channel_executors

        ORDER BY priority

        """)

        for canal, executor, ativo in cursor.fetchall():

            print(canal)

            print("Executor.........", executor)

            print("Ativo............", "SIM" if ativo else "NÃƒÆ'O")

            print()

        conn.close()

        print("=" * 70)

        print("FLUXO")

        print()

        print("Dispatcher")
        print("Ã¢â€ â€œ")
        print("Kernel Router")
        print("Ã¢â€ â€œ")
        print("Executor")
        print("Ã¢â€ â€œ")
        print("Canal")
        print("Ã¢â€ â€œ")
        print("Lead")
        print("Ã¢â€ â€œ")
        print("CRM")
        print("Ã¢â€ â€œ")
        print("Receita")

        print()

        print("=" * 70)

        print("FILOSOFIA")

        print()

        print("O Kernel nÃƒÂ£o executa.")
        print("O Kernel decide")
        print("qual Executor")
        print("deverÃƒÂ¡ assumir")
        print("cada missÃƒÂ£o.")

        print()

        print("=" * 70)

        print("KERNEL ROUTER ONLINE")

        print("=" * 70)


if __name__ == "__main__":

    KernelRouter().executar()



