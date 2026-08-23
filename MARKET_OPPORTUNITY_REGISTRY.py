from dataclasses import dataclass
from typing import List


@dataclass
class MarketOpportunity:

    sector: str
    country: str
    priority: int
    active: bool = True


class MarketOpportunityRegistry:

    def __init__(self):

        self.registry: List[MarketOpportunity] = []

    def register(self, sector, country, priority):

        self.registry.append(

            MarketOpportunity(

                sector=sector,

                country=country,

                priority=priority

            )

        )

    def total(self):

        return len(self.registry)

    def active(self):

        return len(

            [

                x

                for x in self.registry

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.registry

                if not x.active

            ]

        )

    def by_country(self, country):

        return [

            x

            for x in self.registry

            if x.country.lower() == country.lower()

        ]

    def by_sector(self, sector):

        return [

            x

            for x in self.registry

            if x.sector.lower() == sector.lower()

        ]


if __name__ == "__main__":

    engine = MarketOpportunityRegistry()

    print("=" * 70)
    print("MARKET OPPORTUNITY REGISTRY")
    print("=" * 70)

    print("TOTAL     :", engine.total())
    print("ACTIVE    :", engine.active())
    print("INACTIVE  :", engine.inactive())

