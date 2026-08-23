import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC FIRST SALE ORCHESTRATOR
# ==========================================================

import requests
import webbrowser
import json
from datetime import datetime

SERVER = "http://127.0.0.1:5001"

class FirstSaleOrchestrator:

    def __init__(self):

        self.order = None

    # ------------------------------------------------------

    def banner(self):

        print()
        print("="*70)
        print("IOTEC FIRST SALE ORCHESTRATOR")
        print("="*70)
        print()

    # ------------------------------------------------------

    def health(self):

        print("Verificando servidor...")

        r = requests.get(f"{SERVER}/health", timeout=10)

        if r.status_code != 200:

            raise Exception("Servidor indisponÃƒÂ­vel.")

        print("Servidor OK")

    # ------------------------------------------------------

    def create_payment(self):

        print()

        print("Solicitando criaÃƒÂ§ÃƒÂ£o da ordem...")

        r = requests.get(
            f"{SERVER}/criar-pagamento",
            timeout=30
        )

        if r.status_code != 200:

            raise Exception("Falha ao criar pagamento.")

        self.order = r.json()

        print("Ordem criada.")

        print()

        print("Order ID")

        print(self.order["order_id"])

        print()

        print("Checkout")

        print(self.order["url"])

    # ------------------------------------------------------

    def open_browser(self):

        print()

        print("Abrindo checkout...")

        webbrowser.open(self.order["url"])

    # ------------------------------------------------------

    def save_log(self):

        log = {

            "timestamp": datetime.now().isoformat(),

            "status":"ORDER_CREATED",

            "order":self.order

        }

        with open(

            "FIRST_SALE_LOG.json",

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                log,

                f,

                indent=4,

                ensure_ascii=False

            )

        print()

        print("Log salvo.")

    # ------------------------------------------------------

    def tower(self):

        print()

        print("="*70)

        print("TORRE DE CONTROLE")

        print("="*70)

        print()

        print("MISSÃƒÆ'O")

        print("Primeira Venda")

        print()

        print("STATUS")

        print("Checkout criado")

        print()

        print("AGUARDANDO PAGAMENTO")

        print()

    # ------------------------------------------------------

    def run(self):

        self.banner()

        self.health()

        self.create_payment()

        self.save_log()

        self.open_browser()

        self.tower()


# ==========================================================

if __name__=="__main__":

    FirstSaleOrchestrator().run()



