import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC LEAD ENGINE
FASE 09

VersÃƒÂ£o 10.0

Motor de GeraÃƒÂ§ÃƒÂ£o AutomÃƒÂ¡tica de Leads

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class LeadEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =========================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS leads(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            contact_name TEXT,

            channel TEXT,

            campaign TEXT,

            source_event TEXT,

            status TEXT,

            score INTEGER,

            priority TEXT,

            assigned_to TEXT,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # =========================================================

    def buscar_eventos(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

            id,
            channel,
            campaign,
            event_type,
            status

        FROM channel_events

        WHERE status='SUCESSO'

        ORDER BY id

        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    # =========================================================

    def lead_existe(self, evento_id):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM leads

        WHERE source_event=?

        """,(str(evento_id),))

        total = cursor.fetchone()[0]

        conn.close()

        return total > 0

    # =========================================================

    def calcular_score(self, canal):

        if canal == "WhatsApp":
            return 90

        if canal == "Email":
            return 70

        if canal == "LinkedIn":
            return 80

        return 50

    # =========================================================

    def prioridade(self, score):

        if score >= 90:
            return "CRÃƒÂTICA"

        if score >= 75:
            return "ALTA"

        if score >= 60:
            return "MÃƒâ€°DIA"

        return "BAIXA"

    # =========================================================

    def criar_lead(self, evento):

        score = self.calcular_score(evento[1])

        prioridade = self.prioridade(score)

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO leads(

            company,
            contact_name,
            channel,
            campaign,
            source_event,
            status,
            score,
            priority,
            assigned_to,
            created_at

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """,(

            "Empresa nÃƒÂ£o identificada",
            "",
            evento[1],
            evento[2],
            str(evento[0]),
            "NOVO",
            score,
            prioridade,
            "Comercial",
            str(datetime.now())

        ))

        conn.commit()
        conn.close()

    # =========================================================

    def resumo(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM leads")

        total = cursor.fetchone()[0]

        conn.close()

        return total

    # =========================================================

    def executar(self):

        self.criar_tabela()

        eventos = self.buscar_eventos()

        novos = 0

        for evento in eventos:

            if not self.lead_existe(evento[0]):

                self.criar_lead(evento)

                novos += 1

        print()

        print("="*70)
        print("IOTEC LEAD ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("EVENTOS ANALISADOS.....", len(eventos))
        print("NOVOS LEADS...........", novos)
        print("TOTAL DE LEADS.........", self.resumo())

        print()

        print("="*70)

        print("FLUXO")

        print()

        print("Evento")
        print("Ã¢â€ â€œ")
        print("Lead")
        print("Ã¢â€ â€œ")
        print("Score")
        print("Ã¢â€ â€œ")
        print("Prioridade")
        print("Ã¢â€ â€œ")
        print("CRM")
        print("Ã¢â€ â€œ")
        print("Pipeline")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Transformar")

        print("interaÃƒÂ§ÃƒÂµes")

        print("em oportunidades")

        print("comerciais.")

        print()

        print("="*70)

        print("LEAD ENGINE ONLINE")

        print("="*70)


if __name__ == "__main__":

    LeadEngine().executar()



