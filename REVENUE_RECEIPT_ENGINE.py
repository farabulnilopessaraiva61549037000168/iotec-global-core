from dataclasses import dataclass
from typing import List


@dataclass
class RevenueReceipt:

    payment_id: str
    client: str
    amount: float
    delivered: bool = False


class RevenueReceiptEngine:

    def __init__(self):

        self.receipts: List[RevenueReceipt] = []

    def register(self, payment_id, client, amount):

        self.receipts.append(

            RevenueReceipt(

                payment_id=payment_id,

                client=client,

                amount=amount

            )

        )

    def total(self):

        return len(self.receipts)

    def delivered(self):

        return len(

            [

                x

                for x in self.receipts

                if x.delivered

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.receipts

                if not x.delivered

            ]

        )

    def total_value(self):

        return sum(

            x.amount

            for x in self.receipts

        )


if __name__ == "__main__":

    engine = RevenueReceiptEngine()

    print("=" * 70)
    print("REVENUE RECEIPT ENGINE")
    print("=" * 70)

    print("RECEIPTS   :", engine.total())
    print("DELIVERED  :", engine.delivered())
    print("PENDING    :", engine.pending())
    print("VALUE      :", engine.total_value())

