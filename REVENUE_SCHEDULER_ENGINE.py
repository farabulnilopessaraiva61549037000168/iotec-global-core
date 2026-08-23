from dataclasses import dataclass
from typing import List


@dataclass
class RevenueScheduler:

    task: str
    interval: str
    status: str = "SCHEDULED"


class RevenueSchedulerEngine:

    def __init__(self):

        self.tasks: List[RevenueScheduler] = []

    def register(self, task, interval):

        self.tasks.append(

            RevenueScheduler(

                task=task,

                interval=interval

            )

        )

    def total(self):

        return len(self.tasks)

    def scheduled(self):

        return len(

            [

                x

                for x in self.tasks

                if x.status == "SCHEDULED"

            ]

        )

    def running(self):

        return len(

            [

                x

                for x in self.tasks

                if x.status == "RUNNING"

            ]

        )

    def completed(self):

        return len(

            [

                x

                for x in self.tasks

                if x.status == "COMPLETED"

            ]

        )

    def failed(self):

        return len(

            [

                x

                for x in self.tasks

                if x.status == "FAILED"

            ]

        )


if __name__ == "__main__":

    engine = RevenueSchedulerEngine()

    print("=" * 70)
    print("REVENUE SCHEDULER ENGINE")
    print("=" * 70)

    print("TASKS      :", engine.total())
    print("SCHEDULED  :", engine.scheduled())
    print("RUNNING    :", engine.running())
    print("COMPLETED  :", engine.completed())
    print("FAILED     :", engine.failed())

