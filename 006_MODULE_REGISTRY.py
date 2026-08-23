"""
===============================================================================
006_MODULE_REGISTRY.py
Registro Oficial de MÃ³dulos da Plataforma IOTEC
===============================================================================
"""

from enum import Enum
from datetime import datetime


# =============================================================================
# ENUMERAÃ‡Ã•ES
# =============================================================================

class ModuleStatus(Enum):

    PLANNED = "PLANNED"
    DEVELOPMENT = "DEVELOPMENT"
    READY = "READY"
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"


class ModuleType(Enum):

    CORE = "CORE"
    ENGINE = "ENGINE"
    SERVICE = "SERVICE"
    ENTITY = "ENTITY"
    PANEL = "PANEL"
    INTEGRATION = "INTEGRATION"


# =============================================================================
# MÃ"DULO
# =============================================================================

class Module:

    def __init__(
            self,
            code,
            name,
            module_type,
            mission):

        self.code = code
        self.name = name
        self.module_type = module_type
        self.mission = mission

        self.status = ModuleStatus.READY

        self.dependencies = []

        self.publish_events = []

        self.consume_events = []

        self.integrations = []

        self.last_update = datetime.now()

    # -------------------------------------------------------------------------

    def add_dependency(self, dependency):

        if dependency not in self.dependencies:
            self.dependencies.append(dependency)

    # -------------------------------------------------------------------------

    def add_publish_event(self, event):

        if event not in self.publish_events:
            self.publish_events.append(event)

    # -------------------------------------------------------------------------

    def add_consume_event(self, event):

        if event not in self.consume_events:
            self.consume_events.append(event)

    # -------------------------------------------------------------------------

    def add_integration(self, integration):

        if integration not in self.integrations:
            self.integrations.append(integration)


# =============================================================================
# REGISTRO
# =============================================================================

class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    # -------------------------------------------------------------------------

    def register(self, module):

        self.modules[module.code] = module

        print(f"[REGISTER] {module.code} - {module.name}")

    # -------------------------------------------------------------------------

    def report(self):

        print()
        print("=" * 70)
        print("IOTEC MODULE REGISTRY")
        print("=" * 70)

        for module in self.modules.values():

            print()
            print(f"CÃ"DIGO............. {module.code}")
            print(f"NOME............... {module.name}")
            print(f"TIPO............... {module.module_type.value}")
            print(f"STATUS............. {module.status.value}")
            print(f"MISSÃƒO............. {module.mission}")

            print()

            print("DEPENDÃŠNCIAS")

            if module.dependencies:

                for item in module.dependencies:
                    print(f"  â€¢ {item}")

            else:

                print("  Nenhuma")

            print()

            print("PUBLICA EVENTOS")

            if module.publish_events:

                for item in module.publish_events:
                    print(f"  â€¢ {item}")

            else:

                print("  Nenhum")

            print()

            print("CONSOME EVENTOS")

            if module.consume_events:

                for item in module.consume_events:
                    print(f"  â€¢ {item}")

            else:

                print("  Nenhum")

            print()

            print("INTEGRAÃ‡Ã•ES")

            if module.integrations:

                for item in module.integrations:
                    print(f"  â€¢ {item}")

            else:

                print("  Nenhuma")

            print("-" * 70)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    registry = ModuleRegistry()

    core = Module(

        "000",

        "IOTEC Core",

        ModuleType.CORE,

        "Inicializar e coordenar toda a plataforma."

    )

    core.add_publish_event("CORE_STARTED")

    registry.register(core)

    orchestrator = Module(

        "001",

        "Mission Orchestrator",

        ModuleType.ENGINE,

        "Gerenciar e distribuir missÃµes."

    )

    orchestrator.add_dependency("000")

    orchestrator.add_publish_event("MISSION_CREATED")

    orchestrator.add_publish_event("MISSION_FINISHED")

    registry.register(orchestrator)

    observability = Module(

        "003",

        "Observability Core",

        ModuleType.PANEL,

        "Monitorar toda a operaÃ§Ã£o."

    )

    observability.add_dependency("002")

    observability.add_consume_event("MISSION_CREATED")

    observability.add_consume_event("MISSION_FINISHED")

    registry.register(observability)

    registry.report()

