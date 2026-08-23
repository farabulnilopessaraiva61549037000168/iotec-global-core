import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC BUSINESS MODEL ENGINE
VersÃƒÂ£o Enterprise 10.0

O Kernel aprende a transformar
tecnologias em modelos de negÃƒÂ³cio.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class BusinessModelEngine:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # =============================================================

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS business_models(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            technology TEXT,

            recommended_model TEXT,

            target_market TEXT,

            recurring INTEGER,

            implementation INTEGER,

            licensing INTEGER,

            white_label INTEGER,

            oem INTEGER,

            consulting INTEGER,

            training INTEGER,

            api_service INTEGER,

            maturity INTEGER,

            observations TEXT,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    # =============================================================

    def registrar(self):

        modelos = [

            ("Kernel IOTEC",
             "Licenciamento Corporativo",
             "Grandes Empresas",
             1,1,1,1,1,1,1,1,10),

            ("Campaign Engine",
             "SaaS + ImplantaÃƒÂ§ÃƒÂ£o",
             "Empresas",
             1,1,0,0,0,1,1,0,10),

            ("Lead Engine",
             "SaaS",
             "Empresas",
             1,0,0,0,0,0,0,1,10),

            ("CRM Pipeline",
             "SaaS",
             "Empresas",
             1,0,0,0,0,0,0,1,10),

            ("Corporate Dossier",
             "Consultoria + ImplantaÃƒÂ§ÃƒÂ£o",
             "Grandes Empresas",
             0,1,0,0,0,1,1,0,10),

            ("Executive Reasoning",
             "Consultoria Executiva",
             "Diretores e CEOs",
             1,1,0,0,0,1,1,0,10),

            ("Adaptive Motors",
             "Pesquisa",
             "Todos",
             0,0,0,0,0,0,0,0,1),

            ("Learning Engine",
             "Pesquisa",
             "Todos",
             0,0,0,0,0,0,0,0,1)

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for m in modelos:

            cursor.execute("""

            INSERT OR IGNORE INTO business_models(

                technology,
                recommended_model,
                target_market,
                recurring,
                implementation,
                licensing,
                white_label,
                oem,
                consulting,
                training,
                api_service,
                maturity,
                observations,
                created_at

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)

            """,(

                m[0],
                m[1],
                m[2],
                m[3],
                m[4],
                m[5],
                m[6],
                m[7],
                m[8],
                m[9],
                m[10],
                m[11],
                "Modelo recomendado pelo Kernel.",
                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    # =============================================================

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        technology,

        recommended_model,

        target_market,

        maturity

        FROM business_models

        ORDER BY maturity DESC, technology

        """)

        dados = cursor.fetchall()

        conn.close()

        print("="*70)
        print("IOTEC BUSINESS MODEL ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)
        print()

        for d in dados:

            print("TECNOLOGIA")
            print(d[0])

            print("Modelo.............", d[1])
            print("Mercado............", d[2])
            print("Maturidade.........", f"{d[3]}/10")

            print()

        print("="*70)

        print("MODELOS DE NEGÃƒâ€œCIO SUPORTADOS")

        print()

        print("Ã¢Å"â€œ SaaS")
        print("Ã¢Å"â€œ ImplantaÃƒÂ§ÃƒÂ£o")
        print("Ã¢Å"â€œ Licenciamento")
        print("Ã¢Å"â€œ White Label")
        print("Ã¢Å"â€œ OEM")
        print("Ã¢Å"â€œ Consultoria")
        print("Ã¢Å"â€œ API")
        print("Ã¢Å"â€œ Treinamento")
        print("Ã¢Å"â€œ Assinatura")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Cada tecnologia")
        print("pode possuir")
        print("mais de um")
        print("modelo de negÃƒÂ³cio.")
        print()

        print("O Kernel deverÃƒÂ¡")
        print("escolher aquele")
        print("mais adequado")
        print("ao perfil")
        print("do cliente.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Transformar")
        print("tecnologia")
        print("em receita")
        print("recorrente")
        print("e sustentÃƒÂ¡vel.")

        print()

        print("="*70)
        print("BUSINESS MODEL ENGINE ONLINE")
        print("="*70)

    # =============================================================

    def executar(self):

        self.criar_tabela()

        self.registrar()

        self.mostrar()


if __name__ == "__main__":

    BusinessModelEngine().executar()



