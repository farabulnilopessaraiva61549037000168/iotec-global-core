from dataclasses import dataclass
from typing import List


@dataclass
class RevenueTarget:

    name: str
    category: str
    priority: int
    active: bool = True


class RevenueTargetRegistry:

    def __init__(self):

        self.targets: List[RevenueTarget] = []

    def register(self, name, category, priority):

        self.targets.append(

            RevenueTarget(

                name=name,

                category=category,

                priority=priority

            )

        )

    def total(self):

        return len(self.targets)

    def active(self):

        return len(

            [

                x

                for x in self.targets

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.targets

                if not x.active

            ]

        )

    def categories(self):

        return sorted(

            {

                x.category

                for x in self.targets

            }

        )


if __name__ == "__main__":

    engine = RevenueTargetRegistry()

    print("=" * 70)
    print("REVENUE TARGET REGISTRY")
    print("=" * 70)

    print("TARGETS    :", engine.total())
    print("ACTIVE     :", engine.active())
    print("INACTIVE   :", engine.inactive())
    print("CATEGORIES :", len(engine.categories()))

