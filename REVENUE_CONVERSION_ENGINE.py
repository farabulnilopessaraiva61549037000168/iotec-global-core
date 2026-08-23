from dataclasses import dataclass
from typing import List


@dataclass
class RevenueConversion:

    lead: str
    proposal: bool = False
    contract: bool = False
    payment: bool = False


class RevenueConversionEngine:

    def __init__(self):

        self.items: List[RevenueConversion] = []

    def register(self, lead):

        self.items.append(
            RevenueConversion(
                lead=lead
            )
        )

    def total(self):

        return len(self.items)

    def proposals(self):

        return len(
            [
                x
                for x in self.items
                if x.proposal
            ]
        )

    def contracts(self):

        return len(
            [
                x
                for x in self.items
                if x.contract
            ]
        )

    def payments(self):

        return len(
            [
                x
                for x in self.items
                if x.payment
            ]
        )

    def conversion_rate(self):

        if not self.items:
            return 0.0

        return (
            self.payments()
            / self.total()
        ) * 100


if __name__ == "__main__":

    engine = RevenueConversionEngine()

    print("=" * 70)
    print("REVENUE CONVERSION ENGINE")
    print("=" * 70)

    print("LEADS           :", engine.total())
    print("PROPOSALS       :", engine.proposals())
    print("CONTRACTS       :", engine.contracts())
    print("PAYMENTS        :", engine.payments())
    print("CONVERSION (%)  :", f"{engine.conversion_rate():.2f}")

