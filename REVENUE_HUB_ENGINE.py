from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RevenueHub:

    name: str

    engine: Any

    enabled: bool = True


class RevenueHubEngine:

    def __init__(self):

        self.engines: Dict[str, RevenueHub] = {}

    def register(self, name, engine):

        self.engines[name] = RevenueHub(

            name=name,

            engine=engine

        )

    def unregister(self, name):

        if name in self.engines:

            del self.engines[name]

    def exists(self, name):

        return name in self.engines

    def total(self):

        return len(self.engines)

    def enabled(self):

        return len(

            [

                x

                for x in self.engines.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.engines.values()

                if not x.enabled

            ]

        )

    def list(self):

        return sorted(

            self.engines.keys()

        )


if __name__ == "__main__":

    hub = RevenueHubEngine()

    print("=" * 70)

    print("REVENUE HUB ENGINE")

    print("=" * 70)

    print("ENGINES   :", hub.total())

    print("ENABLED   :", hub.enabled())

    print("DISABLED  :", hub.disabled())

