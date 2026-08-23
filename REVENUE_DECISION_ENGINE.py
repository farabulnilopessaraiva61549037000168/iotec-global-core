from dataclasses import dataclass
from typing import Dict, Callable, Any


@dataclass
class RevenueDecision:

    name: str
    decision: Callable[..., Any]
    enabled: bool = True


class RevenueDecisionEngine:

    def __init__(self):

        self.decisions: Dict[str, RevenueDecision] = {}

    def register(self, name, decision):

        self.decisions[name] = RevenueDecision(

            name=name,

            decision=decision

        )

    def unregister(self, name):

        self.decisions.pop(name, None)

    def exists(self, name):

        return name in self.decisions

    def total(self):

        return len(self.decisions)

    def enabled(self):

        return len(

            [

                x

                for x in self.decisions.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.decisions.values()

                if not x.enabled

            ]

        )

    def names(self):

        return sorted(

            self.decisions.keys()

        )


if __name__ == "__main__":

    engine = RevenueDecisionEngine()

    print("=" * 70)

    print("REVENUE DECISION ENGINE")

    print("=" * 70)

    print("DECISIONS  :", engine.total())

    print("ENABLED    :", engine.enabled())

    print("DISABLED   :", engine.disabled())

