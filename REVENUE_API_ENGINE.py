from dataclasses import dataclass
from typing import Callable, Dict, Any


@dataclass
class RevenueApiRoute:

    path: str

    method: str

    handler: Callable[..., Any]

    enabled: bool = True


class RevenueApiEngine:

    def __init__(self):

        self.routes: Dict[str, RevenueApiRoute] = {}

    def register(self, path, method, handler):

        key = f"{method.upper()}:{path}"

        self.routes[key] = RevenueApiRoute(

            path=path,

            method=method.upper(),

            handler=handler

        )

    def unregister(self, path, method):

        key = f"{method.upper()}:{path}"

        self.routes.pop(key, None)

    def exists(self, path, method):

        key = f"{method.upper()}:{path}"

        return key in self.routes

    def total(self):

        return len(self.routes)

    def enabled(self):

        return len(

            [

                x

                for x in self.routes.values()

                if x.enabled

            ]

        )

    def disabled(self):

        return len(

            [

                x

                for x in self.routes.values()

                if not x.enabled

            ]

        )


if __name__ == "__main__":

    api = RevenueApiEngine()

    print("=" * 70)

    print("REVENUE API ENGINE")

    print("=" * 70)

    print("ROUTES     :", api.total())

    print("ENABLED    :", api.enabled())

    print("DISABLED   :", api.disabled())

