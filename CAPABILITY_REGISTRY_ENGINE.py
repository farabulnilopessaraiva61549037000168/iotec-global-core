from dataclasses import dataclass
from typing import List


@dataclass
class Capability:

    name: str
    category: str
    active: bool = True


class CapabilityRegistryEngine:

    def __init__(self):

        self.capabilities: List[Capability] = []

    def register(self, capability: Capability):

        self.capabilities.append(capability)

    def total(self):

        return len(self.capabilities)

    def active(self):

        return len(

            [

                c

                for c in self.capabilities

                if c.active

            ]

        )

    def inactive(self):

        return len(

            [

                c

                for c in self.capabilities

                if not c.active

            ]

        )

    def clear(self):

        self.capabilities.clear()


if __name__ == "__main__":

    engine = CapabilityRegistryEngine()

    print("=" * 70)
    print("CAPABILITY REGISTRY ENGINE")
    print("=" * 70)

    print("TOTAL      :", engine.total())
    print("ACTIVE     :", engine.active())
    print("INACTIVE   :", engine.inactive())

