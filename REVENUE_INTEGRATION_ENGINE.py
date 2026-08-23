from dataclasses import dataclass
from typing import Dict, Callable, Any


@dataclass
class RevenueIntegration:

    name: str
    connector: Callable[..., Any]
    enabled: bool = True


class RevenueIntegrationEngine:

    def __init__(self):

        self.integrations: Dict[str, RevenueIntegration] = {}

    def register(self, name, connector):

        self.integrations[name] = RevenueIntegration(

            name=name,

            connector=connector

        )

    def unregister(self, name):

        self.integrations.pop(name, None)

    def exists(self, name):

        return name in self.integrations

    def total(self):

        return len(self.integrations)

    def enabled(self):

        return len(

            [

                x

                for x in self.integrations.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.integrations.values()

                if not x.enabled

            ]

        )

    def names(self):

        return sorted(

            self.integrations.keys()

        )


if __name__ == "__main__":

    integration = RevenueIntegrationEngine()

    print("=" * 70)

    print("REVENUE INTEGRATION ENGINE")

    print("=" * 70)

    print("INTEGRATIONS :", integration.total())

    print("ENABLED      :", integration.enabled())

    print("DISABLED     :", integration.disabled())

