from dataclasses import dataclass
from typing import List


@dataclass
class RevenueBootstrap:

    module: str
    initialized: bool = False


class RevenueBootstrapEngine:

    def __init__(self):

        self.modules: List[RevenueBootstrap] = []

    def register(self, module):

        self.modules.append(

            RevenueBootstrap(

                module=module

            )

        )

    def total(self):

        return len(self.modules)

    def initialized(self):

        return len(

            [

                x

                for x in self.modules

                if x.initialized

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.modules

                if not x.initialized

            ]

        )

    def progress(self):

        if not self.modules:

            return 0.0

        return (

            self.initialized()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueBootstrapEngine()

    print("=" * 70)
    print("REVENUE BOOTSTRAP ENGINE")
    print("=" * 70)

    print("MODULES        :", engine.total())
    print("INITIALIZED    :", engine.initialized())
    print("PENDING        :", engine.pending())
    print("PROGRESS (%)   :", f"{engine.progress():.2f}")

