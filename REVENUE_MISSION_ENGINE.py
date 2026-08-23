import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC REVENUE MISSION ENGINE
FASE 001

Centro de MissÃƒÂ£o Comercial

==============================================================
"""

import sqlite3
from datetime import datetime

DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn = sqlite3.connect(DB, timeout=30)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")


class RevenueMission:

    def __init__(self):

        self.meta = 5000000

        self.pipeline = 0
        self.receita = 0

        self.leads = 0
        self.propostas = 0
        self.contratos = 0

    # -----------------------------------------------------

    def atualizar_pipeline(self):

        cur.execute("""

            SELECT
                estimated_value,
                probability
            FROM opportunities

        """)

        total = 0

        for row in cur.fetchall():

            total += row["estimated_value"] * (row["probability"]/100)

        self.pipeline = total

    # -----------------------------------------------------

    def atualizar_receita(self):

        cur.execute("""

            SELECT
                SUM(estimated_value)

            FROM opportunities

            WHERE status='CONTRATO'

        """)

        valor = cur.fetchone()[0]

        if valor is None:
            valor = 0

        self.receita = valor

    # -----------------------------------------------------

    def contar_leads(self):

        cur.execute("""

            SELECT COUNT(*)

            FROM opportunities

        """)

        self.leads = cur.fetchone()[0]

    # -----------------------------------------------------

    def contar_propostas(self):

        cur.execute("""

            SELECT COUNT(*)

            FROM opportunities

            WHERE status='PROPOSTA'

        """)

        self.propostas = cur.fetchone()[0]

    # -----------------------------------------------------

    def contar_contratos(self):

        cur.execute("""

            SELECT COUNT(*)

            FROM opportunities

            WHERE status='CONTRATO'

        """)

        self.contratos = cur.fetchone()[0]

    # -----------------------------------------------------

    def chance_meta(self):

        if self.meta == 0:
            return 0

        return round((self.pipeline/self.meta)*100,2)

    # -----------------------------------------------------

    def proxima_missao(self):

        if self.propostas > 0:
            return "Realizar Follow-up das propostas."

        if self.leads > 0:
            return "Converter Leads em reuniÃƒÂµes."

        return "Prospectar novas empresas."

    # -----------------------------------------------------

    def executar(self):

        self.atualizar_pipeline()
        self.atualizar_receita()

        self.contar_leads()
        self.contar_propostas()
        self.contar_contratos()

        print()

        print("="*70)
        print("IOTEC REVENUE MISSION CENTER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("INDICADORES")

        print()

        print(f"Leads................... {self.leads}")

        print(f"Propostas............... {self.propostas}")

        print(f"Contratos............... {self.contratos}")

        print()

        print(f"Pipeline................ R$ {self.pipeline:,.2f}")

        print(f"Receita................. R$ {self.receita:,.2f}")

        print(f"Meta.................... R$ {self.meta:,.2f}")

        print(f"Meta Atingida........... {self.chance_meta()} %")

        print()

        print("MISSÃƒÆ'O PRIORITÃƒÂRIA")

        print()

        print(self.proxima_missao())

        print()

        print("="*70)

        print("Objetivo Principal")

        print("Transformar oportunidades em contratos.")

        print("="*70)


if __name__ == "__main__":

    RevenueMission().executar()

    conn.close()



