import json
from pathlib import Path
from datetime import datetime

CONFIG_FILE = Path(r"C:\IOTEC\gateway_config.json")


class GatewayConfigurationEngine:

    def __init__(self):

        self.config = {

            "version": "1.0",

            "updated_at": datetime.now().isoformat(),

            "active_gateway": "PAYPAL",

            "environment": "SANDBOX",

            "gateways": {

                "PAYPAL": {

                    "enabled": True,

                    "client_id": "",

                    "client_secret": "",

                    "base_url": "https://api-m.sandbox.paypal.com",

                    "payment_url": "https://www.sandbox.paypal.com"

                },

                "MERCADOPAGO": {

                    "enabled": False,

                    "access_token": "",

                    "base_url": "https://api.mercadopago.com"

                },

                "ASAAS": {

                    "enabled": False,

                    "api_key": "",

                    "base_url": "https://api.asaas.com"

                },

                "PICPAY": {

                    "enabled": False,

                    "token": "",

                    "base_url": "https://appws.picpay.com"

                }

            }

        }

    # ------------------------------------------------------

    def load(self):

        if CONFIG_FILE.exists():

            with open(CONFIG_FILE, "r", encoding="utf-8") as f:

                self.config = json.load(f)

        return self.config

    # ------------------------------------------------------

    def save(self):

        self.config["updated_at"] = datetime.now().isoformat()

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:

            json.dump(

                self.config,

                f,

                indent=4,

                ensure_ascii=False

            )

    # ------------------------------------------------------

    def set_gateway(self, gateway):

        gateway = gateway.upper()

        if gateway not in self.config["gateways"]:

            raise Exception("Gateway inexistente.")

        self.config["active_gateway"] = gateway

        self.save()

    # ------------------------------------------------------

    def show(self):

        print()

        print("===================================================")
        print("GATEWAY CONFIGURATION ENGINE")
        print("===================================================")

        print(f"Gateway Ativo : {self.config['active_gateway']}")
        print(f"Ambiente      : {self.config['environment']}")

        print()

        for nome, dados in self.config["gateways"].items():

            status = "ATIVO" if dados["enabled"] else "DESLIGADO"

            print(f"{nome:15} {status}")

        print("===================================================")


# ==========================================================

if __name__ == "__main__":

    engine = GatewayConfigurationEngine()

    engine.save()

    engine.load()

    engine.show()

