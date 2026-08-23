from dataclasses import dataclass
from typing import List


@dataclass
class RevenueChannel:

    name: str
    enabled: bool = True


class RevenueChannelEngine:

    def __init__(self):

        self.channels: List[RevenueChannel] = []

    def register(self, name: str):

        self.channels.append(
            RevenueChannel(name=name)
        )

    def total(self):

        return len(self.channels)

    def enabled(self):

        return len(

            [

                c

                for c in self.channels

                if c.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                c

                for c in self.channels

                if not c.enabled

            ]

        )


if __name__ == "__main__":

    engine = RevenueChannelEngine()

    print("=" * 70)
    print("REVENUE CHANNEL ENGINE")
    print("=" * 70)

    print("CHANNELS :", engine.total())
    print("ENABLED  :", engine.enabled())
    print("DISABLED :", engine.disabled())

