from dataclasses import dataclass
from typing import List


@dataclass
class ServicePortfolio:

    name: str
    category: str
    enabled: bool = True


class ServicePortfolioEngine:

    def __init__(self):

        self.services: List[ServicePortfolio] = []

    def register(self, name, category):

        self.services.append(
            ServicePortfolio(
                name=name,
                category=category
            )
        )

    def total(self):

        return len(self.services)

    def enabled(self):

        return len(
            [
                s
                for s in self.services
                if s.enabled
            ]
        )

    def disabled(self):

        return len(
            [
                s
                for s in self.services
                if not s.enabled
            ]
        )

    def categories(self):

        return sorted(
            {
                s.category
                for s in self.services
            }
        )


if __name__ == "__main__":

    engine = ServicePortfolioEngine()

    print("=" * 70)
    print("SERVICE PORTFOLIO ENGINE")
    print("=" * 70)

    print("SERVICES   :", engine.total())
    print("ENABLED    :", engine.enabled())
    print("DISABLED   :", engine.disabled())
    print("CATEGORIES :", len(engine.categories()))

