from dataclasses import dataclass
from typing import List


@dataclass
class RevenueKernel:

    component: str
    version: str
    online: bool = True


class RevenueKernelEngine:

    def __init__(self):

        self.components: List[RevenueKernel] = []

    def register(self, component, version):

        self.components.append(

            RevenueKernel(

                component=component,

                version=version

            )

        )

    def total(self):

        return len(self.components)

    def online(self):

        return len(

            [

                x

                for x in self.components

                if x.online

            ]

        )

    def offline(self):

        return len(

            [

                x

                for x in self.components

                if not x.online

            ]

        )

    def versions(self):

        return len(

            {

                x.version

                for x in self.components

            }

        )


if __name__ == "__main__":

    engine = RevenueKernelEngine()

    print("=" * 70)
    print("REVENUE KERNEL ENGINE")
    print("=" * 70)

    print("COMPONENTS :", engine.total())
    print("VERSIONS   :", engine.versions())
    print("ONLINE     :", engine.online())
    print("OFFLINE    :", engine.offline())

