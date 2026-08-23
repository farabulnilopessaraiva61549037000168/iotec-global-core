from dataclasses import dataclass
from typing import List


@dataclass
class RevenueHeartbeat:

    component: str
    state: str = "ALIVE"


class RevenueHeartbeatEngine:

    def __init__(self):

        self.components: List[RevenueHeartbeat] = []

    def register(self, component):

        self.components.append(

            RevenueHeartbeat(

                component=component

            )

        )

    def total(self):

        return len(self.components)

    def alive(self):

        return len(

            [

                x

                for x in self.components

                if x.state == "ALIVE"

            ]

        )

    def warning(self):

        return len(

            [

                x

                for x in self.components

                if x.state == "WARNING"

            ]

        )

    def failed(self):

        return len(

            [

                x

                for x in self.components

                if x.state == "FAILED"

            ]

        )

    def availability(self):

        if not self.components:

            return 100.0

        return (

            self.alive()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueHeartbeatEngine()

    print("=" * 70)
    print("REVENUE HEARTBEAT ENGINE")
    print("=" * 70)

    print("COMPONENTS     :", engine.total())
    print("ALIVE          :", engine.alive())
    print("WARNING        :", engine.warning())
    print("FAILED         :", engine.failed())
    print("AVAILABILITY % :", f"{engine.availability():.2f}")

