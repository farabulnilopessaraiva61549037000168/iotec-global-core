from dataclasses import dataclass
from typing import List


@dataclass
class RevenueTelemetry:

    event: str
    level: str = "INFO"
    processed: bool = False


class RevenueTelemetryEngine:

    def __init__(self):

        self.events: List[RevenueTelemetry] = []

    def register(self, event, level="INFO"):

        self.events.append(

            RevenueTelemetry(

                event=event,

                level=level

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

    def info(self):

        return len(

            [

                x

                for x in self.events

                if x.level == "INFO"

            ]

        )

    def warning(self):

        return len(

            [

                x

                for x in self.events

                if x.level == "WARNING"

            ]

        )

    def error(self):

        return len(

            [

                x

                for x in self.events

                if x.level == "ERROR"

            ]

        )


if __name__ == "__main__":

    engine = RevenueTelemetryEngine()

    print("=" * 70)
    print("REVENUE TELEMETRY ENGINE")
    print("=" * 70)

    print("EVENTS     :", engine.total())
    print("PENDING    :", engine.pending())
    print("PROCESSED  :", engine.processed())
    print("INFO       :", engine.info())
    print("WARNING    :", engine.warning())
    print("ERROR      :", engine.error())

