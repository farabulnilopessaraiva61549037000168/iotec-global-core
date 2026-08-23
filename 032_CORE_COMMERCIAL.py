import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORE COMMERCIAL
FASE 05
ETAPA 002

VersÃƒÂ£o 6.0

======================================================================
"""

import sqlite3


class CoreCommercial:

    def __init__(self, banco="iotec.db"):

        self.conn = sqlite3.connect(banco)

        self.conn.row_factory = sqlite3.Row

        self.cur = self.conn.cursor()

    # ------------------------------------------------------------

    def total_empresas(self):

        self.cur.execute("SELECT COUNT(*) TOTAL FROM companies")

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def total_leads(self):

        self.cur.execute("SELECT COUNT(*) TOTAL FROM leads")

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def total_propostas(self):

        self.cur.execute("SELECT COUNT(*) TOTAL FROM proposals")

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def total_contratos(self):

        self.cur.execute("SELECT COUNT(*) TOTAL FROM contracts")

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def pipeline_total(self):

        self.cur.execute("""

            SELECT

                COALESCE(SUM(value),0) TOTAL

            FROM proposals

            WHERE status<>'CANCELADA'

        """)

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def receita_total(self):

        self.cur.execute("""

            SELECT

                COALESCE(SUM(amount),0) TOTAL

            FROM payments

            WHERE status='PAGO'

        """)

        return self.cur.fetchone()["TOTAL"]

    # ------------------------------------------------------------

    def resumo(self):

        print()

        print("="*70)

        print("IOTEC CORE COMMERCIAL")

        print("="*70)

        print()

        print(f"Empresas.......... {self.total_empresas()}")

        print(f"Leads............. {self.total_leads()}")

        print(f"Propostas......... {self.total_propostas()}")

        print(f"Contratos......... {self.total_contratos()}")

        print(f"Pipeline.......... R$ {self.pipeline_total():,.2f}")

        print(f"Receita........... R$ {self.receita_total():,.2f}")

        print()

        print("="*70)

        print("CORE COMMERCIAL ONLINE")

        print("="*70)

    # ------------------------------------------------------------

    def fechar(self):

        self.conn.close()


# =====================================================================

if __name__ == "__main__":

    core = CoreCommercial()

    core.resumo()

    core.fechar()



