import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC GATEWAY DISCOVERY
# Descoberta automÃƒÂ¡tica de gateways de pagamento
# ==========================================================

from pathlib import Path

ROOT = Path("C:/IOTEC")

CATALOG = {
    "PAYPAL": [
        "paypal",
        "payment",
        "confirm_payment",
        "checkout"
    ],

    "PICPAY": [
        "picpay"
    ],

    "PIX": [
        "pix"
    ],

    "MERCADOPAGO": [
        "mercado",
        "mercadopago"
    ],

    "PAGSEGURO": [
        "pagseguro"
    ],

    "STRIPE": [
        "stripe"
    ],

    "WEBHOOK": [
        "webhook"
    ]
}


class GatewayDiscovery:

    def __init__(self):

        self.result = {}

    # --------------------------------------------------

    def scan(self):

        print()
        print("=" * 70)
        print("IOTEC GATEWAY DISCOVERY")
        print("=" * 70)

        files = list(ROOT.rglob("*"))

        for gateway in CATALOG:

            self.result[gateway] = []

        for file in files:

            if not file.is_file():
                continue

            name = file.name.lower()

            for gateway, words in CATALOG.items():

                for word in words:

                    if word in name:

                        self.result[gateway].append(file)

                        break

        print()

    # --------------------------------------------------

    def report(self):

        best_gateway = None
        best_score = -1

        for gateway in self.result:

            print("=" * 70)
            print(gateway)
            print("=" * 70)

            files = self.result[gateway]

            print("Componentes :", len(files))
            print()

            for item in files[:10]:

                print(item)

            print()

            if len(files) > best_score:

                best_score = len(files)
                best_gateway = gateway

        print("=" * 70)
        print("GATEWAY RECOMENDADO")
        print("=" * 70)
        print()

        if best_gateway:

            print(best_gateway)
            print()
            print("Score :", best_score)

        else:

            print("Nenhum gateway encontrado.")

        print()
        print("=" * 70)
        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")
        print("=" * 70)
        print()
        print("GERAR CHECKOUT")
        print("CRIAR LINK")
        print("VALIDAR PAGAMENTO")
        print()

    # --------------------------------------------------

    def run(self):

        self.scan()

        self.report()


# ==========================================================

if __name__ == "__main__":

    GatewayDiscovery().run()



