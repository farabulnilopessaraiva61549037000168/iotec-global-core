import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC MARKETING COMMAND CENTER
FASE 02
ETAPA 002

VersÃƒÂ£o 4.0

======================================================================
"""

from datetime import datetime


class MarketingCommandCenter:

    VERSION = "4.0"

    def __init__(self):

        self.canais = {

            "Portal Institucional": False,

            "Landing Pages": False,

            "LinkedIn": False,

            "WhatsApp Business": False,

            "Instagram": False,

            "YouTube": False,

            "Google Business": False,

            "E-mail Corporativo": False,

            "FormulÃƒÂ¡rios": False,

            "VÃƒÂ­deos Institucionais": False,

            "PortfÃƒÂ³lio Comercial": False,

            "Tabela Comercial": False

        }

    # -------------------------------------------------------------

    def percentual(self):

        ativos = sum(self.canais.values())

        total = len(self.canais)

        return round((ativos/total)*100,2)

    # -------------------------------------------------------------

    def pendencias(self):

        return [

            canal

            for canal,status in self.canais.items()

            if not status

        ]

    # -------------------------------------------------------------

    def executar(self):

        print()

        print("="*70)

        print("IOTEC MARKETING COMMAND CENTER")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("CANAIS DIGITAIS")

        print()

        for canal,status in self.canais.items():

            situacao="ONLINE" if status else "OFFLINE"

            print(f"{canal:35} {situacao}")

        print()

        print("="*70)

        print("MATURIDADE")

        print()

        print(f"{self.percentual()} %")

        print()

        print("="*70)

        print("PENDÃƒÅ NCIAS")

        print()

        for item in self.pendencias():

            print("-",item)

        print()

        print("="*70)

        print("MISSÃƒâ€¢ES")

        print()

        missoes=[

            "Publicar Portal",

            "Ativar WhatsApp Business",

            "Concluir Landing Pages",

            "Publicar LinkedIn",

            "Criar VÃƒÂ­deos",

            "Publicar PortfÃƒÂ³lio",

            "Ativar Google Business",

            "Preparar Campanhas"

        ]

        for numero,item in enumerate(missoes,1):

            print(f"{numero}. {item}")

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Garantir que todos")

        print("os canais digitais")

        print("estejam operacionais")

        print("antes da expansÃƒÂ£o")

        print("comercial.")

        print()

        print("="*70)

        print("MARKETING COMMAND CENTER ONLINE")

        print("="*70)


if __name__=="__main__":

    MarketingCommandCenter().executar()



