from dataclasses import dataclass
from typing import List


@dataclass
class ServiceOpportunity:

    title: str
    category: str
    source: str
    location: str
    url: str
    estimated_value: float = 0.0
    compatible: bool = False


class ServiceDiscoveryEngine:

    def __init__(self):

        self.opportunities: List[ServiceOpportunity] = []

    def add(self, opportunity: ServiceOpportunity):

        self.opportunities.append(opportunity)

    def total(self):

        return len(self.opportunities)

    def compatible(self):

        return [

            item

            for item in self.opportunities

            if item.compatible

        ]

    def pending(self):

        return [

            item

            for item in self.opportunities

            if not item.compatible

        ]

    def clear(self):

        self.opportunities.clear()


if __name__ == "__main__":

    engine = ServiceDiscoveryEngine()

    print("=" * 70)
    print("SERVICE DISCOVERY ENGINE")
    print("=" * 70)

    print("TOTAL OPPORTUNITIES :", engine.total())
    print("COMPATIBLE          :", len(engine.compatible()))
    print("PENDING ANALYSIS    :", len(engine.pending()))

