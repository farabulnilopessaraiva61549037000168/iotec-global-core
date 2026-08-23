"""
=========================================================
IOTEC - CASHBOX ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Controla o caixa oficial da plataforma.
=========================================================
"""

from datetime import datetime


class CashboxEngine:

    def __init__(self):

        self.balance = 0.0
        self.transactions = []

    # --------------------------------------------------

    def deposit(
        self,
        description,
        amount,
        source
    ):

        amount = float(amount)

        self.balance += amount

        self.transactions.append({

            "date": datetime.now(),
            "type": "ENTRADA",
            "description": description,
            "source": source,
            "amount": amount,
            "balance": self.balance

        })

    # --------------------------------------------------

    def withdraw(
        self,
        description,
        amount,
        destination
    ):

        amount = float(amount)

        if amount > self.balance:

            print("Saldo insuficiente.")
            return

        self.balance -= amount

        self.transactions.append({

            "date": datetime.now(),
            "type": "SAÃƒÂDA",
            "description": description,
            "source": destination,
            "amount": amount,
            "balance": self.balance

        })

    # --------------------------------------------------

    def statement(self):

        print("\n==========================================")
        print("IOTEC CASHBOX")
        print("==========================================")

        if not self.transactions:
            print("Nenhuma movimentaÃƒÂ§ÃƒÂ£o.")

        for item in self.transactions:

            print(f"{item['date']}")
            print(f"Tipo      : {item['type']}")
            print(f"DescriÃƒÂ§ÃƒÂ£o : {item['description']}")
            print(f"Origem    : {item['source']}")
            print(f"Valor     : R$ {item['amount']:.2f}")
            print(f"Saldo     : R$ {item['balance']:.2f}")
            print("------------------------------------------")

        print(f"SALDO FINAL : R$ {self.balance:.2f}")
        print("==========================================\n")


# ======================================================

if __name__ == "__main__":

    cashbox = CashboxEngine()

    cashbox.deposit(

        description="HomologaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o",

        amount=29.90,

        source="PAYMENT_MONITOR_ENGINE"

    )

    cashbox.statement()


