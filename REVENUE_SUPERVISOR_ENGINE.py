from dataclasses import dataclass
from typing import List


@dataclass
class RevenueSupervisor:

    module: str
    status: str = "IDLE"


class RevenueSupervisorEngine:

    def __init__(self):

        self.modules: List[RevenueSupervisor] = []

    def register(self, module):

        self.modules.append(

            RevenueSupervisor(

                module=module

            )

        )

    def total(self):

        return len(self.modules)

    def idle(self):

        return len(

            [

                x

                for x in self.modules

                if x.status == "IDLE"

            ]

        )

    def running(self):

        return len(

            [

                x

                for x in self.modules

                if x.status == "RUNNING"

            ]

        )

    def paused(self):

        return len(

            [

                x

                for x in self.modules

                if x.status == "PAUSED"

            ]

        )

    def stopped(self):

        return len(

            [

                x

                for x in self.modules

                if x.status == "STOPPED"

            ]

        )


if __name__ == "__main__":

    engine = RevenueSupervisorEngine()

    print("=" * 70)
    print("REVENUE SUPERVISOR ENGINE")
    print("=" * 70)

    print("MODULES   :", engine.total())
    print("IDLE      :", engine.idle())
    print("RUNNING   :", engine.running())
    print("PAUSED    :", engine.paused())
    print("STOPPED   :", engine.stopped())

