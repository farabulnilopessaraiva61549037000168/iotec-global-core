from dataclasses import dataclass
from typing import List


@dataclass
class PipelineItem:

    company: str
    stage: str
    estimated_value: float


class RevenuePipelineEngine:

    def __init__(self):

        self.pipeline: List[PipelineItem] = []

    def add(self, company, stage, value):

        self.pipeline.append(
            PipelineItem(company, stage, value)
        )

    def total_value(self):

        return sum(
            item.estimated_value
            for item in self.pipeline
        )

    def count(self):

        return len(self.pipeline)

    def summary(self):

        stages = {}

        for item in self.pipeline:

            stages[item.stage] = (
                stages.get(item.stage, 0) + 1
            )

        return stages


if __name__ == "__main__":

    engine = RevenuePipelineEngine()

    engine.add(
        "Empresa A",
        "Contato",
        8000
    )

    engine.add(
        "Empresa B",
        "Proposta",
        15000
    )

    engine.add(
        "Empresa C",
        "NegociaÃƒÂ§ÃƒÂ£o",
        25000
    )

    print("=" * 60)
    print("REVENUE PIPELINE ENGINE")
    print("=" * 60)

    print("Itens :", engine.count())
    print("Valor :", engine.total_value())

    print()

    for k, v in engine.summary().items():

        print(f"{k:15} {v}")

