from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class RevenueBus:

    source: str
    target: str
    payload: Any = None
    processed: bool = False


class RevenueBusEngine:

    def __init__(self):

        self.routes: Dict[str, Any] = {}

        self.messages: List[RevenueBus] = []

    def register(self, name, engine):

        self.routes[name] = engine

    def send(self, source, target, payload=None):

        self.messages.append(

            RevenueBus(

                source=source,

                target=target,

                payload=payload

            )

        )

    def total_routes(self):

        return len(self.routes)

    def total_messages(self):

        return len(self.messages)

    def processed(self):

        return len(

            [

                x

                for x in self.messages

                if x.processed

            ]

        )

    def pending(self):

        return len(

            [

                x

                for x in self.messages

                if not x.processed

            ]

        )


if __name__ == "__main__":

    bus = RevenueBusEngine()

    print("=" * 70)

    print("REVENUE BUS ENGINE")

    print("=" * 70)

    print("ROUTES     :", bus.total_routes())

    print("MESSAGES   :", bus.total_messages())

    print("PROCESSED  :", bus.processed())

    print("PENDING    :", bus.pending())

