import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC OPERATION CENTER

017 - AUTONOMOUS EXECUTIVE ENGINE

VersÃƒÂ£o 3.0

======================================================================
"""

from datetime import datetime


class AutonomousExecutiveEngine:

    def __init__(self):

        self.meta = 5000000.00

        self.receita = 0.00

        self.pipeline = 17500.00

        self.leads = 3

        self.propostas = 0

        self.contratos = 0

        self.prioridades = [

            "Concluir WhatsApp Business",

            "Publicar Portal Institucional",

            "Cadastrar Produtos",

            "Concluir Landing Pages",

            "Ativar LinkedIn",

            "Preparar Campanha Comercial",

            "Prospectar Empresas",

            "Agendar ReuniÃƒÂµes"

        ]

    # ------------------------------------------------------------

    def percentual_meta(self):

        if self.meta == 0:

            return 0

        return round(

            (self.pipeline / self.meta) * 100,

            2

        )

    # ------------------------------------------------------------

    def executar(self):

        print()

        print("=" * 70)

        print("AUTONOMOUS EXECUTIVE ENGINE")

        print("=" * 70)

        print(datetime.now())

        print("=" * 70)

        print()

        print("RELATÃƒâ€œRIO EXECUTIVO")

        print()

        print(f"Pipeline............. R$ {self.pipeline:,.2f}")

        print(f"Receita.............. R$ {self.receita:,.2f}")

        print(f"Meta................. R$ {self.meta:,.2f}")

        print(f"Meta Atingida........ {self.percentual_meta()} %")

        print()

        print("=" * 70)

        print("INDICADORES")

        print()

        print(f"Leads................ {self.leads}")

        print(f"Propostas............ {self.propostas}")

        print(f"Contratos............ {self.contratos}")

        print()

        print("=" * 70)

        print("PRIORIDADES DO DIA")

        print()

        for numero, item in enumerate(self.prioridades, 1):

            print(f"{numero}. {item}")

        print()

        print("=" * 70)

        print("ANÃƒÂLISE")

        print()

        if self.leads == 0:

            print("Prioridade mÃƒÂ¡xima: gerar novos Leads.")

        elif self.propostas == 0:

            print("Prioridade mÃƒÂ¡xima: transformar Leads em propostas.")

        elif self.contratos == 0:

            print("Prioridade mÃƒÂ¡xima: converter propostas em contratos.")

        else:

            print("Prioridade mÃƒÂ¡xima: expandir carteira de clientes.")

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O DO DIA")

        print()

        print("Toda atividade deverÃƒÂ¡")

        print("aproximar a IOTEC")

        print("do prÃƒÂ³ximo contrato.")

        print()

        print("=" * 70)

        print("EXECUTIVE ENGINE FINALIZADA")

        print("=" * 70)


if __name__ == "__main__":

    AutonomousExecutiveEngine().executar()



