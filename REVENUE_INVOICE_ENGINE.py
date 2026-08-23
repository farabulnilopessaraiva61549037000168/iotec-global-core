from dataclasses import dataclass
from typing import List


@dataclass
class RevenueInvoice:

    payment: str
    client: str
    amount: float
    issued: bool = False


class RevenueInvoiceEngine:

    def __init__(self):

        self.invoices: List[RevenueInvoice] = []

    def register(self, payment, client, amount):

        self.invoices.append(

            RevenueInvoice(

                payment=payment,

                client=client,

                amount=amount

            )

        )

    def total(self):

        return len(self.invoices)

    def issued(self):

        return len(

            [

                x

                for x in self.invoices

                if x.issued

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.invoices

                if not x.issued

            ]

        )

    def total_value(self):

        return sum(

            x.amount

            for x in self.invoices

        )


if __name__ == "__main__":

    engine = RevenueInvoiceEngine()

    print("=" * 70)
    print("REVENUE INVOICE ENGINE")
    print("=" * 70)

    print("INVOICES   :", engine.total())
    print("ISSUED     :", engine.issued())
    print("PENDING    :", engine.pending())
    print("VALUE      :", engine.total_value())

