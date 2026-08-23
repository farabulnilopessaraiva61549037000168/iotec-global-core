from dataclasses import dataclass
from typing import List


@dataclass
class RevenueCoreStatus:

    module: str
    online: bool = True


class RevenueCoreEngine:

    def __init__(self):

        self.modules: List[RevenueCoreStatus] = []

    def register(self, module):

        self.modules.append(

            RevenueCoreStatus(

                module=module

            )

        )

    def total(self):

        return len(self.modules)

    def online(self):

        return len(

            [

                x

                for x in self.modules

                if x.online

            ]

        )

    def offline(self):

        return len(

            [

                x

                for x in self.modules

                if not x.online

            ]

        )

    def completion(self):

        if not self.modules:

            return 0.0

        return (

            self.online()

            / self.total()

        ) * 100


if __name__ == "__main__":

    engine = RevenueCoreEngine()

    print("=" * 70)
    print("REVENUE CORE ENGINE")
    print("=" * 70)

    print("MODULES        :", engine.total())
    print("ONLINE         :", engine.online())
    print("OFFLINE        :", engine.offline())
    print("COMPLETION (%) :", f"{engine.completion():.2f}")

