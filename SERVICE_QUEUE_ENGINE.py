from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ServiceQueue:

    company: str
    service: str
    source: str
    status: str
    created_at: str


class ServiceQueueEngine:

    def __init__(self):

        self.queue: List[ServiceQueue] = []

    def add(self, company, service, source):

        self.queue.append(

            ServiceQueue(

                company=company,

                service=service,

                source=source,

                status="NEW",

                created_at=datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            )

        )

    def total(self):

        return len(self.queue)

    def new(self):

        return len(

            [

                x

                for x in self.queue

                if x.status == "NEW"

            ]

        )

    def processing(self):

        return len(

            [

                x

                for x in self.queue

                if x.status == "PROCESSING"

            ]

        )

    def completed(self):

        return len(

            [

                x

                for x in self.queue

                if x.status == "COMPLETED"

            ]

        )


if __name__ == "__main__":

    engine = ServiceQueueEngine()

    print("=" * 70)
    print("SERVICE QUEUE ENGINE")
    print("=" * 70)

    print("TOTAL       :", engine.total())
    print("NEW         :", engine.new())
    print("PROCESSING  :", engine.processing())
    print("COMPLETED   :", engine.completed())

