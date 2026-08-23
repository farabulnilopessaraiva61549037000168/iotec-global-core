import uuid
from datetime import datetime

from PAYMENT_GATEWAY_MANAGER import PaymentGatewayManager
from GATEWAY_CONFIGURATION_ENGINE import GatewayConfigurationEngine


class PaymentLinkEngine:

    def __init__(self):

        self.gateway = PaymentGatewayManager()

        self.config = GatewayConfigurationEngine()

        self.config.load()

    # ---------------------------------------------------------

    def create(self, client, description, value):

        provider = self.config.config["active_gateway"]

        self.gateway.set_provider(provider)

        payment = self.gateway.create_payment(

            client=client,

            description=description,

            value=value

        )

        payment["reference"] = "IOTEC-" + uuid.uuid4().hex[:12].upper()

        payment["payment_url"] = None

        payment["qr_code"] = None

        payment["environment"] = self.config.config["environment"]

        print("==================================================")
        print("PAYMENT LINK ENGINE")
        print("==================================================")
        print(f"Gateway......: {provider}")
        print(f"ReferÃƒÂªncia...: {payment['reference']}")
        print(f"Ambiente.....: {payment['environment']}")
        print("Status.......: LINK PENDENTE")
        print("==================================================")

        return payment


# ------------------------------------------------------------

if __name__ == "__main__":

    engine = PaymentLinkEngine()

    engine.create(

        client="PRESIDÃƒÅ NCIA IOTEC",

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o",

        value=29.90

    )

