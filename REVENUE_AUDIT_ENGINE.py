from dataclasses import dataclass
from typing import List


@dataclass
class RevenueAudit:

    component: str
    status: str = "NOT_CHECKED"
    issues: int = 0


class RevenueAuditEngine:

    def __init__(self):

        self.components: List[RevenueAudit] = []

    def register(self, component):

        self.components.append(

            RevenueAudit(

                component=component

            )

        )

    def total(self):

        return len(self.components)

    def checked(self):

        return len(

            [

                x

                for x in self.components

                if x.status != "NOT_CHECKED"

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "NOT_CHECKED"

            ]

        )

    def approved(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "APPROVED"

            ]

        )

    def rejected(self):

        return len(

            [

                x

                for x in self.components

                if x.status == "REJECTED"

            ]

        )

    def total_issues(self):

        return sum(

            x.issues

            for x in self.components

        )


if __name__ == "__main__":

    engine = RevenueAuditEngine()

    print("=" * 70)
    print("REVENUE AUDIT ENGINE")
    print("=" * 70)

    print("COMPONENTS :", engine.total())
    print("CHECKED    :", engine.checked())
    print("PENDING    :", engine.pending())
    print("APPROVED   :", engine.approved())
    print("REJECTED   :", engine.rejected())
    print("ISSUES     :", engine.total_issues())

