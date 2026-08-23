from dataclasses import dataclass
from typing import List


@dataclass
class RevenueSettlement:

    receipt_id: str
    client: str
    amount: float
    settled: bool = False


class RevenueSettlementEngine:

    def __init__(self):

        self.settlements: List[RevenueSettlement] = []

    def register(self, receipt_id, client, amount):

        self.settlements.append(

            RevenueSettlement(

                receipt_id=receipt_id,

                client=client,

                amount=amount

            )

        )

    def total(self):

        return len(self.settlements)

    def settled(self):

        return len(

            [

                x

                for x in self.settlements

                if x.settled

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.settlements

                if not x.settled

            ]

        )

    def total_value(self):

        return sum(

            x.amount

            for x in self.settlements

        )


if __name__ == "__main__":

    engine = RevenueSettlementEngine()

    print("=" * 70)
    print("REVENUE SETTLEMENT ENGINE")
    print("=" * 70)

    print("SETTLEMENTS :", engine.total())
    print("SETTLED     :", engine.settled())
    print("PENDING     :", engine.pending())
    print("VALUE       :", engine.total_value())

