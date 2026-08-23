from dataclasses import dataclass
from typing import List


@dataclass
class BootModule:

    name: str

    initialized: bool = False


class RevenueKernelBootEngine:

    def __init__(self):

        self.modules: List[BootModule] = []

    def register(self, name):

        self.modules.append(

            BootModule(

                name=name

            )

        )

    def initialize(self):

        for module in self.modules:

            module.initialized = True

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

    engine = RevenueKernelBootEngine()

    print("=" * 70)

    print("REVENUE KERNEL BOOT ENGINE")

    print("=" * 70)

    print("MODULES      :", engine.total())

    print("INITIALIZED  :", engine.initialized())

    print("PENDING      :", engine.pending())

    print("PROGRESS (%) :", f"{engine.progress():.2f}")

