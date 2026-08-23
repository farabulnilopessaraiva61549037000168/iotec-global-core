from dataclasses import dataclass
from typing import List


@dataclass
class RevenueWorkflow:

    stage: str
    enabled: bool = True


class RevenueWorkflowEngine:

    def __init__(self):

        self.workflow: List[RevenueWorkflow] = []

    def register(self, stage):

        self.workflow.append(
            RevenueWorkflow(stage=stage)
        )

    def total(self):

        return len(self.workflow)

    def enabled(self):

        return len(
            [
                x
                for x in self.workflow
                if x.enabled
            ]
        )

    def disabled(self):

        return len(
            [
                x
                for x in self.workflow
                if not x.enabled
            ]
        )

    def stages(self):

        return [
            x.stage
            for x in self.workflow
        ]


if __name__ == "__main__":

    engine = RevenueWorkflowEngine()

    print("=" * 70)
    print("REVENUE WORKFLOW ENGINE")
    print("=" * 70)

    print("STAGES    :", engine.total())
    print("ENABLED   :", engine.enabled())
    print("DISABLED  :", engine.disabled())

