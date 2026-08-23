from dataclasses import dataclass
from typing import List


@dataclass
class ServiceCapability:

    service: str
    capability: str


class ServiceCapabilityEngine:

    def __init__(self):

        self.links: List[ServiceCapability] = []

    def register(self, service: str, capability: str):

        self.links.append(
            ServiceCapability(
                service=service,
                capability=capability
            )
        )

    def total(self):

        return len(self.links)

    def services(self):

        return len(
            set(
                item.service
                for item in self.links
            )
        )

    def capabilities(self):

        return len(
            set(
                item.capability
                for item in self.links
            )
        )

    def find(self, service):

        return [

            item.capability

            for item in self.links

            if item.service == service

        ]


if __name__ == "__main__":

    engine = ServiceCapabilityEngine()

    print("=" * 70)
    print("SERVICE CAPABILITY ENGINE")
    print("=" * 70)

    print("SERVICES    :", engine.services())
    print("CAPABILITIES:", engine.capabilities())
    print("RELATIONS   :", engine.total())

