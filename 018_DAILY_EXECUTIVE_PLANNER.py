import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC OPERATION CENTER

018 - DAILY EXECUTIVE PLANNER

VersÃƒÂ£o 3.0

======================================================================
"""

from datetime import datetime


class DailyExecutivePlanner:

    VERSION = "3.0"

    def __init__(self):

        self.meta_mensal = 5000000.00
        self.receita = 0.00
        self.pipeline = 17500.00

        self.leads = 3
        self.propostas = 0
        self.contratos = 0

        self.prioridades = []

    # ---------------------------------------------------------

    def analisar(self):

        self.prioridades.clear()

        if self.leads < 10:

            self.prioridades.append(
                "Prospectar novas empresas."
            )

        if self.propostas == 0:

            self.prioridades.append(
                "Preparar propostas comerciais."
            )

        if self.contratos == 0:

            self.prioridades.append(
                "Converter propostas em contratos."
            )

        if self.receita == 0:

            self.prioridades.append(
                "Priorizar geraÃƒÂ§ÃƒÂ£o de receita."
            )

        if self.pipeline < 100000:

            self.prioridades.append(
                "Expandir pipeline comercial."
            )

    # ---------------------------------------------------------

    def executar(self):

        self.analisar()

        print()

        print("="*70)
        print("IOTEC DAILY EXECUTIVE PLANNER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("SITUAÃƒâ€¡ÃƒÆ'O ATUAL")

        print()

        print(f"Receita............... R$ {self.receita:,.2f}")

        print(f"Pipeline.............. R$ {self.pipeline:,.2f}")

        print(f"Leads................. {self.leads}")

        print(f"Propostas............ {self.propostas}")

        print(f"Contratos............ {self.contratos}")

        print()

        print("="*70)

        print("PLANO EXECUTIVO DO DIA")

        print()

        for numero, tarefa in enumerate(self.prioridades,1):

            print(f"{numero}. {tarefa}")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Executar primeiro")

        print("as tarefas com")

        print("maior impacto")

        print("na geraÃƒÂ§ÃƒÂ£o de receita.")

        print()

        print("="*70)

        print("PLANNER FINALIZADO")

        print("="*70)


if __name__=="__main__":

    DailyExecutivePlanner().executar()



