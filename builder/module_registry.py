import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

class ModuleRegistry:

    def __init__(self):

        self.modules = []

    # --------------------------------------------------------

    def scan(self):

        for file in sorted(Path(".").glob("*.py")):

            if file.name.startswith("0"):

                self.modules.append({

                    "name": file.name,

                    "status": "ONLINE"

                })

    # --------------------------------------------------------

    def save(self):

        Path("reports").mkdir(exist_ok=True)

        registry = {

            "generated_at": str(datetime.now()),

            "total_modules": len(self.modules),

            "modules": self.modules

        }

        with open(

            "reports/module_registry.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                registry,

                f,

                indent=4,

                ensure_ascii=False

            )

        print("[REGISTRY] module_registry.json criado.")

    # --------------------------------------------------------

    def execute(self):

        self.scan()

        self.save()



