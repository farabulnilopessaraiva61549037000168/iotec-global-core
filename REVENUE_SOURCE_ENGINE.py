from dataclasses import dataclass
from typing import List


@dataclass
class RevenueSource:

    name: str
    category: str
    recurring: bool
    active: bool = True


class RevenueSourceEngine:

    def __init__(self):

        self.sources: List[RevenueSource] = []

    def register(self, name, category, recurring=False):

        self.sources.append(

            RevenueSource(

                name=name,

                category=category,

                recurring=recurring

            )

        )

    def total(self):

        return len(self.sources)

    def recurring(self):

        return len(

            [

                x

                for x in self.sources

                if x.recurring

            ]

        )

    def one_time(self):

        return len(

            [

                x

                for x in self.sources

                if not x.recurring

            ]

        )

    def active(self):

        return len(

            [

                x

                for x in self.sources

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.sources

                if not x.active

            ]

        )


if __name__ == "__main__":

    engine = RevenueSourceEngine()

    print("=" * 70)
    print("REVENUE SOURCE ENGINE")
    print("=" * 70)

    print("SOURCES      :", engine.total())
    print("RECURRING    :", engine.recurring())
    print("ONE TIME     :", engine.one_time())
    print("ACTIVE       :", engine.active())
    print("INACTIVE     :", engine.inactive())

