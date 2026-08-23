import requests

from PAYMENT_LINK_ENGINE import PaymentLinkEngine
from GATEWAY_CONFIGURATION_ENGINE import GatewayConfigurationEngine


class PaymentProviderEngine:

    def __init__(self):

        self.cfg = GatewayConfigurationEngine()

        self.cfg.load()

    # --------------------------------------------------------

    def get_active_gateway(self):

        return self.cfg.config["active_gateway"]

    # --------------------------------------------------------

    def get_gateway_config(self):

        gateway = self.get_active_gateway()

        return self.cfg.config["gateways"][gateway]

    # --------------------------------------------------------

    def create_payment(self,
                       client,
                       description,
                       value):

        gateway = self.get_active_gateway()

        info = self.get_gateway_config()

        payment = PaymentLinkEngine().create(

            client,

            description,

            value

        )

        print()

        print("====================================================")
        print("PAYMENT PROVIDER ENGINE")
        print("====================================================")
        print("Gateway........:", gateway)
        print("Ambiente.......:", self.cfg.config["environment"])
        print("Base URL.......:", info["base_url"])
        print("====================================================")

        if gateway == "PAYPAL":

            print()

            print("AGUARDANDO CREDENCIAIS PAYPAL")

            print()

        elif gateway == "MERCADOPAGO":

            print()

            print("AGUARDANDO ACCESS TOKEN")

            print()

        elif gateway == "ASAAS":

            print()

            print("AGUARDANDO API KEY")

            print()

        elif gateway == "PICPAY":

            print()

            print("AGUARDANDO TOKEN")

            print()

        return payment


# ===========================================================

if __name__ == "__main__":

    engine = PaymentProviderEngine()

    engine.create_payment(

        client="PRESIDÃƒÅ NCIA IOTEC",

        description="HomologaÃƒÂ§ÃƒÂ£o Primeiro PavilhÃƒÂ£o",

        value=29.90

    )

