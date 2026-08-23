from dataclasses import dataclass
from typing import List


@dataclass
class RevenueLifecycle:

    stage: str
    completed: bool = False


class RevenueLifecycleEngine:

    def __init__(self):

        self.stages: List[RevenueLifecycle] = []

    def register(self, stage):

        self.stages.append(

            RevenueLifecycle(

                stage=stage

            )

        )

    def total(self):

        return len(self.stages)

    def completed(self):

        return len(

            [

                x

                for x in self.stages

                if x.completed

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.stages

                if not x.completed

            ]

        )

    def completion_rate(self):

        if not self.stages:

            return 0.0

        return (

            self.completed()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueLifecycleEngine()

    print("=" * 70)
    print("REVENUE LIFECYCLE ENGINE")
    print("=" * 70)

    print("STAGES          :", engine.total())
    print("COMPLETED       :", engine.completed())
    print("PENDING         :", engine.pending())
    print("COMPLETION (%)  :", f"{engine.completion_rate():.2f}")

