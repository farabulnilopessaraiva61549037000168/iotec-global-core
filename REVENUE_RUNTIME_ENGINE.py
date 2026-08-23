from dataclasses import dataclass
from typing import List


@dataclass
class RevenueRuntime:

    process: str
    status: str = "STOPPED"


class RevenueRuntimeEngine:

    def __init__(self):

        self.processes: List[RevenueRuntime] = []

    def register(self, process):

        self.processes.append(

            RevenueRuntime(

                process=process

            )

        )

    def total(self):

        return len(self.processes)

    def stopped(self):

        return len(

            [

                x

                for x in self.processes

                if x.status == "STOPPED"

            ]

        )

    def running(self):

        return len(

            [

                x

                for x in self.processes

                if x.status == "RUNNING"

            ]

        )

    def paused(self):

        return len(

            [

                x

                for x in self.processes

                if x.status == "PAUSED"

            ]

        )

    def failed(self):

        return len(

            [

                x

                for x in self.processes

                if x.status == "FAILED"

            ]

        )


if __name__ == "__main__":

    engine = RevenueRuntimeEngine()

    print("=" * 70)
    print("REVENUE RUNTIME ENGINE")
    print("=" * 70)

    print("PROCESSES :", engine.total())
    print("STOPPED   :", engine.stopped())
    print("RUNNING   :", engine.running())
    print("PAUSED    :", engine.paused())
    print("FAILED    :", engine.failed())

