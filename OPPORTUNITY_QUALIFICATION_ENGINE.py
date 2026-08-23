from dataclasses import dataclass
from typing import List


@dataclass
class OpportunityQualification:

    opportunity: str
    compatible: bool = False
    validated: bool = False
    monetizable: bool = False


class OpportunityQualificationEngine:

    def __init__(self):

        self.items: List[OpportunityQualification] = []

    def register(self, opportunity):

        self.items.append(

            OpportunityQualification(

                opportunity=opportunity

            )

        )

    def total(self):

        return len(self.items)

    def compatible(self):

        return len(

            [

                x

                for x in self.items

                if x.compatible

            ]

        )

    def validated(self):

        return len(

            [

                x

                for x in self.items

                if x.validated

            ]

        )

    def monetizable(self):

        return len(

            [

                x

                for x in self.items

                if x.monetizable

            ]

        )


if __name__ == "__main__":

    engine = OpportunityQualificationEngine()

    print("=" * 70)
    print("OPPORTUNITY QUALIFICATION ENGINE")
    print("=" * 70)

    print("OPPORTUNITIES :", engine.total())
    print("COMPATIBLE    :", engine.compatible())
    print("VALIDATED     :", engine.validated())
    print("MONETIZABLE   :", engine.monetizable())

