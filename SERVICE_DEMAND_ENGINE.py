from dataclasses import dataclass
from typing import List


@dataclass
class ServiceDemand:

    sector: str
    service: str
    priority: int
    active: bool = True


class ServiceDemandEngine:

    def __init__(self):

        self.demands: List[ServiceDemand] = []

    def register(self, sector, service, priority):

        self.demands.append(

            ServiceDemand(

                sector=sector,

                service=service,

                priority=priority

            )

        )

    def total(self):

        return len(self.demands)

    def active(self):

        return len(

            [

                x

                for x in self.demands

                if x.active

            ]

        )

    def inactive(self):

        return len(

            [

                x

                for x in self.demands

                if not x.active

            ]

        )

    def sectors(self):

        return len(

            {

                x.sector

                for x in self.demands

            }

        )

    def services(self):

        return len(

            {

                x.service

                for x in self.demands

            }

        )


if __name__ == "__main__":

    engine = ServiceDemandEngine()

    print("=" * 70)
    print("SERVICE DEMAND ENGINE")
    print("=" * 70)

    print("DEMANDS    :", engine.total())
    print("SECTORS    :", engine.sectors())
    print("SERVICES   :", engine.services())
    print("ACTIVE     :", engine.active())
    print("INACTIVE   :", engine.inactive())

