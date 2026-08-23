from dataclasses import dataclass
from typing import List


@dataclass
class RevenueOrchestrator:

    engine: str
    enabled: bool = True


class RevenueOrchestratorEngine:

    def __init__(self):

        self.engines: List[RevenueOrchestrator] = []

    def register(self, engine):

        self.engines.append(

            RevenueOrchestrator(

                engine=engine

            )

        )

    def total(self):

        return len(self.engines)

    def enabled(self):

        return len(

            [

                x

                for x in self.engines

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.engines

                if not x.enabled

            ]

        )

    def completion(self):

        if not self.engines:

            return 0.0

        return (

            self.enabled()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueOrchestratorEngine()

    print("=" * 70)
    print("REVENUE ORCHESTRATOR ENGINE")
    print("=" * 70)

    print("ENGINES        :", engine.total())
    print("ENABLED        :", engine.enabled())
    print("DISABLED       :", engine.disabled())
    print("COMPLETION (%) :", f"{engine.completion():.2f}")

