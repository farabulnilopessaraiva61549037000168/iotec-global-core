from dataclasses import dataclass
from typing import List


@dataclass
class RevenueCapability:

    capability: str
    market: str
    execution_type: str
    active: bool = True


class RevenueCapabilityEngine:

    def __init__(self):

        self.capabilities: List[RevenueCapability] = []

    def register(self, capability, market, execution_type):

        self.capabilities.append(

            RevenueCapability(

                capability=capability,

                market=market,

                execution_type=execution_type

            )

        )

    def total(self):

        return len(self.capabilities)

    def active(self):

        return len(

            [

                x

                for x in self.capabilities

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.capabilities

                if not x.active

            ]

        )

    def markets(self):

        return len(

            {

                x.market

                for x in self.capabilities

            }

        )

    def execution_types(self):

        return len(

            {

                x.execution_type

                for x in self.capabilities

            }

        )


if __name__ == "__main__":

    engine = RevenueCapabilityEngine()

    print("=" * 70)
    print("REVENUE CAPABILITY ENGINE")
    print("=" * 70)

    print("CAPABILITIES    :", engine.total())
    print("MARKETS         :", engine.markets())
    print("EXECUTION TYPES :", engine.execution_types())
    print("ACTIVE          :", engine.active())
    print("INACTIVE        :", engine.inactive())

