import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import importlib
import inspect
import pkgutil
import json

from pathlib import Path
from datetime import datetime


class PluginLoader:

    def __init__(self):

        self.plugins=[]

    # -------------------------------------------------------

    def execute(self):

        print()
        print("="*70)
        print("AUTO PLUGIN LOADER")
        print("="*70)
        print()

        import builder

        for module in pkgutil.iter_modules(builder.__path__):

            if module.name.startswith("__"):
                continue

            try:

                m = importlib.import_module(
                    f"builder.{module.name}"
                )

                classes=[]

                for name,obj in inspect.getmembers(m):

                    if inspect.isclass(obj):

                        if obj.__module__==m.__name__:

                            classes.append(name)

                self.plugins.append({

                    "module":module.name,

                    "classes":classes,

                    "status":"ONLINE"

                })

                print("[ OK ]",module.name)

            except Exception as e:

                self.plugins.append({

                    "module":module.name,

                    "status":"ERROR",

                    "message":str(e)

                })

                print("[FAIL]",module.name)

        Path("reports").mkdir(exist_ok=True)

        with open(

            "reports/plugin_loader.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                {

                    "generated_at":str(datetime.now()),

                    "plugins":self.plugins

                },

                f,

                indent=4,

                ensure_ascii=False

            )

        print()
        print("[ OK ] reports/plugin_loader.json")
        print()



