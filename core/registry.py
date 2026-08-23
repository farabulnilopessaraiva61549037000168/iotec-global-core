import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, module):

        self.modules[module.id] = module

        print("\n[REGISTRY]")
        print(f"MODULE REGISTERED: {module.name}")
        print(f"ID: {module.id}")

    def ordered_modules(self):

        return sorted(
            self.modules.values(),
            key=lambda x: x.priority,
            reverse=True
        )

    def show_modules(self):

        print("\n========== ACTIVE MODULES ==========")

        for mod in self.ordered_modules():

            print(
                f"{mod.name} | "
                f"{mod.category} | "
                f"PRIORITY {mod.priority} | "
                f"{mod.status}"
            )


