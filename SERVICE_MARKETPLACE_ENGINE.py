from dataclasses import dataclass
from typing import List


@dataclass
class ServiceMarketplace:

    service: str
    marketplace: str
    country: str
    active: bool = True


class ServiceMarketplaceEngine:

    def __init__(self):

        self.marketplaces: List[ServiceMarketplace] = []

    def register(self, service, marketplace, country):

        self.marketplaces.append(

            ServiceMarketplace(

                service=service,

                marketplace=marketplace,

                country=country

            )

        )

    def total(self):

        return len(self.marketplaces)

    def active(self):

        return len(

            [

                x

                for x in self.marketplaces

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.marketplaces

                if not x.active

            ]

        )

    def countries(self):

        return len(

            {

                x.country

                for x in self.marketplaces

            }

        )

    def marketplaces_count(self):

        return len(

            {

                x.marketplace

                for x in self.marketplaces

            }

        )


if __name__ == "__main__":

    engine = ServiceMarketplaceEngine()

    print("=" * 70)
    print("SERVICE MARKETPLACE ENGINE")
    print("=" * 70)

    print("MARKETPLACES :", engine.marketplaces_count())
    print("SERVICES     :", engine.total())
    print("COUNTRIES    :", engine.countries())
    print("ACTIVE       :", engine.active())
    print("INACTIVE     :", engine.inactive())

