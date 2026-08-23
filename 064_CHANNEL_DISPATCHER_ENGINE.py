import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CHANNEL DISPATCHER ENGINE
FASE 08

VersÃƒÂ£o 9.0

Despachante Central de Campanhas

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class ChannelDispatcher:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS dispatch_queue(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            campaign TEXT,

            channel TEXT,

            priority TEXT,

            status TEXT,

            created_at TEXT,

            dispatched_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ======================================================

    def sincronizar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            id,
            titulo,
            canal,
            prioridade

        FROM approval_queue

        WHERE status='APROVADA'

        """)

        campanhas = cursor.fetchall()

        inseridas = 0

        for campanha in campanhas:

            cursor.execute("""

            SELECT COUNT(*)

            FROM dispatch_queue

            WHERE campaign=?

            """,(campanha[1],))

            if cursor.fetchone()[0] == 0:

                cursor.execute("""

                INSERT INTO dispatch_queue(

                    campaign,

                    channel,

                    priority,

                    status,

                    created_at,

                    dispatched_at

                )

                VALUES(?,?,?,?,?,?)

                """,(

                    campanha[1],

                    campanha[2],

                    campanha[3],

                    "PRONTA",

                    str(datetime.now()),

                    ""

                ))

                inseridas += 1

        conn.commit()
        conn.close()

        return inseridas

    # ======================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            campaign,

            channel,

            priority,

            status

        FROM dispatch_queue

        ORDER BY id

        """)

        filas = cursor.fetchall()

        conn.close()

        print()

        print("="*70)
        print("IOTEC CHANNEL DISPATCHER ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("FILA DE DISPARO")

        print()

        if not filas:

            print("Nenhuma campanha pronta para execuÃƒÂ§ÃƒÂ£o.")

        else:

            for campanha in filas:

                print("Campanha.....", campanha[0])
                print("Canal........", campanha[1])
                print("Prioridade...", campanha[2])
                print("Status.......", campanha[3])
                print()

        print("="*70)

        print("FLUXO")

        print()

        print("Campanha")
        print("Ã¢â€ â€œ")
        print("Fila de AprovaÃƒÂ§ÃƒÂ£o")
        print("Ã¢â€ â€œ")
        print("Dispatcher")
        print("Ã¢â€ â€œ")
        print("Canal")
        print("Ã¢â€ â€œ")
        print("Leads")
        print("Ã¢â€ â€œ")
        print("CRM")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Organizar todas as campanhas")
        print("aprovadas para execuÃƒÂ§ÃƒÂ£o")
        print("nos canais disponÃƒÂ­veis.")

        print()

        print("="*70)

        print("CHANNEL DISPATCHER ONLINE")
        print("="*70)


# ==========================================================

if __name__ == "__main__":

    dispatcher = ChannelDispatcher()

    dispatcher.criar_tabela()

    novas = dispatcher.sincronizar()

    if novas:
        print(f"\n{novas} campanha(s) adicionada(s) ÃƒÂ  fila de disparo.\n")

    dispatcher.mostrar()



