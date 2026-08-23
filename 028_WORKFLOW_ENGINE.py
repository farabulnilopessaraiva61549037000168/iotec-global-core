import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC WORKFLOW ENGINE
FASE 04
ETAPA 001

VersÃƒÂ£o 5.0

======================================================================
"""

from datetime import datetime


class WorkflowEngine:

    VERSION = "5.0"

    def __init__(self):

        self.workflow = [

            {
                "ordem":1,
                "etapa":"Empresa Identificada",
                "origem":"Intelligence",
                "destino":"Commercial",
                "status":"ATIVO"
            },

            {
                "ordem":2,
                "etapa":"Lead Gerado",
                "origem":"Commercial",
                "destino":"CRM",
                "status":"AGUARDANDO"
            },

            {
                "ordem":3,
                "etapa":"ReuniÃƒÂ£o Agendada",
                "origem":"CRM",
                "destino":"Commercial",
                "status":"AGUARDANDO"
            },

            {
                "ordem":4,
                "etapa":"Proposta Enviada",
                "origem":"Commercial",
                "destino":"Cliente",
                "status":"AGUARDANDO"
            },

            {
                "ordem":5,
                "etapa":"Contrato Assinado",
                "origem":"Cliente",
                "destino":"Financeiro",
                "status":"AGUARDANDO"
            },

            {
                "ordem":6,
                "etapa":"Pagamento Recebido",
                "origem":"Financeiro",
                "destino":"OperaÃƒÂ§ÃƒÂ£o",
                "status":"AGUARDANDO"
            },

            {
                "ordem":7,
                "etapa":"ImplantaÃƒÂ§ÃƒÂ£o",
                "origem":"OperaÃƒÂ§ÃƒÂ£o",
                "destino":"Customer Success",
                "status":"AGUARDANDO"
            },

            {
                "ordem":8,
                "etapa":"Cliente Fidelizado",
                "origem":"Customer Success",
                "destino":"Revenue",
                "status":"AGUARDANDO"
            }

        ]

    # ---------------------------------------------------------

    def executar(self):

        print()

        print("="*70)
        print("IOTEC WORKFLOW ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("FLUXO OPERACIONAL")

        print()

        for etapa in self.workflow:

            print(f"[{etapa['ordem']:02}] {etapa['etapa']}")
            print(f"     Origem..... {etapa['origem']}")
            print(f"     Destino.... {etapa['destino']}")
            print(f"     Status..... {etapa['status']}")
            print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Nenhuma oportunidade")
        print("deverÃƒÂ¡ ficar parada")
        print("entre duas etapas")
        print("do fluxo operacional.")

        print()

        print("="*70)

        print("WORKFLOW ENGINE ONLINE")

        print("="*70)


if __name__=="__main__":

    WorkflowEngine().executar()



