import requests
import json
import base64


class PayPalCallbackEngine:

    def __init__(self):

        # Reutilize as mesmas credenciais do seu paypal_server.py
        self.CLIENT_ID = ""
        self.CLIENT_SECRET = ""

        self.BASE_URL = "https://api-m.sandbox.paypal.com"

    # ----------------------------------------------------

    def get_access_token(self):

        auth = base64.b64encode(
            f"{self.CLIENT_ID}:{self.CLIENT_SECRET}".encode()
        ).decode()

        headers = {
            "Authorization": f"Basic {auth}"
        }

        data = {
            "grant_type": "client_credentials"
        }

        r = requests.post(
            self.BASE_URL + "/v1/oauth2/token",
            headers=headers,
            data=data,
            timeout=30
        )

        r.raise_for_status()

        return r.json()["access_token"]

    # ----------------------------------------------------

    def check_order(self, order_id):

        token = self.get_access_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        r = requests.get(
            self.BASE_URL + f"/v2/checkout/orders/{order_id}",
            headers=headers,
            timeout=30
        )

        r.raise_for_status()

        order = r.json()

        print()
        print("=" * 60)
        print("PAYPAL CALLBACK ENGINE")
        print("=" * 60)
        print(json.dumps(order, indent=4, ensure_ascii=False))
        print("=" * 60)

        return order


if __name__ == "__main__":

    order_id = input("ORDER ID: ").strip()

    engine = PayPalCallbackEngine()

    engine.check_order(order_id)

