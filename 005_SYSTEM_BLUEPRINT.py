"""
===============================================================================
005_SYSTEM_BLUEPRINT.py
Plano Diretor da Plataforma IOTEC
===============================================================================
"""

from datetime import datetime


class SystemBlueprint:

    def __init__(self):

        self.name = "IOTEC"

        self.version = "1.0"

        self.created = datetime.now()

        # ==============================================================
        # DOUTRINAS
        # ==============================================================

        self.doctrines = [

            "Nunca utilizar dados simulados em produÃ§Ã£o.",

            "Todo gargalo deve apresentar causa, impacto e soluÃ§Ã£o.",

            "Todo produto deve caminhar para monetizaÃ§Ã£o.",

            "Toda decisÃ£o importante deve gerar evento.",

            "Toda atividade deve ser observÃ¡vel.",

            "Toda integraÃ§Ã£o automÃ¡tica deve ser executada automaticamente.",

            "Somente tarefas humanas devem chegar ao operador.",

            "Nenhuma boa ideia pode ser perdida."

        ]

        # ==============================================================
        # MÃ"DULOS
        # ==============================================================

        self.modules = {

            "000_IOTEC_CORE": "OK",

            "001_MISSION_ORCHESTRATOR": "OK",

            "002_EVENT_BUS": "OK",

            "003_OBSERVABILITY_CORE": "OK",

            "004_INTEGRATION_MANAGER": "OK",

            "005_SYSTEM_BLUEPRINT": "OK"

        }

        # ==============================================================
        # PRIORIDADES
        # ==============================================================

        self.priorities = [

            "Conectar integraÃ§Ãµes reais",

            "Eliminar dados simulados",

            "Construir entidades tÃ©cnicas",

            "Criar equipes automÃ¡ticas",

            "Construir produtos",

            "Gerar receita"

        ]

        # ==============================================================
        # GARGALOS
        # ==============================================================

        self.bottlenecks = []

        # ==============================================================
        # PRODUTOS
        # ==============================================================

        self.products = []

        # ==============================================================
        # CAPACIDADES
        # ==============================================================

        self.capabilities = []

    # -----------------------------------------------------------------

    def add_bottleneck(self,
                       description):

        self.bottlenecks.append(description)

    # -----------------------------------------------------------------

    def add_product(self,
                    product):

        self.products.append(product)

    # -----------------------------------------------------------------

    def add_capability(self,
                       capability):

        self.capabilities.append(capability)

    # -----------------------------------------------------------------

    def report(self):

        print()

        print("=" * 70)

        print("IOTEC SYSTEM BLUEPRINT")

        print("=" * 70)

        print()

        print("VERSÃƒO")

        print(self.version)

        print()

        print("DOUTRINAS")

        for item in self.doctrines:

            print(f" â€¢ {item}")

        print()

        print("MÃ"DULOS")

        for module, status in self.modules.items():

            print(f" â€¢ {module:<35} {status}")

        print()

        print("PRIORIDADES")

        for item in self.priorities:

            print(f" â€¢ {item}")

        print()

        print(f"GARGALOS............... {len(self.bottlenecks)}")

        print(f"PRODUTOS............... {len(self.products)}")

        print(f"CAPACIDADES............ {len(self.capabilities)}")

        print()


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    blueprint = SystemBlueprint()

    blueprint.add_bottleneck(

        "IntegraÃ§Ã£o com CRM ainda nÃ£o realizada."

    )

    blueprint.add_bottleneck(

        "Gateway de pagamento nÃ£o integrado."

    )

    blueprint.add_capability(

        "Mission Orchestrator"

    )

    blueprint.add_capability(

        "Enterprise Event Bus"

    )

    blueprint.report()

