import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class ModuleRegistry:
    pass

    def __init__(self):
        pass

        self.modules = {}

    def register(self, module):
        pass

        self.modules[module.id] = module

        print("\n[REGISTRY]")

        print(
            f"MODULE REGISTERED: "
            f"{module.name}"
        )

        print(f"ID: {module.id}")

    def ordered_modules(self):
        pass

        return sorted(
            self.modules.values(),
            key=lambda x: x.priority,
            reverse=True
        )

    def show_modules(self):
        pass

        print(
            "\n========== ACTIVE MODULES =========="
        )

        for mod in self.ordered_modules():
            pass

            print(
                f"{mod.name} | "
                f"{mod.category} | "
                f"PRIORITY {mod.priority} | "
                f"{mod.status}"
            )



