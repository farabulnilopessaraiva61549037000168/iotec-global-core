import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC FEEDBACK ENGINE
FASE 09

VersÃƒÂ£o 10.0

Central de Feedback Operacional

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class FeedbackEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabelas(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS channel_events(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            channel TEXT,

            campaign TEXT,

            event_type TEXT,

            status TEXT,

            details TEXT,

            created_at TEXT

        )

        """)

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS kernel_notifications(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            origin TEXT,

            level TEXT,

            message TEXT,

            processed INTEGER,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ======================================================

    def registrar_evento(self,
                         canal,
                         campanha,
                         evento,
                         status,
                         detalhes):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO channel_events(

            channel,
            campaign,
            event_type,
            status,
            details,
            created_at

        )

        VALUES(?,?,?,?,?,?)

        """,(

            canal,
            campanha,
            evento,
            status,
            detalhes,
            str(datetime.now())

        ))

        conn.commit()
        conn.close()

    # ======================================================

    def registrar_notificacao(self, origem, nivel, mensagem):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO kernel_notifications(

            origin,
            level,
            message,
            processed,
            created_at

        )

        VALUES(?,?,?,?,?)

        """,(

            origem,
            nivel,
            mensagem,
            0,
            str(datetime.now())

        ))

        conn.commit()
        conn.close()

    # ======================================================

    def listar_eventos(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        channel,
        campaign,
        event_type,
        status,
        created_at

        FROM channel_events

        ORDER BY id DESC

        LIMIT 20

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # ======================================================

    def executar(self):

        self.criar_tabelas()

        # Exemplo de evento inicial
        self.registrar_evento(

            "WhatsApp",
            "Business Intelligence",
            "EXECUÃƒâ€¡ÃƒÆ'O",
            "SUCESSO",
            "Campanha encaminhada ao Executor"

        )

        self.registrar_notificacao(

            "WhatsApp Executor",
            "INFO",
            "Campanha Business Intelligence executada."

        )

        eventos = self.listar_eventos()

        print()

        print("="*70)
        print("IOTEC FEEDBACK ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("EVENTOS REGISTRADOS")

        print()

        for e in eventos:

            print("Canal.........",e[0])
            print("Campanha......",e[1])
            print("Evento........",e[2])
            print("Status........",e[3])
            print("Data..........",e[4])
            print()

        print("="*70)

        print("REAÃƒâ€¡ÃƒÆ'O DO KERNEL")

        print()

        print("Evento recebido")

        print("Ã¢â€ â€œ")

        print("Registrar histÃƒÂ³rico")

        print("Ã¢â€ â€œ")

        print("Atualizar inteligÃƒÂªncia")

        print("Ã¢â€ â€œ")

        print("Gerar notificaÃƒÂ§ÃƒÂµes")

        print("Ã¢â€ â€œ")

        print("Aguardar prÃƒÂ³ximos eventos")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA EVOLUÃƒâ€¡ÃƒÆ'O")

        print()

        print("Ã¢â‚¬Â¢ Criar Lead automaticamente")

        print("Ã¢â‚¬Â¢ Atualizar CRM")

        print("Ã¢â‚¬Â¢ Calcular Lead Score")

        print("Ã¢â‚¬Â¢ Gerar tarefas comerciais")

        print()

        print("="*70)

        print("FEEDBACK ENGINE ONLINE")

        print("="*70)


if __name__ == "__main__":

    FeedbackEngine().executar()



