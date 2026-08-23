from dataclasses import dataclass
from typing import List


@dataclass
class RevenueOperation:

    operation: str
    module: str
    active: bool = True


class RevenueOperationEngine:

    def __init__(self):

        self.operations: List[RevenueOperation] = []

    def register(self, operation, module):

        self.operations.append(

            RevenueOperation(

                operation=operation,

                module=module

            )

        )

    def total(self):

        return len(self.operations)

    def active(self):

        return len(

            [

                x

                for x in self.operations

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.operations

                if not x.active

            ]

        )

    def modules(self):

        return len(

            {

                x.module

                for x in self.operations

            }

        )


if __name__ == "__main__":

    engine = RevenueOperationEngine()

    print("=" * 70)
    print("REVENUE OPERATION ENGINE")
    print("=" * 70)

    print("OPERATIONS :", engine.total())
    print("MODULES    :", engine.modules())
    print("ACTIVE     :", engine.active())
    print("INACTIVE   :", engine.inactive())

