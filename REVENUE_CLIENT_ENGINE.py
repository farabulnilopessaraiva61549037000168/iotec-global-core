from dataclasses import dataclass
from typing import List


@dataclass
class RevenueClient:

    company: str
    country: str
    layer: int
    status: str = "PROSPECT"


class RevenueClientEngine:

    def __init__(self):

        self.clients: List[RevenueClient] = []

    def register(self, company, country, layer):

        self.clients.append(

            RevenueClient(

                company=company,

                country=country,

                layer=layer

            )

        )

    def total(self):

        return len(self.clients)

    def prospects(self):

        return len(

            [

                x

                for x in self.clients

                if x.status == "PROSPECT"

            ]

        )

    def active(self):

        return len(

            [

                x

                for x in self.clients

                if x.status == "ACTIVE"

            ]

        )

    def countries(self):

        return len(

            {

                x.country

                for x in self.clients

            }

        )

    def layers(self):

        return len(

            {

                x.layer

                for x in self.clients

            }

        )


if __name__ == "__main__":

    engine = RevenueClientEngine()

    print("=" * 70)
    print("REVENUE CLIENT ENGINE")
    print("=" * 70)

    print("CLIENTS    :", engine.total())
    print("PROSPECTS  :", engine.prospects())
    print("ACTIVE     :", engine.active())
    print("COUNTRIES  :", engine.countries())
    print("LAYERS     :", engine.layers())

