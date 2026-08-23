import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC WHATSAPP EXECUTOR ENGINE
FASE 09

VersÃƒÂ£o 10.0

Executor Oficial do WhatsApp Business

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class WhatsAppExecutor:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =============================================================

    def criar_tabela_execucoes(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS whatsapp_execution_log(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            campaign TEXT,

            phone TEXT,

            status TEXT,

            executed_at TEXT,

            observation TEXT

        )

        """)

        conn.commit()
        conn.close()

    # =============================================================

    def buscar_campanhas(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            id,
            campaign,
            channel,
            priority,
            status

        FROM dispatch_queue

        WHERE channel='WhatsApp'
        AND status='PRONTA'

        ORDER BY id

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # =============================================================

    def registrar_execucao(self, campanha):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO whatsapp_execution_log(

            campaign,
            phone,
            status,
            executed_at,
            observation

        )

        VALUES(?,?,?,?,?)

        """,(

            campanha[1],

            "+55 88 99306-4168",

            "EXECUTADA",

            str(datetime.now()),

            "Aguardando integraÃƒÂ§ÃƒÂ£o oficial com WhatsApp Business API"

        ))

        cursor.execute("""

        UPDATE dispatch_queue

        SET status='EXECUTADA',
            dispatched_at=?

        WHERE id=?

        """,(

            str(datetime.now()),

            campanha[0]

        ))

        conn.commit()
        conn.close()

    # =============================================================

    def executar(self):

        self.criar_tabela_execucoes()

        campanhas = self.buscar_campanhas()

        print()
        print("="*70)
        print("IOTEC WHATSAPP EXECUTOR ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        if not campanhas:

            print("Nenhuma campanha pronta para execuÃƒÂ§ÃƒÂ£o.")
            print()
            print("="*70)
            print("WHATSAPP EXECUTOR ONLINE")
            print("="*70)
            return

        print("CAMPANHAS RECEBIDAS")
        print()

        total = 0

        for campanha in campanhas:

            print("Campanha.....",campanha[1])
            print("Canal........",campanha[2])
            print("Prioridade...",campanha[3])

            self.registrar_execucao(campanha)

            print("Status....... EXECUTADA")
            print()

            total += 1

        print("="*70)

        print("RESUMO")

        print()

        print("Campanhas executadas....",total)

        print()

        print("="*70)

        print("FLUXO")

        print()

        print("Dispatcher")

        print("Ã¢â€ â€œ")

        print("WhatsApp Executor")

        print("Ã¢â€ â€œ")

        print("Registro de ExecuÃƒÂ§ÃƒÂ£o")

        print("Ã¢â€ â€œ")

        print("HistÃƒÂ³rico")

        print("Ã¢â€ â€œ")

        print("Aguardando API Oficial")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Toda campanha")

        print("executada")

        print("deve possuir")

        print("rastreabilidade")

        print("completa.")

        print()

        print("="*70)

        print("WHATSAPP EXECUTOR ONLINE")

        print("="*70)


# ============================================================

if __name__ == "__main__":

    executor = WhatsAppExecutor()

    executor.executar()



