from dataclasses import dataclass
from typing import List


@dataclass
class ServiceExecution:

    service: str
    company: str
    status: str = "WAITING"


class ServiceExecutionEngine:

    def __init__(self):

        self.executions: List[ServiceExecution] = []

    def register(self, service, company):

        self.executions.append(

            ServiceExecution(

                service=service,

                company=company

            )

        )

    def total(self):

        return len(self.executions)

    def waiting(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "WAITING"

            ]

        )

    def processing(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "PROCESSING"

            ]

        )

    def completed(self):

        return len(

            [

                x

                for x in self.executions

                if x.status == "COMPLETED"

            ]

        )


if __name__ == "__main__":

    engine = ServiceExecutionEngine()

    print("=" * 70)
    print("SERVICE EXECUTION ENGINE")
    print("=" * 70)

    print("TOTAL      :", engine.total())
    print("WAITING    :", engine.waiting())
    print("PROCESSING :", engine.processing())
    print("COMPLETED  :", engine.completed())

