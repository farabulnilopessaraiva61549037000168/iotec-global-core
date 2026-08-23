from dataclasses import dataclass
from typing import List


@dataclass
class ServiceCategory:

    name: str
    active: bool = True


class ServiceCategoryEngine:

    def __init__(self):

        self.categories: List[ServiceCategory] = []

    def register(self, name):

        self.categories.append(
            ServiceCategory(name=name)
        )

    def total(self):

        return len(self.categories)

    def active(self):

        return len(
            [
                c
                for c in self.categories
                if c.active
            ]
        )

    def inactive(self):

        return len(
            [
                c
                for c in self.categories
                if not c.active
            ]
        )

    def exists(self, name):

        return any(
            c.name.lower() == name.lower()
            for c in self.categories
        )


if __name__ == "__main__":

    engine = ServiceCategoryEngine()

    print("=" * 70)
    print("SERVICE CATEGORY ENGINE")
    print("=" * 70)

    print("CATEGORIES :", engine.total())
    print("ACTIVE     :", engine.active())
    print("INACTIVE   :", engine.inactive())

