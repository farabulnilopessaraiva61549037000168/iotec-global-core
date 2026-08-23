import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC ENTERPRISE DASHBOARD
FASE 04
ETAPA 003

VersÃƒÂ£o 5.0

======================================================================
"""

from datetime import datetime


class EnterpriseDashboard:

    VERSION = "5.0"

    def __init__(self):

        # -------------------------------------------------------
        # EXECUTIVO
        # -------------------------------------------------------

        self.status_empresa = "EM EXPANSÃƒÆ'O"

        # -------------------------------------------------------
        # COMERCIAL
        # -------------------------------------------------------

        self.empresas = 483
        self.oportunidades = 84
        self.leads = 3
        self.reunioes = 0
        self.propostas = 0
        self.contratos = 0

        # -------------------------------------------------------
        # FINANCEIRO
        # -------------------------------------------------------

        self.pipeline = 17500.00
        self.receita = 0.00
        self.meta = 5000000.00

        # -------------------------------------------------------
        # MARKETING
        # -------------------------------------------------------

        self.marketing = 0

        # -------------------------------------------------------
        # INTELIGÃƒÅ NCIA
        # -------------------------------------------------------

        self.produtos = 21
        self.segmentos = 18

        # -------------------------------------------------------
        # EXECUÃƒâ€¡ÃƒÆ'O
        # -------------------------------------------------------

        self.workflow = 12.5

        self.tarefas = 8

        self.missoes = 8

    # ----------------------------------------------------------

    def percentual_meta(self):

        if self.meta == 0:

            return 0

        return round(

            (self.pipeline/self.meta)*100,

            2

        )

    # ----------------------------------------------------------

    def executar(self):

        print()

        print("="*70)

        print("IOTEC ENTERPRISE DASHBOARD")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("STATUS GERAL")

        print()

        print(self.status_empresa)

        print()

        print("="*70)

        print("COMERCIAL")

        print()

        print(f"Empresas.............. {self.empresas}")

        print(f"Oportunidades......... {self.oportunidades}")

        print(f"Leads................. {self.leads}")

        print(f"ReuniÃƒÂµes.............. {self.reunioes}")

        print(f"Propostas............. {self.propostas}")

        print(f"Contratos............. {self.contratos}")

        print()

        print("="*70)

        print("FINANCEIRO")

        print()

        print(f"Pipeline.............. R$ {self.pipeline:,.2f}")

        print(f"Receita............... R$ {self.receita:,.2f}")

        print(f"Meta.................. R$ {self.meta:,.2f}")

        print(f"Meta Atingida......... {self.percentual_meta()} %")

        print()

        print("="*70)

        print("MARKETING")

        print()

        print(f"Maturidade............ {self.marketing}%")

        print()

        print("="*70)

        print("INTELIGÃƒÅ NCIA")

        print()

        print(f"Produtos.............. {self.produtos}")

        print(f"Segmentos............. {self.segmentos}")

        print()

        print("="*70)

        print("EXECUÃƒâ€¡ÃƒÆ'O")

        print()

        print(f"Workflow.............. {self.workflow}%")

        print(f"Tarefas............... {self.tarefas}")

        print(f"MissÃƒÂµes............... {self.missoes}")

        print()

        print("="*70)

        print("MISSÃƒÆ'O PRIORITÃƒÂRIA")

        print()

        print("Transformar")

        print("Leads")

        print("Ã¢â€ â€œ")

        print("Propostas")

        print("Ã¢â€ â€œ")

        print("Contratos")

        print("Ã¢â€ â€œ")

        print("Receita")

        print()

        print("="*70)

        print("ENTERPRISE DASHBOARD ONLINE")

        print("="*70)


if __name__=="__main__":

    EnterpriseDashboard().executar()



