from dataclasses import dataclass
from typing import List


@dataclass
class RevenueContract:

    company: str
    service: str
    value: float
    status: str = "DRAFT"


class RevenueContractEngine:

    def __init__(self):

        self.contracts: List[RevenueContract] = []

    def register(self, company, service, value):

        self.contracts.append(

            RevenueContract(

                company=company,

                service=service,

                value=value

            )

        )

    def total(self):

        return len(self.contracts)

    def draft(self):

        return len(

            [

                x

                for x in self.contracts

                if x.status == "DRAFT"

            ]

        )

    def signed(self):

        return len(

            [

                x

                for x in self.contracts

                if x.status == "SIGNED"

            ]

        )

    def finished(self):

        return len(

            [

                x

                for x in self.contracts

                if x.status == "FINISHED"

            ]

        )

    def total_value(self):

        return sum(

            x.value

            for x in self.contracts

        )


if __name__ == "__main__":

    engine = RevenueContractEngine()

    print("=" * 70)
    print("REVENUE CONTRACT ENGINE")
    print("=" * 70)

    print("CONTRACTS  :", engine.total())
    print("DRAFT      :", engine.draft())
    print("SIGNED     :", engine.signed())
    print("FINISHED   :", engine.finished())
    print("VALUE      :", engine.total_value())

