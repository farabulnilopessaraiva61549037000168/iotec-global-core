from dataclasses import dataclass
from typing import List


@dataclass
class RevenuePayment:

    contract: str
    client: str
    method: str
    amount: float
    status: str = "WAITING"


class RevenuePaymentEngine:

    def __init__(self):

        self.payments: List[RevenuePayment] = []

    def register(self, contract, client, method, amount):

        self.payments.append(

            RevenuePayment(

                contract=contract,

                client=client,

                method=method,

                amount=amount

            )

        )

    def total(self):

        return len(self.payments)

    def waiting(self):

        return len(

            [

                x

                for x in self.payments

                if x.status == "WAITING"

            ]

        )

    def paid(self):

        return len(

            [

                x

                for x in self.payments

                if x.status == "PAID"

            ]

        )

    def cancelled(self):

        return len(

            [

                x

                for x in self.payments

                if x.status == "CANCELLED"

            ]

        )

    def total_value(self):

        return sum(

            x.amount

            for x in self.payments

        )


if __name__ == "__main__":

    engine = RevenuePaymentEngine()

    print("=" * 70)
    print("REVENUE PAYMENT ENGINE")
    print("=" * 70)

    print("PAYMENTS   :", engine.total())
    print("WAITING    :", engine.waiting())
    print("PAID       :", engine.paid())
    print("CANCELLED  :", engine.cancelled())
    print("VALUE      :", engine.total_value())

