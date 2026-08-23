from dataclasses import dataclass
from typing import List


@dataclass
class RevenueHealth:

    component: str
    status: str = "READY"


class RevenueHealthEngine:

    def __init__(self):

        self.components: List[RevenueHealth] = []

    def register(self, component):

        self.components.append(

            RevenueHealth(

                component=component

            )

        )

    def total(self):

        return len(self.components)

    def ready(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "READY"

            ]

        )

    def warning(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "WARNING"

            ]

        )

    def error(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "ERROR"

            ]

        )

    def health(self):

        if not self.components:

            return 100.0

        return (

            self.ready()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueHealthEngine()

    print("=" * 70)
    print("REVENUE HEALTH ENGINE")
    print("=" * 70)

    print("COMPONENTS :", engine.total())
    print("READY      :", engine.ready())
    print("WARNING    :", engine.warning())
    print("ERROR      :", engine.error())
    print("HEALTH (%) :", f"{engine.health():.2f}")

