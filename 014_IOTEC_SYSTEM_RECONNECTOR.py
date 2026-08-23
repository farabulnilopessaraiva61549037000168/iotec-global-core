import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================================
IOTEC OPERATING SYSTEM
===============================================================================

MÃƒâ€œDULO:
014_IOTEC_SYSTEM_RECONNECTOR.py

MISSÃƒÆ'O

Antes de criar qualquer mÃƒÂ³dulo novo, localizar capacidades jÃƒÂ¡ existentes,
identificar duplicatas, sugerir reconexÃƒÂµes e reduzir fragmentaÃƒÂ§ÃƒÂ£o.

POLÃƒÂTICA

REUTILIZAR > RECONECTAR > TESTAR > CRIAR

===============================================================================
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path(r"C:\IOTEC")
DATABASE = ROOT / "kernel.db"


class SystemReconnector:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

        self.capacidades = defaultdict(list)

        self.palavras = {

            "PAGAMENTO":[
                "payment",
                "paypal",
                "checkout",
                "pix",
                "mercadopago"
            ],

            "FORMULARIO":[
                "form",
                "lead",
                "register",
                "cadastro"
            ],

            "EMAIL":[
                "email",
                "mail"
            ],

            "WHATSAPP":[
                "whatsapp"
            ],

            "API":[
                "api",
                "gateway"
            ],

            "BANCO":[
                "database",
                ".db",
                "sqlite"
            ],

            "RENDER":[
                "render"
            ],

            "NETLIFY":[
                "netlify"
            ],

            "PRODUTO":[
                "product",
                "catalog",
                "service"
            ]

        }

    # ============================================================

    def now(self):

        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # ============================================================

    def registrar_evento(self, texto):

        self.cursor.execute("""

        INSERT INTO events(

            agent,

            type,

            description,

            timestamp

        )

        VALUES(?,?,?,?)

        """,

        (

            "SYSTEM_RECONNECTOR",

            "AUDITORIA",

            texto,

            self.now()

        )

        )

        self.conn.commit()

    # ============================================================

    def mapear_capacidades(self):

        print()

        print("="*70)
        print("MAPEANDO CAPACIDADES")
        print("="*70)

        for arquivo in ROOT.rglob("*"):

            if not arquivo.is_file():
                continue

            nome = arquivo.name.lower()

            for capacidade, palavras in self.palavras.items():

                for palavra in palavras:

                    if palavra in nome:

                        self.capacidades[capacidade].append(str(arquivo))
                        break

        print()

    # ============================================================

    def relatorio(self):

        print("="*70)
        print("RELATÃƒâ€œRIO DE RECONEXÃƒÆ'O")
        print("="*70)

        for capacidade in sorted(self.capacidades):

            quantidade = len(self.capacidades[capacidade])

            print()
            print(capacidade)
            print("-"*50)
            print("Componentes encontrados :", quantidade)

            principais = self.capacidades[capacidade][:5]

            for arq in principais:
                print(arq)

            if quantidade > 1:

                print()

                print("AÃƒâ€¡ÃƒÆ'O SUGERIDA")

                print("Localizar mÃƒÂ³dulo principal.")

                print("Eliminar duplicaÃƒÂ§ÃƒÂµes desnecessÃƒÂ¡rias.")

                print("Reconectar funcionalidades.")

                print("Evitar criaÃƒÂ§ÃƒÂ£o de novos mÃƒÂ³dulos.")

            self.registrar_evento(

                f"{capacidade}: {quantidade} componentes encontrados."

            )

    # ============================================================

    def resumo_executivo(self):

        print()

        print("="*70)
        print("PARECER EXECUTIVO")
        print("="*70)

        print()

        print("FILOSOFIA")

        print()

        print("Antes de criar qualquer cÃƒÂ³digo novo,")

        print("o nÃƒÂºcleo deverÃƒÂ¡ procurar capacidades")

        print("jÃƒÂ¡ existentes e tentar reutilizÃƒÂ¡-las.")

        print()

        print("ORDEM OBRIGATÃƒâ€œRIA")

        print()

        print("1 - Procurar")

        print("2 - Reutilizar")

        print("3 - Reconectar")

        print("4 - Testar")

        print("5 - Somente entÃƒÂ£o criar cÃƒÂ³digo novo")

        print()

        print("="*70)

    # ============================================================

    def iniciar(self):

        self.mapear_capacidades()

        self.relatorio()

        self.resumo_executivo()


# =====================================================================

if __name__ == "__main__":

    engine = SystemReconnector()

    engine.iniciar()



