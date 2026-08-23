import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

import sqlite3

DB = r"C:\IOTEC\IOTEC_OPPORTUNITY.db"

conn = sqlite3.connect(DB, timeout=30)

conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

# ============================================================
# COMMERCIAL INTELLIGENCE
# ============================================================

class CommercialIntelligence:

    def __init__(self):

        self.meta_mensal = 5000000

        self.pipeline = 0

        self.receita = 0

        self.propostas = 0

        self.contratos = 0

        self.campanhas = 0


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

        return total


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

        return valor


    def atualizar_propostas(self):

        cur.execute("""

        SELECT COUNT(*)

        FROM opportunities

        WHERE status='PROPOSTA'

        """)

        self.propostas = cur.fetchone()[0]


    def atualizar_contratos(self):

        cur.execute("""

        SELECT COUNT(*)

        FROM opportunities

        WHERE status='CONTRATO'

        """)

        self.contratos = cur.fetchone()[0]


    def atualizar_campanhas(self):

        cur.execute("""

        SELECT COUNT(DISTINCT campaign)

        FROM opportunities

        """)

        valor = cur.fetchone()[0]

        if valor is None:

            valor = 0

        self.campanhas = valor


    def chance_meta(self):

        if self.meta_mensal == 0:

            return 0

        return round((self.pipeline/self.meta_mensal)*100,2)


    def resumo(self):

        self.atualizar_pipeline()

        self.atualizar_receita()

        self.atualizar_propostas()

        self.atualizar_contratos()

        self.atualizar_campanhas()

        print()

        print("="*70)

        print("CENTRO COMERCIAL IOTEC")

        print("="*70)

        print(f"Meta Mensal............. R$ {self.meta_mensal:,.2f}")

        print(f"Pipeline................. R$ {self.pipeline:,.2f}")

        print(f"Receita................. R$ {self.receita:,.2f}")

        print(f"Propostas............... {self.propostas}")

        print(f"Contratos............... {self.contratos}")

        print(f"Campanhas............... {self.campanhas}")

        print(f"Chance Meta............. {self.chance_meta()} %")

        print("="*70)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print()

    print("=" * 70)
    print("IOTEC COMMERCIAL INTELLIGENCE")
    print("=" * 70)

    ci = CommercialIntelligence()

    ci.resumo()

    conn.close()





