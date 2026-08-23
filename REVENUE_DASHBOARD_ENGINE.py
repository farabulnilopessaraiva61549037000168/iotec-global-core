from dataclasses import dataclass
from typing import List


@dataclass
class RevenueDashboard:

    metric: str
    value: float


class RevenueDashboardEngine:

    def __init__(self):

        self.metrics: List[RevenueDashboard] = []

    def register(self, metric, value):

        self.metrics.append(

            RevenueDashboard(

                metric=metric,

                value=value

            )

        )

    def total(self):

        return len(self.metrics)

    def metric_names(self):

        return len(

            {

                x.metric

                for x in self.metrics

            }

        )

    def total_value(self):

        return sum(

            x.value

            for x in self.metrics

        )

    def average(self):

        if not self.metrics:

            return 0.0

        return self.total_value() / self.total()


if __name__ == "__main__":

    engine = RevenueDashboardEngine()

    print("=" * 70)
    print("REVENUE DASHBOARD ENGINE")
    print("=" * 70)

    print("METRICS      :", engine.total())
    print("UNIQUE       :", engine.metric_names())
    print("TOTAL VALUE  :", engine.total_value())
    print("AVERAGE      :", f"{engine.average():.2f}")

