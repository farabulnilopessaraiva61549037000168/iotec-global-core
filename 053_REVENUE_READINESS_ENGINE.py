import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC REVENUE READINESS ENGINE
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Verificador de ProntidÃƒÂ£o Comercial

======================================================================
"""

from datetime import datetime


class RevenueReadinessEngine:

    def __init__(self):

        self.itens = [

            ("Telefone Comercial", True),

            ("WhatsApp Business", False),

            ("E-mail Corporativo", True),

            ("Portal Institucional", False),

            ("Landing Page", False),

            ("LinkedIn Corporativo", False),

            ("Google Business", False),

            ("CatÃƒÂ¡logo Comercial", False),

            ("Tabela de PreÃƒÂ§os", False),

            ("FormulÃƒÂ¡rio de Contato", False),

            ("CRM", True),

            ("Banco Corporativo", True),

            ("Pipeline Comercial", True),

            ("Produtos Cadastrados", True),

            ("Meio de Pagamento", False)

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC REVENUE READINESS ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        concluidos = 0

        print()

        print("CHECKLIST DE RECEITA")

        print()

        for item, status in self.itens:

            if status:

                print("[Ã¢Å"â€œ]", item)

                concluidos += 1

            else:

                print("[ ]", item)

        percentual = (concluidos / len(self.itens)) * 100

        print()

        print("="*70)

        print("PRONTIDÃƒÆ'O COMERCIAL")

        print()

        print(f"{percentual:.1f}%")

        print()

        print("="*70)

        if percentual < 40:

            nivel = "EM IMPLANTAÃƒâ€¡ÃƒÆ'O"

        elif percentual < 70:

            nivel = "PRÃƒâ€°-OPERAÃƒâ€¡ÃƒÆ'O"

        elif percentual < 90:

            nivel = "OPERACIONAL"

        else:

            nivel = "PRONTA PARA ESCALAR"

        print("STATUS")

        print()

        print(nivel)

        print()

        print("="*70)

        print("BLOQUEADORES DA RECEITA")

        print()

        for item, status in self.itens:

            if not status:

                print("Ã¢â‚¬Â¢", item)

        print()

        print("="*70)

        print("MISSÃƒÆ'O DO KERNEL")

        print()

        print("Eliminar um bloqueador")
        print("por vez atÃƒÂ© que")
        print("a plataforma esteja")
        print("100% preparada")
        print("para gerar receita.")

        print()

        print("="*70)

        print("REVENUE READINESS ONLINE")

        print("="*70)


if __name__ == "__main__":

    RevenueReadinessEngine().executar()



