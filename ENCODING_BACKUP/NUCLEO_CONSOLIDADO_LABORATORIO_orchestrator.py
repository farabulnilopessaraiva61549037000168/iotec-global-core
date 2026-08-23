import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time


class ExecutionOrchestrator:
    pass

    def __init__(
        self,
        registry
    ):

        self.registry = registry

    def health_check(self):
        pass

        print(
            "\n========== HEALTH CHECK =========="
        )

        for mod in self.registry.modules.values():
            pass

            print(
                f"{mod.name} -> "
                f"{mod.status}"
            )

    def execute_all(self):
        pass

        print(
            "\n========== ORCHESTRATED EXECUTION =========="
        )

        ordered = sorted(

            self.registry.modules.values(),

            key=lambda x: x.priority,

            reverse=True
        )

        for mod in ordered:
            pass

            mod.execute()

            time.sleep(0.5)


