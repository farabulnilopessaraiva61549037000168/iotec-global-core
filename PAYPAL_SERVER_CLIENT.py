import requests
import json


class PayPalServerClient:

    def __init__(self):

        self.base_url = "http://127.0.0.1:5001"

    # ---------------------------------------------------------

    def health(self):

        r = requests.get(

            self.base_url + "/health",

            timeout=10

        )

        print()

        print("=" * 60)

        print("PAYPAL SERVER")

        print("=" * 60)

        print(r.text)

        print("=" * 60)

    # ---------------------------------------------------------

    def create_payment(self):

        r = requests.get(

            self.base_url + "/criar-pagamento",

            timeout=60

        )

        print()

        print("=" * 60)

        print("RESPOSTA DO SERVIDOR")

        print("=" * 60)

        print(json.dumps(

            r.json(),

            indent=4,

            ensure_ascii=False

        ))

        print("=" * 60)

        return r.json()


# ===========================================================

if __name__ == "__main__":

    client = PayPalServerClient()

    client.health()

    client.create_payment()

