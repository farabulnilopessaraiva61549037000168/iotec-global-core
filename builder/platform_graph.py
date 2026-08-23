import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

class PlatformGraphEngine:

    def __init__(self):

        self.registry_file = Path("reports/module_registry.json")

        self.dependencies_file = Path("reports/dependencies.json")

    # -----------------------------------------------------

    def execute(self):

        if not self.registry_file.exists():

            print("[ERRO] module_registry.json inexistente.")

            return

        if not self.dependencies_file.exists():

            print("[ERRO] dependencies.json inexistente.")

            return

        with open(

            self.registry_file,

            "r",

            encoding="utf-8"

        ) as f:

            registry=json.load(f)

        with open(

            self.dependencies_file,

            "r",

            encoding="utf-8"

        ) as f:

            dependencies=json.load(f)

        modules=[]

        for item in registry["modules"]:

            name=item["name"]

            modules.append({

                "module":name,

                "imports":dependencies["modules"].get(name,[]),

                "status":item["status"]

            })

        graph={

            "generated_at":str(datetime.now()),

            "total_modules":len(modules),

            "modules":modules

        }

        Path("reports").mkdir(exist_ok=True)

        with open(

            "reports/platform_graph.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                graph,

                f,

                indent=4,

                ensure_ascii=False

            )

        with open(

            "reports/platform_map.txt",

            "w",

            encoding="utf-8"

        ) as txt:

            txt.write("="*70+"\n")

            txt.write("IOTEC PLATFORM MAP\n")

            txt.write("="*70+"\n\n")

            for module in modules:

                txt.write(module["module"]+"\n")

                for dep in module["imports"]:

                    txt.write("   â""â"€â"€ "+dep+"\n")

                txt.write("\n")

        print()

        print("[GRAPH] platform_graph.json criado.")

        print("[GRAPH] platform_map.txt criado.")



