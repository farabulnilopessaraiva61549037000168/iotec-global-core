from dataclasses import dataclass
from typing import List


@dataclass
class RevenueStartup:

    subsystem: str
    status: str = "PENDING"


class RevenueStartupEngine:

    def __init__(self):

        self.subsystems: List[RevenueStartup] = []

    def register(self, subsystem):

        self.subsystems.append(

            RevenueStartup(

                subsystem=subsystem

            )

        )

    def total(self):

        return len(self.subsystems)

    def pending(self):

        return len(

            [

                x

                for x in self.subsystems

                if x.status == "PENDING"

            ]

        )

    def running(self):

        return len(

            [

                x

                for x in self.subsystems

                if x.status == "RUNNING"

            ]

        )

    def ready(self):

        return len(

            [

                x

                for x in self.subsystems

                if x.status == "READY"

            ]

        )

    def failed(self):

        return len(

            [

                x

                for x in self.subsystems

                if x.status == "FAILED"

            ]

        )


if __name__ == "__main__":

    engine = RevenueStartupEngine()

    print("=" * 70)
    print("REVENUE STARTUP ENGINE")
    print("=" * 70)

    print("SUBSYSTEMS :", engine.total())
    print("PENDING    :", engine.pending())
    print("RUNNING    :", engine.running())
    print("READY      :", engine.ready())
    print("FAILED     :", engine.failed())

