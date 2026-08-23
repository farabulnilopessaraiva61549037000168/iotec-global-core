import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC INTELLIGENCE COMMAND CENTER
FASE 02
ETAPA 004

VersÃƒÂ£o 4.0

======================================================================
"""

from datetime import datetime


class IntelligenceCommandCenter:

    VERSION = "4.0"

    def __init__(self):

        # ---------------------------------------------------------
        # MONITORAMENTO
        # ---------------------------------------------------------

        self.empresas_monitoradas = 483
        self.oportunidades = 84
        self.corredores = 12
        self.cidades = 8
        self.paises = 5

        # ---------------------------------------------------------
        # INTELIGÃƒÅ NCIA
        # ---------------------------------------------------------

        self.company_discovery = True
        self.opportunity_engine = True
        self.market_intelligence = True
        self.executive_reports = True
        self.newsroom = True
        self.kernel = True

        # ---------------------------------------------------------
        # PRODUÃƒâ€¡ÃƒÆ'O
        # ---------------------------------------------------------

        self.produtos = 21
        self.segmentos = 18
        self.campanhas = 0

    # ------------------------------------------------------------

    def status(self, valor):

        return "ONLINE" if valor else "OFFLINE"

    # ------------------------------------------------------------

    def executar(self):

        print()

        print("=" * 70)
        print("IOTEC INTELLIGENCE COMMAND CENTER")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()

        print("MONITORAMENTO")

        print()

        print(f"Empresas..................... {self.empresas_monitoradas}")
        print(f"Oportunidades............... {self.oportunidades}")
        print(f"Corredores EconÃƒÂ´micos....... {self.corredores}")
        print(f"Cidades..................... {self.cidades}")
        print(f"PaÃƒÂ­ses...................... {self.paises}")

        print()

        print("=" * 70)

        print("MOTORES DE INTELIGÃƒÅ NCIA")

        print()

        print(f"Kernel...................... {self.status(self.kernel)}")
        print(f"Company Discovery........... {self.status(self.company_discovery)}")
        print(f"Opportunity Engine.......... {self.status(self.opportunity_engine)}")
        print(f"Market Intelligence......... {self.status(self.market_intelligence)}")
        print(f"Executive Reports........... {self.status(self.executive_reports)}")
        print(f"Newsroom.................... {self.status(self.newsroom)}")

        print()

        print("=" * 70)

        print("CAPACIDADE")

        print()

        print(f"Produtos.................... {self.produtos}")
        print(f"Segmentos................... {self.segmentos}")
        print(f"Campanhas................... {self.campanhas}")

        print()

        print("=" * 70)

        print("MISSÃƒâ€¢ES PRIORITÃƒÂRIAS")

        print()

        missoes = [

            "Expandir monitoramento empresarial.",

            "Mapear novos polos econÃƒÂ´micos.",

            "Descobrir novas oportunidades.",

            "Priorizar empresas estratÃƒÂ©gicas.",

            "Atualizar conhecimento corporativo.",

            "Alimentar o Centro Comercial.",

            "Alimentar o Centro de Marketing.",

            "Apoiar decisÃƒÂµes executivas."

        ]

        for numero, item in enumerate(missoes, 1):

            print(f"{numero}. {item}")

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O DO CENTRO")

        print()

        print("Transformar dados")
        print("em conhecimento.")

        print()

        print("Transformar conhecimento")
        print("em inteligÃƒÂªncia.")

        print()

        print("Transformar inteligÃƒÂªncia")
        print("em decisÃƒÂµes estratÃƒÂ©gicas.")

        print()

        print("=" * 70)

        print("INTELLIGENCE COMMAND CENTER ONLINE")

        print("=" * 70)


if __name__ == "__main__":

    IntelligenceCommandCenter().executar()



