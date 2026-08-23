from dataclasses import dataclass
from typing import List


@dataclass
class OpportunityCategory:

    name: str
    enabled: bool = True


class OpportunityCategoryEngine:

    def __init__(self):

        self.categories: List[OpportunityCategory] = []

    def register(self, name):

        self.categories.append(
            OpportunityCategory(name=name)
        )

    def total(self):

        return len(self.categories)

    def enabled(self):

        return len(
            [
                c
                for c in self.categories
                if c.enabled
            ]
        )

    def disabled(self):

        return len(
            [
                c
                for c in self.categories
                if not c.enabled
            ]
        )

    def names(self):

        return sorted(
            [
                c.name
                for c in self.categories
            ]
        )


if __name__ == "__main__":

    engine = OpportunityCategoryEngine()

    print("=" * 70)
    print("OPPORTUNITY CATEGORY ENGINE")
    print("=" * 70)

    print("CATEGORIES :", engine.total())
    print("ENABLED    :", engine.enabled())
    print("DISABLED   :", engine.disabled())

