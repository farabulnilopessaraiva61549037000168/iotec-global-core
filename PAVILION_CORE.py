"""
=========================================================
IOTEC - PAVILION CORE
Primeiro PavilhÃƒÂ£o
=========================================================
MissÃƒÂ£o:
Orquestrar todo o funcionamento do Primeiro PavilhÃƒÂ£o.
=========================================================
"""

from datetime import datetime


class PavilionCore:

    def __init__(self):

        self.name = "PRIMEIRO PAVILHÃƒÆ'O"
        self.version = "1.0"
        self.status = "INICIALIZANDO"

        self.components = {}

        self.created_at = datetime.now()

    # --------------------------------------------------

    def register_component(self, name):

        self.components[name] = {
            "status": "REGISTRADO",
            "last_check": None
        }

        print(f"[OK] {name} registrado.")

    # --------------------------------------------------

    def update_status(self, component, status):

        if component in self.components:

            self.components[component]["status"] = status
            self.components[component]["last_check"] = datetime.now()

    # --------------------------------------------------

    def system_summary(self):

        print("\n==============================")
        print("PAVILION CORE")
        print("==============================")

        print(f"Nome     : {self.name}")
        print(f"VersÃƒÂ£o   : {self.version}")
        print(f"Status   : {self.status}")
        print(f"Criado   : {self.created_at}")

        print("\nComponentes:")

        for component, info in self.components.items():

            print(
                f" - {component:<30}"
                f"{info['status']}"
            )

        print("==============================\n")

    # --------------------------------------------------

    def start(self):

        self.status = "OPERACIONAL"

        print("\n========================================")
        print("IOTEC PAVILION CORE")
        print("========================================")
        print("Primeiro PavilhÃƒÂ£o iniciado.")
        print("Sistema operacional.")
        print("========================================\n")


# =====================================================

if __name__ == "__main__":

    core = PavilionCore()

    core.register_component("SYSTEM_HEALTH_ENGINE")
    core.register_component("TECHNICAL_LASSO")
    core.register_component("HOMOLOGATION_ENGINE")
    core.register_component("TECHNICAL_REPORT_ENGINE")
    core.register_component("BILLING_ENGINE")
    core.register_component("PAYMENT_MONITOR_ENGINE")
    core.register_component("CASHBOX_ENGINE")

    core.start()

    core.system_summary()

