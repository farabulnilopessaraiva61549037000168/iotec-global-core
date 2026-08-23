from dataclasses import dataclass
from typing import List


@dataclass
class OpportunityMonitor:

    name: str
    source: str
    enabled: bool = True


class OpportunityMonitorEngine:

    def __init__(self):

        self.monitors: List[OpportunityMonitor] = []

    def register(self, name, source):

        self.monitors.append(

            OpportunityMonitor(

                name=name,

                source=source

            )

        )

    def total(self):

        return len(self.monitors)

    def enabled(self):

        return len(

            [

                x

                for x in self.monitors

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.monitors

                if not x.enabled

            ]

        )

    def sources(self):

        return len(

            {

                x.source

                for x in self.monitors

            }

        )


if __name__ == "__main__":

    engine = OpportunityMonitorEngine()

    print("=" * 70)
    print("OPPORTUNITY MONITOR ENGINE")
    print("=" * 70)

    print("MONITORS :", engine.total())
    print("SOURCES  :", engine.sources())
    print("ENABLED  :", engine.enabled())
    print("DISABLED :", engine.disabled())

