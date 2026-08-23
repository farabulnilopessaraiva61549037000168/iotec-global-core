from dataclasses import dataclass
from typing import List


@dataclass
class RevenueMarket:

    name: str
    country: str
    layer: int
    active: bool = True


class RevenueMarketEngine:

    def __init__(self):

        self.markets: List[RevenueMarket] = []

    def register(self, name, country, layer):

        self.markets.append(

            RevenueMarket(

                name=name,

                country=country,

                layer=layer

            )

        )

    def total(self):

        return len(self.markets)

    def active(self):

        return len(

            [

                x

                for x in self.markets

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.markets

                if not x.active

            ]

        )

    def countries(self):

        return len(

            {

                x.country

                for x in self.markets

            }

        )

    def layers(self):

        return len(

            {

                x.layer

                for x in self.markets

            }

        )


if __name__ == "__main__":

    engine = RevenueMarketEngine()

    print("=" * 70)
    print("REVENUE MARKET ENGINE")
    print("=" * 70)

    print("MARKETS   :", engine.total())
    print("COUNTRIES :", engine.countries())
    print("LAYERS    :", engine.layers())
    print("ACTIVE    :", engine.active())
    print("INACTIVE  :", engine.inactive())

