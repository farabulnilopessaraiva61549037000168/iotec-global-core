"""
===============================================================================
004_INTEGRATION_MANAGER.py
Gerenciador Central de IntegraÃ§Ãµes da IOTEC
===============================================================================
"""

from enum import Enum
from datetime import datetime


# =============================================================================
# STATUS
# =============================================================================

class IntegrationStatus(Enum):

    NOT_CONFIGURED = "NOT_CONFIGURED"

    WAITING = "WAITING"

    CONNECTING = "CONNECTING"

    CONNECTED = "CONNECTED"

    FAILED = "FAILED"


# =============================================================================
# INTEGRAÃ‡ÃƒO
# =============================================================================

class Integration:

    def __init__(
            self,
            name,
            description,
            estimated_time,
            benefits):

        self.name = name

        self.description = description

        self.estimated_time = estimated_time

        self.benefits = benefits

        self.status = IntegrationStatus.NOT_CONFIGURED

        self.last_check = None


# =============================================================================
# GERENCIADOR
# =============================================================================

class IntegrationManager:

    def __init__(self):

        self.integrations = {}

    # -------------------------------------------------------------------------

    def register(self,
                 integration):

        self.integrations[integration.name] = integration

        print(f"[REGISTER] {integration.name}")

    # -------------------------------------------------------------------------

    def connected(self, name):

        if name in self.integrations:

            self.integrations[name].status = IntegrationStatus.CONNECTED

            self.integrations[name].last_check = datetime.now()

    # -------------------------------------------------------------------------

    def failed(self, name):

        if name in self.integrations:

            self.integrations[name].status = IntegrationStatus.FAILED

            self.integrations[name].last_check = datetime.now()

    # -------------------------------------------------------------------------

    def validate(self):

        print()

        print("=" * 70)

        print("IOTEC INTEGRATION STATUS")

        print("=" * 70)

        print()

        for integration in self.integrations.values():

            print(f"INTEGRAÃ‡ÃƒO : {integration.name}")

            print(f"STATUS.....: {integration.status.value}")

            if integration.status != IntegrationStatus.CONNECTED:

                print()

                print("MOTIVO")

                print(integration.description)

                print()

                print("TEMPO ESTIMADO")

                print(integration.estimated_time)

                print()

                print("BENEFÃCIOS")

                for benefit in integration.benefits:

                    print(f"  â€¢ {benefit}")

            print()

            print("-" * 70)

    # -------------------------------------------------------------------------

    def ready(self):

        return all(

            integration.status == IntegrationStatus.CONNECTED

            for integration in self.integrations.values()

        )


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    manager = IntegrationManager()

    manager.register(

        Integration(

            "CRM",

            "IntegraÃ§Ã£o necessÃ¡ria para clientes reais.",

            "2 horas",

            [

                "Clientes reais",

                "HistÃ³rico comercial",

                "Pipeline de vendas"

            ]

        )

    )

    manager.register(

        Integration(

            "PAYMENT_GATEWAY",

            "IntegraÃ§Ã£o necessÃ¡ria para pagamentos reais.",

            "1 hora",

            [

                "Recebimento automÃ¡tico",

                "ConciliaÃ§Ã£o financeira",

                "Receita em tempo real"

            ]

        )

    )

    manager.validate()

    if manager.ready():

        print("\n>>> Plataforma pronta para operar.\n")

    else:

        print("\n>>> Plataforma NÃƒO pode operar com dados reais.\n")

