from dataclasses import dataclass
from typing import Dict, Callable, Any


@dataclass
class RevenueCommand:

    name: str
    command: Callable[..., Any]
    enabled: bool = True


class RevenueCommandCenterEngine:

    def __init__(self):

        self.commands: Dict[str, RevenueCommand] = {}

    def register(self, name, command):

        self.commands[name] = RevenueCommand(

            name=name,

            command=command

        )

    def unregister(self, name):

        self.commands.pop(name, None)

    def exists(self, name):

        return name in self.commands

    def total(self):

        return len(self.commands)

    def enabled(self):

        return len(

            [

                x

                for x in self.commands.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.commands.values()

                if not x.enabled

            ]

        )

    def names(self):

        return sorted(

            self.commands.keys()

        )


if __name__ == "__main__":

    engine = RevenueCommandCenterEngine()

    print("=" * 70)

    print("REVENUE COMMAND CENTER ENGINE")

    print("=" * 70)

    print("COMMANDS   :", engine.total())

    print("ENABLED    :", engine.enabled())

    print("DISABLED   :", engine.disabled())

