import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC TECHNOLOGY PORTFOLIO ENGINE
VersÃƒÂ£o Enterprise 10.0

Gerenciador do PatrimÃƒÂ´nio TecnolÃƒÂ³gico da IOTEC

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class TechnologyPortfolioEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ================================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS technology_portfolio(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            technology TEXT UNIQUE,

            category TEXT,

            maturity INTEGER,

            internal_use INTEGER,

            commercial_release INTEGER,

            licensable INTEGER,

            strategic_value INTEGER,

            commercial_value INTEGER,

            estimated_price REAL,

            clients INTEGER,

            observations TEXT,

            created_at TEXT,

            updated_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # ================================================================

    def registrar(self):

        tecnologias = [

            ("Kernel IOTEC","Kernel",10,1,1,1,100,100,500000.00,0),
            ("Executive Reasoning","IA",10,1,1,1,95,90,180000.00,0),
            ("Corporate Dossier","InteligÃƒÂªncia",10,1,1,1,90,88,150000.00,0),
            ("Campaign Engine","Comercial",10,1,1,1,92,91,120000.00,0),
            ("Lead Engine","CRM",10,1,1,1,90,90,100000.00,0),
            ("CRM Pipeline","CRM",10,1,1,1,92,89,130000.00,0),
            ("Knowledge Core","Conhecimento",10,1,1,1,98,94,250000.00,0),
            ("Adaptive Motors","Motores",1,1,0,0,100,100,0.00,0),
            ("Learning Engine","IA",1,1,0,0,100,95,0.00,0),
            ("Technology Licensing","Licenciamento",1,0,0,0,95,100,0.00,0)

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for t in tecnologias:

            cursor.execute("""

            INSERT OR IGNORE INTO technology_portfolio(

                technology,
                category,
                maturity,
                internal_use,
                commercial_release,
                licensable,
                strategic_value,
                commercial_value,
                estimated_price,
                clients,
                observations,
                created_at,
                updated_at

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)

            """,(

                t[0],
                t[1],
                t[2],
                t[3],
                t[4],
                t[5],
                t[6],
                t[7],
                t[8],
                t[9],
                "Ativo tecnolÃƒÂ³gico da IOTEC.",
                str(datetime.now()),
                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    # ================================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        technology,
        category,
        maturity,
        internal_use,
        commercial_release,
        licensable,
        estimated_price

        FROM technology_portfolio

        ORDER BY strategic_value DESC

        """)

        dados = cursor.fetchall()

        conn.close()

        print("="*70)
        print("IOTEC TECHNOLOGY PORTFOLIO ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)
        print()

        patrimonio = 0

        for d in dados:

            patrimonio += d[6]

            print(d[0])
            print("Categoria........", d[1])
            print("Maturidade.......", f"{d[2]}/10")
            print("Uso Interno......", "SIM" if d[3] else "NÃƒÆ'O")
            print("Comercial........", "SIM" if d[4] else "NÃƒÆ'O")
            print("LicenciÃƒÂ¡vel......", "SIM" if d[5] else "NÃƒÆ'O")
            print("Valor Estimado...", f"R$ {d[6]:,.2f}")
            print()

        print("="*70)

        print("PATRIMÃƒâ€NIO TECNOLÃƒâ€œGICO")

        print()

        print("Tecnologias........", len(dados))
        print("Valor Estimado.....", f"R$ {patrimonio:,.2f}")

        print()

        print("="*70)

        print("FILOSOFIA")
        print()

        print("Tecnologia ÃƒÂ© patrimÃƒÂ´nio.")
        print("Conhecimento gera ativos.")
        print("Ativos geram licenciamento.")
        print("Licenciamento gera receita.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Transformar")
        print("conhecimento")
        print("em ativos")
        print("tecnolÃƒÂ³gicos")
        print("reutilizÃƒÂ¡veis")
        print("e licenciÃƒÂ¡veis.")

        print()

        print("="*70)

        print("PORTFOLIO ONLINE")
        print("="*70)

    # ================================================================

    def executar(self):

        self.criar_tabela()
        self.registrar()
        self.mostrar()


if __name__ == "__main__":
    TechnologyPortfolioEngine().executar()



