from dataclasses import dataclass


@dataclass
class RevenueSystemStatus:

    hub: bool = False

    bus: bool = False

    database: bool = False

    repository: bool = False

    api: bool = False

    controller: bool = False

    integration: bool = False

    decision: bool = False

    command_center: bool = False


class RevenueSystemEngine:

    def __init__(self):

        self.status = RevenueSystemStatus()

    def connect_hub(self):

        self.status.hub = True

    def connect_bus(self):

        self.status.bus = True

    def connect_database(self):

        self.status.database = True

    def connect_repository(self):

        self.status.repository = True

    def connect_api(self):

        self.status.api = True

    def connect_controller(self):

        self.status.controller = True

    def connect_integration(self):

        self.status.integration = True

    def connect_decision(self):

        self.status.decision = True

    def connect_command_center(self):

        self.status.command_center = True

    def completion(self):

        itens = [

            self.status.hub,

            self.status.bus,

            self.status.database,

            self.status.repository,

            self.status.api,

            self.status.controller,

            self.status.integration,

            self.status.decision,

            self.status.command_center

        ]

        ativos = sum(itens)

        return ativos, len(itens), (ativos / len(itens)) * 100


if __name__ == "__main__":

    engine = RevenueSystemEngine()

    ativos, total, percentual = engine.completion()

    print("=" * 70)

    print("REVENUE SYSTEM ENGINE")

    print("=" * 70)

    print("CONNECTED :", ativos)

    print("TOTAL     :", total)

    print("PROGRESS  :", f"{percentual:.2f}%")

