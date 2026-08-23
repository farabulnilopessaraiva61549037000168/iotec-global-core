from dataclasses import dataclass
from typing import List


@dataclass
class ServiceProvider:

    name: str
    capability: str
    country: str
    enabled: bool = True


class ServiceProviderEngine:

    def __init__(self):

        self.providers: List[ServiceProvider] = []

    def register(self, name, capability, country):

        self.providers.append(

            ServiceProvider(

                name=name,

                capability=capability,

                country=country

            )

        )

    def total(self):

        return len(self.providers)

    def enabled(self):

        return len(

            [

                x

                for x in self.providers

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.providers

                if not x.enabled

            ]

        )

    def countries(self):

        return len(

            {

                x.country

                for x in self.providers

            }

        )

    def capabilities(self):

        return len(

            {

                x.capability

                for x in self.providers

            }

        )


if __name__ == "__main__":

    engine = ServiceProviderEngine()

    print("=" * 70)
    print("SERVICE PROVIDER ENGINE")
    print("=" * 70)

    print("PROVIDERS   :", engine.total())
    print("COUNTRIES   :", engine.countries())
    print("CAPABILITIES:", engine.capabilities())
    print("ENABLED     :", engine.enabled())
    print("DISABLED    :", engine.disabled())

