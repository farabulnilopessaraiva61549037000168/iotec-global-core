"""
===============================================================================
IOTEC CORE
Kernel Central da Plataforma IOTEC
VersÃ£o: 1.0
===============================================================================
"""

from datetime import datetime
import time


# =============================================================================
# CONFIGURAÃ‡ÃƒO DO CORE
# =============================================================================

class CoreConfig:

    VERSION = "1.0"

    NAME = "IOTEC CORE"

    AUTHOR = "IOTEC"

    START_TIME = datetime.now()

    DEBUG = True

    STATUS = "INITIALIZING"


# =============================================================================
# REGISTRO DE MÃ"DULOS
# =============================================================================

class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, name, module):

        self.modules[name] = module

        print(f"[REGISTER] {name}")

    def list_modules(self):

        return list(self.modules.keys())


# =============================================================================
# EVENT BUS
# =============================================================================

class EventBus:

    def __init__(self):

        self.events = []

    def publish(self, event):

        self.events.append(event)

        print(f"[EVENT] {event}")

    def consume(self):

        if len(self.events) == 0:

            return None

        return self.events.pop(0)


# =============================================================================
# OBSERVABILIDADE
# =============================================================================

class Observatory:

    def update(self, message):

        now = datetime.now().strftime("%H:%M:%S")

        print(f"[{now}] {message}")


# =============================================================================
# NÃšCLEO
# =============================================================================

class IOTECCore:

    def __init__(self):

        self.registry = ModuleRegistry()

        self.event_bus = EventBus()

        self.observatory = Observatory()

    def boot(self):

        print("=" * 70)

        print("IOTEC CORE")

        print("=" * 70)

        self.observatory.update("Inicializando Kernel...")

        CoreConfig.STATUS = "RUNNING"

        self.event_bus.publish("CORE_STARTED")

    def register_default_modules(self):

        modules = [

            "MISSION_ORCHESTRATOR",

            "KNOWLEDGE_ENGINE",

            "PRODUCT_ENGINE",

            "COMMERCIAL_ENGINE",

            "OBSERVABILITY_ENGINE",

            "EVENT_BUS",

            "PRODUCTION_ENGINE"

        ]

        for module in modules:

            self.registry.register(module, object())

    def run(self):

        self.boot()

        self.register_default_modules()

        self.observatory.update("Sistema operacional.")

        while True:

            event = self.event_bus.consume()

            if event:

                self.observatory.update(f"Processando evento: {event}")

            time.sleep(1)


# =============================================================================
# START
# =============================================================================

if __name__ == "__main__":

    core = IOTECCore()

    core.run()

