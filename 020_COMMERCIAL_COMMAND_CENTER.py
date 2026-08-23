import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC COMMERCIAL COMMAND CENTER
FASE 02
ETAPA 001

VersÃƒÂ£o 4.0

======================================================================
"""

from datetime import datetime


class CommercialCommandCenter:

    VERSION = "4.0"

    def __init__(self):

        # -------------------------------
        # Empresas
        # -------------------------------

        self.empresas = 483
        self.oportunidades = 84

        # -------------------------------
        # Funil Comercial
        # -------------------------------

        self.leads = 3
        self.reunioes = 0
        self.propostas = 0
        self.contratos = 0

        # -------------------------------
        # Financeiro
        # -------------------------------

        self.pipeline = 17500.00
        self.receita = 0.00
        self.meta = 5000000.00

        # -------------------------------
        # Produtos
        # -------------------------------

        self.produtos = 21

        # -------------------------------
        # Campanhas
        # -------------------------------

        self.campanhas = 0

    # ======================================================

    def percentual_meta(self):

        if self.meta == 0:
            return 0

        return round(
            (self.pipeline / self.meta) * 100,
            2
        )

    # ======================================================

    def taxa_conversao(self):

        if self.leads == 0:
            return 0

        return round(
            (self.contratos / self.leads) * 100,
            2
        )

    # ======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC COMMERCIAL COMMAND CENTER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("EMPRESAS")

        print()

        print(f"Empresas Monitoradas..... {self.empresas}")

        print(f"Oportunidades............ {self.oportunidades}")

        print()

        print("="*70)

        print("FUNIL COMERCIAL")

        print()

        print(f"Leads.................... {self.leads}")

        print(f"ReuniÃƒÂµes................. {self.reunioes}")

        print(f"Propostas................ {self.propostas}")

        print(f"Contratos................ {self.contratos}")

        print()

        print("="*70)

        print("FINANCEIRO")

        print()

        print(f"Pipeline................. R$ {self.pipeline:,.2f}")

        print(f"Receita.................. R$ {self.receita:,.2f}")

        print(f"Meta..................... R$ {self.meta:,.2f}")

        print(f"Meta Atingida............ {self.percentual_meta()} %")

        print()

        print("="*70)

        print("PRODUÃƒâ€¡ÃƒÆ'O")

        print()

        print(f"Produtos................. {self.produtos}")

        print(f"Campanhas............... {self.campanhas}")

        print()

        print("="*70)

        print("INDICADORES")

        print()

        print(f"ConversÃƒÂ£o............... {self.taxa_conversao()} %")

        print()

        print("="*70)

        print("MISSÃƒâ€¢ES PRIORITÃƒÂRIAS")

        print()

        missoes = [

            "Gerar novos Leads",

            "Transformar Leads em ReuniÃƒÂµes",

            "Transformar ReuniÃƒÂµes em Propostas",

            "Transformar Propostas em Contratos",

            "Gerar Receita",

            "Fidelizar Clientes"

        ]

        for i, missao in enumerate(missoes,1):

            print(f"{i}. {missao}")

        print()

        print("="*70)

        print("OBJETIVO EXECUTIVO")

        print()

        print("O Centro Comercial deverÃƒÂ¡")

        print("acompanhar continuamente")

        print("todo o funil de vendas,")

        print("identificando gargalos")

        print("e orientando aÃƒÂ§ÃƒÂµes")

        print("para aumentar a conversÃƒÂ£o.")

        print()

        print("="*70)

        print("COMMERCIAL COMMAND CENTER ONLINE")

        print("="*70)


# ==========================================================

if __name__ == "__main__":

    CommercialCommandCenter().executar()



