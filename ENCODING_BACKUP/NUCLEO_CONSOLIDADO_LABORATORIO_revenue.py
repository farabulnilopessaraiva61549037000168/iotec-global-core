import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime


class RevenueEngine:
    pass

    def __init__(self):
        pass

        self.monthly_revenue = 0.0

        self.total_sales = 0

        self.clients = []

        self.sales_history = []

    def register_client(
        self,
        client
    ):

        self.clients.append(client)

        print("\n[CLIENT]")

        print(
            f"CLIENT REGISTERED: "
            f"{client}"
        )

    def register_sale(
        self,
        client,
        product,
        amount
    ):

        self.monthly_revenue += amount

        self.total_sales += 1

        sale = {

            "client": client,

            "product": product,

            "amount": amount,

            "time": str(datetime.now())
        }

        self.sales_history.append(sale)

        print("\n[SALE]")

        print(f"CLIENT: {client}")

        print(f"PRODUCT: {product}")

        print(
            f"VALUE: ${amount:.2f}"
        )

    def report(self):
        pass

        print(
            "\n========== REVENUE REPORT =========="
        )

        print(
            f"TOTAL CLIENTS: "
            f"{len(self.clients)}"
        )

        print(
            f"TOTAL SALES: "
            f"{self.total_sales}"
        )

        print(
            f"MONTHLY REVENUE: "
            f"${self.monthly_revenue:.2f}"
        )

    def sales_history_report(self):
        pass

        print(
            "\n========== SALES HISTORY =========="
        )

        for sale in self.sales_history:
            pass

            print(
                f"{sale['client']} -> "
                f"{sale['product']} | "
                f"${sale['amount']:.2f}"
            )


