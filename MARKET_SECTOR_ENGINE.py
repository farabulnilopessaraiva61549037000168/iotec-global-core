from dataclasses import dataclass
from typing import List


@dataclass
class MarketSector:

    name: str
    active: bool = True


class MarketSectorEngine:

    def __init__(self):

        self.sectors: List[MarketSector] = []

    def register(self, name: str):

        self.sectors.append(
            MarketSector(name=name)
        )

    def total(self):

        return len(self.sectors)

    def active(self):

        return len(
            [
                s
                for s in self.sectors
                if s.active
            ]
        )

    def inactive(self):

        return len(
            [
                s
                for s in self.sectors
                if not s.active
            ]
        )

    def clear(self):

        self.sectors.clear()


if __name__ == "__main__":

    engine = MarketSectorEngine()

    print("=" * 70)
    print("MARKET SECTOR ENGINE")
    print("=" * 70)

    print("SECTORS  :", engine.total())
    print("ACTIVE   :", engine.active())
    print("INACTIVE :", engine.inactive())

