from dataclasses import dataclass
from typing import List


@dataclass
class RevenueProjection:

    market: str
    opportunity: str
    estimated_value: float
    probability: float
    active: bool = True


class RevenueProjectionEngine:

    def __init__(self):

        self.projections: List[RevenueProjection] = []

    def register(self, market, opportunity, estimated_value, probability):

        self.projections.append(

            RevenueProjection(

                market=market,

                opportunity=opportunity,

                estimated_value=estimated_value,

                probability=probability

            )

        )

    def total(self):

        return len(self.projections)

    def active(self):

        return len(

            [

                x

                for x in self.projections

                if x.active

            ]

        )

    def expected_revenue(self):

        return sum(

            x.estimated_value * x.probability

            for x in self.projections

        )

    def markets(self):

        return len(

            {

                x.market

                for x in self.projections

            }

        )


if __name__ == "__main__":

    engine = RevenueProjectionEngine()

    print("=" * 70)
    print("REVENUE PROJECTION ENGINE")
    print("=" * 70)

    print("PROJECTIONS      :", engine.total())
    print("ACTIVE           :", engine.active())
    print("MARKETS          :", engine.markets())
    print("EXPECTED REVENUE :", engine.expected_revenue())

