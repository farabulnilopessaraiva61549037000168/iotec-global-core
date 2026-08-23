from dataclasses import dataclass
from typing import List


@dataclass
class RevenueEvent:

    event: str
    source: str
    severity: str = "INFO"
    processed: bool = False


class RevenueEventEngine:

    def __init__(self):

        self.events: List[RevenueEvent] = []

    def register(self, event, source, severity="INFO"):

        self.events.append(

            RevenueEvent(

                event=event,

                source=source,

                severity=severity

            )

        )

    def total(self):

        return len(self.events)

    def processed(self):

        return len(

            [

                x

                for x in self.events

                if x.processed

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.events

                if not x.processed

            ]

        )

    def sources(self):

        return len(

            {

                x.source

                for x in self.events

            }

        )

    def info(self):

        return len(

            [

                x

                for x in self.events

                if x.severity == "INFO"

            ]

        )

    def warning(self):

        return len(

            [

                x

                for x in self.events

                if x.severity == "WARNING"

            ]

        )

    def error(self):

        return len(

            [

                x

                for x in self.events

                if x.severity == "ERROR"

            ]

        )


if __name__ == "__main__":

    engine = RevenueEventEngine()

    print("=" * 70)
    print("REVENUE EVENT ENGINE")
    print("=" * 70)

    print("EVENTS     :", engine.total())
    print("PENDING    :", engine.pending())
    print("PROCESSED  :", engine.processed())
    print("SOURCES    :", engine.sources())
    print("INFO       :", engine.info())
    print("WARNING    :", engine.warning())
    print("ERROR      :", engine.error())

