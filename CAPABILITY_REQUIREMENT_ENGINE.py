from dataclasses import dataclass
from typing import List


@dataclass
class CapabilityRequirement:

    service: str
    capability: str
    required: bool = True


class CapabilityRequirementEngine:

    def __init__(self):

        self.requirements: List[CapabilityRequirement] = []

    def register(self, service, capability):

        self.requirements.append(

            CapabilityRequirement(

                service=service,

                capability=capability

            )

        )

    def total(self):

        return len(self.requirements)

    def services(self):

        return len(

            {

                x.service

                for x in self.requirements

            }

        )

    def capabilities(self):

        return len(

            {

                x.capability

                for x in self.requirements

            }

        )

    def by_service(self, service):

        return [

            x

            for x in self.requirements

            if x.service == service

        ]


if __name__ == "__main__":

    engine = CapabilityRequirementEngine()

    print("=" * 70)
    print("CAPABILITY REQUIREMENT ENGINE")
    print("=" * 70)

    print("SERVICES     :", engine.services())
    print("CAPABILITIES :", engine.capabilities())
    print("RELATIONS    :", engine.total())

