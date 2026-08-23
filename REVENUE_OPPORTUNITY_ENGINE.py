from dataclasses import dataclass
from typing import List


@dataclass
class RevenueOpportunity:

    title: str
    organization: str
    country: str
    source: str
    priority: int
    status: str = "DISCOVERED"


class RevenueOpportunityEngine:

    def __init__(self):

        self.opportunities: List[RevenueOpportunity] = []

    def register(
        self,
        title,
        organization,
        country,
        source,
        priority
    ):

        self.opportunities.append(

            RevenueOpportunity(

                title=title,

                organization=organization,

                country=country,

                source=source,

                priority=priority

            )

        )

    def total(self):

        return len(self.opportunities)

    def discovered(self):

        return len(

            [

                x

                for x in self.opportunities

                if x.status == "DISCOVERED"

            ]

        )

    def processing(self):

        return len(

            [

                x

                for x in self.opportunities

                if x.status == "PROCESSING"

            ]

        )

    def completed(self):

        return len(

            [

                x

                for x in self.opportunities

                if x.status == "COMPLETED"

            ]

        )

    def countries(self):

        return len(

            {

                x.country

                for x in self.opportunities

            }

        )

    def sources(self):

        return len(

            {

                x.source

                for x in self.opportunities

            }

        )


if __name__ == "__main__":

    engine = RevenueOpportunityEngine()

    print("=" * 70)
    print("REVENUE OPPORTUNITY ENGINE")
    print("=" * 70)

    print("OPPORTUNITIES :", engine.total())
    print("DISCOVERED    :", engine.discovered())
    print("PROCESSING    :", engine.processing())
    print("COMPLETED     :", engine.completed())
    print("COUNTRIES     :", engine.countries())
    print("SOURCES       :", engine.sources())

