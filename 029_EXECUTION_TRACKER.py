import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EXECUTION TRACKER
FASE 04
ETAPA 002

VersÃƒÂ£o 5.0

======================================================================
"""

from datetime import datetime


class ExecutionTracker:

    VERSION = "5.0"

    def __init__(self):

        self.workflow = [

            ("Empresa Identificada","CONCLUÃƒÂDA"),
            ("Lead Gerado","EM EXECUÃƒâ€¡ÃƒÆ'O"),
            ("ReuniÃƒÂ£o Agendada","PENDENTE"),
            ("Proposta Enviada","PENDENTE"),
            ("Contrato Assinado","PENDENTE"),
            ("Pagamento Recebido","PENDENTE"),
            ("ImplantaÃƒÂ§ÃƒÂ£o","PENDENTE"),
            ("Cliente Fidelizado","PENDENTE")

        ]

    # -----------------------------------------------------

    def percentual(self):

        concluidas = sum(

            1 for _,status in self.workflow

            if status=="CONCLUÃƒÂDA"

        )

        return round(

            (concluidas/len(self.workflow))*100,

            2

        )

    # -----------------------------------------------------

    def executar(self):

        print()

        print("="*70)
        print("IOTEC EXECUTION TRACKER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("ACOMPANHAMENTO")

        print()

        for numero,(etapa,status) in enumerate(self.workflow,1):

            print(f"[{numero:02}] {etapa}")

            print(f"     Status..... {status}")

            print()

        print("="*70)

        print("PROGRESSO")

        print()

        print(f"{self.percentual()} %")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA ETAPA")

        print()

        for etapa,status in self.workflow:

            if status=="EM EXECUÃƒâ€¡ÃƒÆ'O":

                print(etapa)

                break

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Toda oportunidade")

        print("deverÃƒÂ¡ avanÃƒÂ§ar")

        print("continuamente")

        print("atÃƒÂ© a fidelizaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("EXECUTION TRACKER ONLINE")

        print("="*70)


if __name__=="__main__":

    ExecutionTracker().executar()



