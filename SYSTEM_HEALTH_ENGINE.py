"""
=========================================================
IOTEC - SYSTEM HEALTH ENGINE
=========================================================
ResponsÃƒÂ¡vel por verificar a saÃƒÂºde dos componentes.
=========================================================
"""

from datetime import datetime


class SystemHealthEngine:

    def __init__(self):

        self.components = {}

    # -----------------------------------------------------

    def register(self, name):

        self.components[name] = {
            "status": "UNKNOWN",
            "checked_at": None
        }

    # -----------------------------------------------------

    def check(self, name, status=True):

        if name not in self.components:
            return

        self.components[name]["status"] = "ONLINE" if status else "OFFLINE"
        self.components[name]["checked_at"] = datetime.now()

    # -----------------------------------------------------

    def check_all(self):

        for component in self.components:
            self.check(component, True)

    # -----------------------------------------------------

    def online_count(self):

        return sum(
            1
            for component in self.components.values()
            if component["status"] == "ONLINE"
        )

    # -----------------------------------------------------

    def total(self):

        return len(self.components)

    # -----------------------------------------------------

    def health_percentage(self):

        if self.total() == 0:
            return 0

        return round(
            (self.online_count() / self.total()) * 100,
            2
        )

    # -----------------------------------------------------

    def report(self):

        print("\n===================================")
        print("SYSTEM HEALTH REPORT")
        print("===================================")

        for name, info in self.components.items():

            print(
                f"{name:<35}"
                f"{info['status']}"
            )

        print("-----------------------------------")
        print(f"ONLINE : {self.online_count()}")
        print(f"TOTAL  : {self.total()}")
        print(f"SAÃƒÅ¡DE  : {self.health_percentage()}%")
        print("===================================\n")


if __name__ == "__main__":

    engine = SystemHealthEngine()

    engine.register("SYSTEM_HEALTH_ENGINE")
    engine.register("TECHNICAL_LASSO")
    engine.register("HOMOLOGATION_ENGINE")
    engine.register("TECHNICAL_REPORT_ENGINE")
    engine.register("BILLING_ENGINE")
    engine.register("PAYMENT_MONITOR_ENGINE")
    engine.register("CASHBOX_ENGINE")

    engine.check_all()

    engine.report()

