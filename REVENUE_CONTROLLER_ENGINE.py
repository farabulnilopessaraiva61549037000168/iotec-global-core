from dataclasses import dataclass
from typing import Dict, Callable, Any


@dataclass
class RevenueController:

    name: str
    handler: Callable[..., Any]
    enabled: bool = True


class RevenueControllerEngine:

    def __init__(self):

        self.controllers: Dict[str, RevenueController] = {}

    def register(self, name, handler):

        self.controllers[name] = RevenueController(

            name=name,

            handler=handler

        )

    def unregister(self, name):

        self.controllers.pop(name, None)

    def exists(self, name):

        return name in self.controllers

    def total(self):

        return len(self.controllers)

    def enabled(self):

        return len(

            [

                x

                for x in self.controllers.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.controllers.values()

                if not x.enabled

            ]

        )


if __name__ == "__main__":

    controller = RevenueControllerEngine()

    print("=" * 70)

    print("REVENUE CONTROLLER ENGINE")

    print("=" * 70)

    print("CONTROLLERS :", controller.total())

    print("ENABLED     :", controller.enabled())

    print("DISABLED    :", controller.disabled())

