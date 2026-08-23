import requests
import json
from datetime import datetime

from PAYMENT_PROVIDER_ENGINE import PaymentProviderEngine


class PaymentExecutionEngine:

    def __init__(self):

        self.provider = PaymentProviderEngine()

        self.server = "http://127.0.0.1:5001"

    # ------------------------------------------------------------

    def health(self):

        try:

            r = requests.get(

                self.server + "/health",

                timeout=5

            )

            return r.status_code == 200

        except:

            return False

    # ------------------------------------------------------------

    def create_payment(self):

        if not self.health():

            print()

            print("==========================================")
            print("PAYPAL SERVER OFFLINE")
            print("==========================================")

            return

        print()

        print("==========================================")
        print("SOLICITANDO NOVA COBRANÃƒâ€¡A")
        print("==========================================")

        r = requests.get(

            self.server + "/criar-pagamento",

            timeout=60

        )

        dados = r.json()

        print()

        print("==========================================")
        print("ORDEM RECEBIDA")
        print("==========================================")

        print(json.dumps(

            dados,

            indent=4,

            ensure_ascii=False

        ))

        print()

        print("==========================================")

        print("STATUS")

        print("==========================================")

        print("Gateway.......: PAYPAL")

        print("Data..........:", datetime.now())

        if "url" in dados:

            print("Checkout......:", dados["url"])

        elif "approve_url" in dados:

            print("Checkout......:", dados["approve_url"])

        else:

            print("Checkout......: NÃƒÆ'O INFORMADO")

        print("==========================================")

        return dados


# ===============================================================

if __name__ == "__main__":

    PaymentExecutionEngine().create_payment()

