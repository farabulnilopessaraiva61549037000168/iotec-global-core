import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC ENTERPRISE MISSION ENGINE
FASE 03
ETAPA 003

VersÃƒÂ£o 5.0

======================================================================
"""

from datetime import datetime


class EnterpriseMissionEngine:

    VERSION = "5.0"

    def __init__(self):

        self.missoes = [

            {
                "id": 1,
                "titulo": "Ativar WhatsApp Business",
                "area": "Marketing",
                "prioridade": "CRÃƒÂTICA",
                "status": "PENDENTE"
            },

            {
                "id": 2,
                "titulo": "Publicar Portal Institucional",
                "area": "Marketing",
                "prioridade": "CRÃƒÂTICA",
                "status": "PENDENTE"
            },

            {
                "id": 3,
                "titulo": "Concluir Landing Pages",
                "area": "Marketing",
                "prioridade": "ALTA",
                "status": "PENDENTE"
            },

            {
                "id": 4,
                "titulo": "Cadastrar Produtos",
                "area": "Comercial",
                "prioridade": "ALTA",
                "status": "PENDENTE"
            },

            {
                "id": 5,
                "titulo": "Gerar 20 novos Leads",
                "area": "Comercial",
                "prioridade": "ALTA",
                "status": "PENDENTE"
            },

            {
                "id": 6,
                "titulo": "Enviar 10 propostas",
                "area": "Comercial",
                "prioridade": "ALTA",
                "status": "PENDENTE"
            },

            {
                "id": 7,
                "titulo": "Fechar o primeiro contrato",
                "area": "Comercial",
                "prioridade": "MÃƒÂXIMA",
                "status": "PENDENTE"
            },

            {
                "id": 8,
                "titulo": "Receber o primeiro pagamento",
                "area": "Financeiro",
                "prioridade": "MÃƒÂXIMA",
                "status": "PENDENTE"
            }

        ]

    # ------------------------------------------------------------

    def executar(self):

        print()

        print("=" * 70)
        print("IOTEC ENTERPRISE MISSION ENGINE")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()

        print("MISSÃƒâ€¢ES CORPORATIVAS")

        print()

        for missao in self.missoes:

            print(f"[{missao['id']:02}] {missao['titulo']}")
            print(f"     ÃƒÂrea....... {missao['area']}")
            print(f"     Prioridade. {missao['prioridade']}")
            print(f"     Status..... {missao['status']}")
            print()

        print("=" * 70)

        print("SEQUÃƒÅ NCIA ESTRATÃƒâ€°GICA")

        print()

        fluxo = [

            "Marketing pronto",

            "Mais visitantes",

            "Mais Leads",

            "Mais reuniÃƒÂµes",

            "Mais propostas",

            "Mais contratos",

            "Mais receita",

            "Clientes recorrentes"

        ]

        for numero, etapa in enumerate(fluxo, 1):

            print(f"{numero}. {etapa}")

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O DO KERNEL")

        print()

        print("Priorizar automaticamente")
        print("as missÃƒÂµes com maior")
        print("impacto na geraÃƒÂ§ÃƒÂ£o")
        print("de receita.")

        print()

        print("=" * 70)

        print("ENTERPRISE MISSION ENGINE ONLINE")

        print("=" * 70)


if __name__ == "__main__":

    EnterpriseMissionEngine().executar()



