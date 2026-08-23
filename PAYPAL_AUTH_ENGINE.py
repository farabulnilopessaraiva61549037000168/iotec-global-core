import json
import base64
import requests


class PayPalAuthEngine:

    def __init__(self):

        with open("paypal_credentials.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)

        self.environment = cfg["environment"]

        if self.environment == "LIVE":

            self.client_id = cfg["live"]["client_id"]
            self.client_secret = cfg["live"]["client_secret"]

            self.base_url = "https://api-m.paypal.com"

        else:

            self.client_id = cfg["sandbox"]["client_id"]
            self.client_secret = cfg["sandbox"]["client_secret"]

            self.base_url = "https://api-m.sandbox.paypal.com"

    # ---------------------------------------------------

    def get_token(self):

        auth = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()

        headers = {
            "Authorization": f"Basic {auth}"
        }

        data = {
            "grant_type": "client_credentials"
        }

        r = requests.post(

            self.base_url + "/v1/oauth2/token",

            headers=headers,

            data=data,

            timeout=30

        )

        r.raise_for_status()

        token = r.json()["access_token"]

        print()

        print("=" * 60)
        print("PAYPAL AUTH ENGINE")
        print("=" * 60)
        print("Ambiente :", self.environment)
        print("Token obtido com sucesso.")
        print("=" * 60)

        return token


if __name__ == "__main__":

    PayPalAuthEngine().get_token()

