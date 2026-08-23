# ============================================================
# IOTEC - SENSOR MANAGER
# CÃƒÂ³digo 002 da Cadeia Principal
# ============================================================

import datetime


class SensorManager:

    def __init__(self):

        self.sensors = {}

        self.load_default_sensors()

    # ---------------------------------------------------------

    def load_default_sensors(self):

        defaults = [

            "COMMERCIAL_RADAR",
            "CONTROL_TOWER",
            "DATABASE",
            "PAYPAL",
            "CRM",
            "WEBSITE",
            "EMAIL",
            "FINANCIAL",
            "AI_ENGINE"

        ]

        for name in defaults:

            self.sensors[name] = {
                "status": "ONLINE",
                "last_scan": None,
                "events": []
            }

    # ---------------------------------------------------------

    def register_sensor(self, name):

        if name not in self.sensors:

            self.sensors[name] = {
                "status": "ONLINE",
                "last_scan": None,
                "events": []
            }

    # ---------------------------------------------------------

    def set_status(self, name, status):

        if name in self.sensors:

            self.sensors[name]["status"] = status

    # ---------------------------------------------------------

    def add_event(self, sensor, event):

        if sensor not in self.sensors:
            return

        self.sensors[sensor]["events"].append(event)

    # ---------------------------------------------------------

    def scan(self):

        collected = []

        now = datetime.datetime.now()

        for sensor in self.sensors.values():

            sensor["last_scan"] = now

            collected.extend(sensor["events"])

            sensor["events"] = []

        return collected

    # ---------------------------------------------------------

    def dashboard(self):

        print("\n================ SENSORES ================\n")

        for name, sensor in self.sensors.items():

            print(f"{name:20} {sensor['status']}")

        print("\n==========================================\n")


# ============================================================

if __name__ == "__main__":

    manager = SensorManager()

    manager.dashboard()

    manager.add_event(
        "COMMERCIAL_RADAR",
        {
            "tipo": "nova_oportunidade",
            "empresa": "EMPRESA TESTE",
            "prioridade": 8
        }
    )

    eventos = manager.scan()

    print("EVENTOS ENCONTRADOS:\n")

    for evento in eventos:

        print(evento)

