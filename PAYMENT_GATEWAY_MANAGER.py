import uuid
from datetime import datetime


class PaymentGatewayManager:

    VERSION = "1.0"

    DEFAULT_PROVIDER = "PAYPAL"

    def __init__(self):

        self.provider = self.DEFAULT_PROVIDER

    # ---------------------------------------------------------

    def set_provider(self, provider):

        self.provider = provider.upper()

    # ---------------------------------------------------------

    def create_payment(
        self,
        client,
        description,
        value
    ):

        payment = {

            "payment_id": str(uuid.uuid4()),

            "provider": self.provider,

            "client": client,

            "description": description,

            "value": float(value),

            "status": "CREATED",

            "created_at": datetime.now().isoformat()

        }

        print("")
        print("==================================================")
        print("PAYMENT GATEWAY MANAGER")
        print("==================================================")
        print(f"Gateway......: {payment['provider']}")
        print(f"ID...........: {payment['payment_id']}")
        print(f"Cliente......: {payment['client']}")
        print(f"DescriÃƒÂ§ÃƒÂ£o....: {payment['description']}")
        print(f"Valor........: R$ {payment['value']:.2f}")
        print(f"Status.......: {payment['status']}")
        print("==================================================")
        print("")

        return payment


if __name__ == "__main__":

    gateway = PaymentGatewayManager()

    gateway.create_payment(

        client="PRESIDÃƒÅ NCIA IOTEC",

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o",

        value=29.90

    )

