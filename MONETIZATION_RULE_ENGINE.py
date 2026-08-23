from dataclasses import dataclass
from typing import List


@dataclass
class MonetizationRule:

    capability: str
    market: str
    strategy: str
    enabled: bool = True


class MonetizationRuleEngine:

    def __init__(self):

        self.rules: List[MonetizationRule] = []

    def register(self, capability, market, strategy):

        self.rules.append(

            MonetizationRule(

                capability=capability,

                market=market,

                strategy=strategy

            )

        )

    def total(self):

        return len(self.rules)

    def enabled(self):

        return len(

            [

                x

                for x in self.rules

                if x.enabled

            ]

        )

    def markets(self):

        return len(

            {

                x.market

                for x in self.rules

            }

        )

    def capabilities(self):

        return len(

            {

                x.capability

                for x in self.rules

            }

        )

    def by_market(self, market):

        return [

            x

            for x in self.rules

            if x.market.lower() == market.lower()

        ]


if __name__ == "__main__":

    engine = MonetizationRuleEngine()

    print("=" * 70)
    print("MONETIZATION RULE ENGINE")
    print("=" * 70)

    print("RULES        :", engine.total())
    print("CAPABILITIES :", engine.capabilities())
    print("MARKETS      :", engine.markets())
    print("ENABLED      :", engine.enabled())

