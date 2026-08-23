from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class RevenueEvent:

    timestamp: str
    company: str
    action: str
    value: float


class RevenueLedgerEngine:

    def __init__(self):

        self.events: List[RevenueEvent] = []

    def register(self, company, action, value):

        self.events.append(
            RevenueEvent(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                company,
                action,
                value
            )
        )

    def total(self):

        return sum(
            event.value
            for event in self.events
        )

    def show(self):

        for event in self.events:

            print(
                f"{event.timestamp} | "
                f"{event.company:20} | "
                f"{event.action:15} | "
                f"R$ {event.value:10.2f}"
            )


if __name__ == "__main__":

    ledger = RevenueLedgerEngine()

    ledger.register(
        "Empresa A",
        "Lead",
        8000
    )

    ledger.register(
        "Empresa B",
        "Proposta",
        15000
    )

    ledger.register(
        "Empresa C",
        "Contrato",
        25000
    )

    print("=" * 70)
    print("REVENUE LEDGER ENGINE")
    print("=" * 70)

    ledger.show()

    print()

    print("TOTAL :", ledger.total())

