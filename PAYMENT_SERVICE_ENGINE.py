import requests


class PaymentServiceEngine:

    def __init__(self):

        self.server = "http://127.0.0.1:5001"

    # ----------------------------------------------------

    def create_payment(self):

        response = requests.get(

            self.server + "/criar-pagamento",

            timeout=60

        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------------------------

    def health(self):

        response = requests.get(

            self.server + "/health",

            timeout=10

        )

        response.raise_for_status()

        return response.json()


# ======================================================

if __name__ == "__main__":

    service = PaymentServiceEngine()

    print(service.health())

    payment = service.create_payment()

    print()

    print("=" * 60)

    print("PAGAMENTO GERADO")

    print("=" * 60)

    print(payment)

    print("=" * 60)

