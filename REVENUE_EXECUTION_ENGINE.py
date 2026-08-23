from dataclasses import dataclass
from typing import List


@dataclass
class RevenueExecution:

    service: str
    client: str
    source: str
    status: str = "PENDING"


class RevenueExecutionEngine:

    def __init__(self):

        self.executions: List[RevenueExecution] = []

    def register(self, service, client, source):

        self.executions.append(

            RevenueExecution(

                service=service,

                client=client,

                source=source

            )

        )

    def total(self):

        return len(self.executions)

    def pending(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "PENDING"

            ]

        )

    def running(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "RUNNING"

            ]

        )

    def finished(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "FINISHED"

            ]

        )

    def sources(self):

        return len(

            {

                x.source

                for x in self.executions

            }

        )


if __name__ == "__main__":

    engine = RevenueExecutionEngine()

    print("=" * 70)
    print("REVENUE EXECUTION ENGINE")
    print("=" * 70)

    print("EXECUTIONS :", engine.total())
    print("PENDING    :", engine.pending())
    print("RUNNING    :", engine.running())
    print("FINISHED   :", engine.finished())
    print("SOURCES    :", engine.sources())

