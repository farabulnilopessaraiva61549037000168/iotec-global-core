import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC GATEWAY VALIDATOR
# ==========================================================

from pathlib import Path
import re

GATEWAY = Path(r"C:\IOTEC\paypal_server.py")


class GatewayValidator:

    def __init__(self):

        self.text = ""

        self.score = 0

        self.report = []

    # ------------------------------------------------------

    def load(self):

        print()
        print("=" * 70)
        print("VALIDAÃƒâ€¡ÃƒÆ'O DO GATEWAY OFICIAL")
        print("=" * 70)

        if not GATEWAY.exists():

            print()
            print("ERRO")
            print("Gateway nÃƒÂ£o encontrado.")
            return False

        self.text = GATEWAY.read_text(
            encoding="utf8",
            errors="ignore"
        ).lower()

        return True

    # ------------------------------------------------------

    def check(self, title, patterns, points):

        ok = False

        for pattern in patterns:

            if re.search(pattern, self.text):

                ok = True
                break

        self.report.append((title, ok))

        if ok:

            self.score += points

    # ------------------------------------------------------

    def analyse(self):

        self.check(
            "Client ID",
            [r"client_id"],
            10
        )

        self.check(
            "Client Secret",
            [r"client_secret"],
            10
        )

        self.check(
            "OAuth",
            [r"oauth"],
            10
        )

        self.check(
            "Access Token",
            [r"access_token"],
            10
        )

        self.check(
            "Checkout",
            [r"checkout"],
            10
        )

        self.check(
            "Orders",
            [r"orders"],
            10
        )

        self.check(
            "Create Order",
            [
                r"create_order",
                r"create-order"
            ],
            20
        )

        self.check(
            "Capture Order",
            [
                r"capture_order",
                r"capture-order"
            ],
            20
        )

        self.check(
            "Webhook",
            [r"webhook"],
            10
        )

        self.check(
            "Flask Route",
            [
                r"@app.route",
                r"route\("
            ],
            10
        )

    # ------------------------------------------------------

    def show(self):

        print()

        print("=" * 70)
        print("RELATÃƒâ€œRIO")
        print("=" * 70)
        print()

        for title, ok in self.report:

            print(

                f"{title:<25}",

                "OK" if ok else "--"

            )

        print()

        print("=" * 70)

        print("SCORE")

        print("=" * 70)

        print()

        print(self.score)

        print("/120")

        print()

        print("=" * 70)

        if self.score >= 90:

            print("STATUS")

            print("PRONTO PARA GERAR CHECKOUT")

        elif self.score >= 60:

            print("STATUS")

            print("PRECISA DE PEQUENOS AJUSTES")

        else:

            print("STATUS")

            print("INCOMPLETO")

        print()

        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")

        print()

        print("GERAR CHECKOUT DE R$ 30,00")

    # ------------------------------------------------------

    def run(self):

        if not self.load():

            return

        self.analyse()

        self.show()


# ==========================================================

if __name__ == "__main__":

    GatewayValidator().run()



