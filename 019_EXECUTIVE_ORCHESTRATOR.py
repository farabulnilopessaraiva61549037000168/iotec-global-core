import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EXECUTIVE ORCHESTRATOR
MISSÃƒÆ'O 001

======================================================================
"""

from datetime import datetime


class ExecutiveOrchestrator:

    VERSION = "4.0"

    def __init__(self):

        self.status = {

            "Kernel": True,

            "Commercial Intelligence": True,

            "Revenue Mission": True,

            "Opportunity Engine": True,

            "Company Discovery": True,

            "Executive Reports": True,

            "Campaign Engine": True,

            "CRM": True,

            "Portal": False,

            "Landing Pages": False,

            "WhatsApp Business": False,

            "LinkedIn": False,

            "Instagram": False,

            "YouTube": False,

            "Produtos": False,

            "Tabela Comercial": False,

            "Pagamentos": False

        }

        self.missoes = [

            "Prospectar Empresas",

            "Transformar Leads em Propostas",

            "Fechar Contratos",

            "Gerar Receita"

        ]

    # ------------------------------------------------------------

    def percentual(self):

        ativos = sum(self.status.values())

        total = len(self.status)

        return round((ativos / total) * 100, 2)

    # ------------------------------------------------------------

    def executar(self):

        print()

        print("=" * 70)

        print("IOTEC EXECUTIVE ORCHESTRATOR")

        print("=" * 70)

        print(datetime.now())

        print("=" * 70)

        print()

        print("CENTRO DE COMANDO")

        print()

        for modulo, estado in self.status.items():

            situacao = "ONLINE" if estado else "OFFLINE"

            print(f"{modulo:30} {situacao}")

        print()

        print("=" * 70)

        print("MATURIDADE")

        print()

        print(f"{self.percentual()} %")

        print()

        print("=" * 70)

        print("MISSÃƒâ€¢ES")

        print()

        for indice, missao in enumerate(self.missoes, 1):

            print(f"{indice}. {missao}")

        print()

        print("=" * 70)

        print("ORDEM EXECUTIVA")

        print()

        print("Todo mÃƒÂ³dulo offline")

        print("deverÃƒÂ¡ tornar-se prioridade")

        print("atÃƒÂ© que toda a plataforma")

        print("esteja operacional.")

        print()

        print("=" * 70)

        print("STATUS GERAL")

        print()

        if self.percentual() >= 90:

            print("IOTEC PRONTA PARA ESCALAR.")

        elif self.percentual() >= 70:

            print("IOTEC EM FASE AVANÃƒâ€¡ADA.")

        elif self.percentual() >= 50:

            print("IOTEC EM CONSOLIDAÃƒâ€¡ÃƒÆ'O.")

        else:

            print("IOTEC EM IMPLANTAÃƒâ€¡ÃƒÆ'O.")

        print()

        print("=" * 70)

        print("EXECUTIVE ORCHESTRATOR ONLINE")

        print("=" * 70)


if __name__ == "__main__":

    ExecutiveOrchestrator().executar()



