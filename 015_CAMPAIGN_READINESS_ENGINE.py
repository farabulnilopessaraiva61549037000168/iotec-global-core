import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC OPERATION CENTER

015 - CAMPAIGN READINESS ENGINE

VersÃƒÂ£o 3.0

======================================================================
"""

from datetime import datetime


class CampaignReadinessEngine:

    VERSION = "3.0"

    def __init__(self):

        self.itens = {

            # IDENTIDADE

            "Portal Institucional": False,
            "Landing Pages": False,
            "Logomarca": False,
            "PortfÃƒÂ³lio": False,

            # COMUNICAÃƒâ€¡ÃƒÆ'O

            "LinkedIn": False,
            "WhatsApp Business": False,
            "Instagram": False,
            "YouTube": False,
            "E-mail Corporativo": False,

            # COMERCIAL

            "CRM": False,
            "Pipeline": False,
            "Produtos": False,
            "Tabela de PreÃƒÂ§os": False,
            "Propostas": False,
            "Contratos": False,

            # FINANCEIRO

            "Pagamento": False,
            "PIX": False,
            "Conta Empresarial": False,

            # MARKETING

            "VÃƒÂ­deos": False,
            "Campanhas": False,
            "CTA": False,
            "FormulÃƒÂ¡rios": False,

            # INTELIGÃƒÅ NCIA

            "Opportunity Engine": True,
            "Revenue Mission": True,
            "Executive Reports": True,
            "Commercial Intelligence": True,
            "Kernel": True

        }

    # ----------------------------------------------------------

    def percentual(self):

        total = len(self.itens)

        ativos = sum(self.itens.values())

        return round((ativos / total) * 100, 2)

    # ----------------------------------------------------------

    def pendencias(self):

        return [

            nome

            for nome, status in self.itens.items()

            if not status

        ]

    # ----------------------------------------------------------

    def executar(self):

        print()

        print("=" * 70)

        print("IOTEC CAMPAIGN READINESS ENGINE")

        print("=" * 70)

        print(datetime.now())

        print("=" * 70)

        print()

        print("VERIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        for nome, status in self.itens.items():

            if status:

                print(f"[ OK ] {nome}")

            else:

                print(f"[PEND] {nome}")

        print()

        print("=" * 70)

        percentual = self.percentual()

        print("MATURIDADE OPERACIONAL")

        print()

        print(f"{percentual}%")

        print()

        print("=" * 70)

        print("PENDÃƒÅ NCIAS")

        print()

        for item in self.pendencias():

            print("-", item)

        print()

        print("=" * 70)

        if percentual >= 90:

            print("STATUS")

            print()

            print("CAMPANHA LIBERADA")

        else:

            print("STATUS")

            print()

            print("CAMPANHA BLOQUEADA")

        print()

        print("=" * 70)

        print("PRÃƒâ€œXIMAS AÃƒâ€¡Ãƒâ€¢ES")

        print()

        prioridades = [

            "Concluir canais digitais.",

            "Concluir meios de pagamento.",

            "Finalizar Landing Pages.",

            "Preparar campanha.",

            "Iniciar divulgaÃƒÂ§ÃƒÂ£o.",

            "Monitorar indicadores.",

            "Converter Leads.",

            "Fechar contratos."

        ]

        for i, item in enumerate(prioridades, 1):

            print(f"{i}. {item}")

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O")

        print()

        print("Nenhuma campanha deverÃƒÂ¡ iniciar")

        print("sem que os recursos crÃƒÂ­ticos")

        print("estejam operacionais.")

        print()

        print("=" * 70)

        print("ENGINE FINALIZADA")

        print("=" * 70)


# ======================================================================

if __name__ == "__main__":

    CampaignReadinessEngine().executar()



