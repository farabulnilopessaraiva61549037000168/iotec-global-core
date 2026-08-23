import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==============================================================================
# MODULE LOADER
# ==============================================================================

from importlib import import_module
from dataclasses import dataclass

@dataclass
class ModuleDefinition:

    name: str

    filename: str

    required: bool = True

    loaded: bool = False

    error: str = ""


class ModuleLoader:

    def __init__(self):

        self.modules = [

            ModuleDefinition(
                "ENTERPRISE_COMMAND_CENTER",
                "001_IOTEC_ENTERPRISE_COMMAND_CENTER"
            ),

            ModuleDefinition(
                "X27_CORE",
                "002_X27_CORE"
            ),

            ModuleDefinition(
                "KATSUYO_ENGINE",
                "003_KATSUYO_ENGINE"
            ),

            ModuleDefinition(
                "EVENT_BUS",
                "004_EVENT_BUS"
            ),

            ModuleDefinition(
                "REVENUE_RADAR",
                "005_REVENUE_RADAR"
            ),

            ModuleDefinition(
                "MARKET_HUNTER",
                "006_MARKET_HUNTER"
            ),

            ModuleDefinition(
                "COMMERCIAL_AGENT",
                "007_COMMERCIAL_AGENT"
            ),

            ModuleDefinition(
                "CONTRACT_CENTER",
                "008_CONTRACT_CENTER"
            ),

            ModuleDefinition(
                "FINANCIAL_CENTER",
                "009_FINANCIAL_CENTER"
            ),

            ModuleDefinition(
                "BUDGET_HUNTER",
                "010_BUDGET_HUNTER"
            ),

            ModuleDefinition(
                "CRM_CENTER",
                "011_CRM_CENTER"
            ),

            ModuleDefinition(
                "CONNECTOR_MANAGER",
                "012_CONNECTOR_MANAGER"
            ),

            ModuleDefinition(
                "API_GATEWAY",
                "013_API_GATEWAY"
            ),

            ModuleDefinition(
                "SECURITY_CENTER",
                "014_SECURITY_CENTER"
            ),

            ModuleDefinition(
                "AUDIT_ENGINE",
                "015_AUDIT_ENGINE"
            ),

            ModuleDefinition(
                "ENTERPRISE_KERNEL",
                "016_ENTERPRISE_KERNEL"
            )

        ]

    # ---------------------------------------------------------------------

    def load_all(self):

        print()

        print("=" * 90)

        print("CARREGANDO MÃƒâ€œDULOS")

        print("=" * 90)

        print()

        for module in self.modules:

            try:

                import_module(module.filename)

                module.loaded = True

                print(f"[ OK ] {module.name}")

            except Exception as error:

                module.error = str(error)

                print(f"[FAIL] {module.name}")

                print("       ", error)

        print()

        print("=" * 90)

    # ---------------------------------------------------------------------

    def statistics(self):

        total = len(self.modules)

        loaded = len(

            [

                m

                for m in self.modules

                if m.loaded

            ]

        )

        failed = total - loaded

        return {

            "total": total,

            "loaded": loaded,

            "failed": failed

        }

    # ---------------------------------------------------------------------

    def dashboard(self):

        s = self.statistics()

        print()

        print("=" * 90)

        print("MODULE LOADER")

        print("=" * 90)

        print()

        print("TOTAL........:", s["total"])

        print("ONLINE.......:", s["loaded"])

        print("ERROS........:", s["failed"])

        print()

        print("=" * 90)
# ==============================================================================
# MAIN
# ==============================================================================

def main():

    print()
    print("=" * 90)
    print("INICIANDO IOTEC ENTERPRISE PLATFORM")
    print("=" * 90)

    platform_core = EnterprisePlatform()

    platform_core.banner()

    platform_core.initialize()

    loader = ModuleLoader()

    loader.load_all()

    loader.dashboard()

    platform_core.summary()


if __name__ == "__main__":

    main()





