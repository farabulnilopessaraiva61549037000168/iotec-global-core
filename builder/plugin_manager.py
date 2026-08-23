import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import traceback
import importlib.util
import inspect
import sys

from pathlib import Path
from datetime import datetime


class PluginManager:

    def __init__(self):

        self.plugins=[]

    # --------------------------------------------------------

    def load_plugin(self,file):

        try:

            spec=importlib.util.spec_from_file_location(

                file.stem,

                file

            )

            module=importlib.util.module_from_spec(spec)

            sys.modules[spec.name]=module

            spec.loader.exec_module(module)

            for name,obj in inspect.getmembers(module):

                if inspect.isclass(obj):

                    if obj.__module__==module.__name__:

                        if name.startswith("_"):

                            continue

                        self.plugins.append({

                            "plugin":name,

                            "module":file.name,

                            "status":"ONLINE"

                        })

            print("[ OK ]",file.name)

        except Exception as e:

            self.plugins.append({

                "plugin":file.name,

                "status":"ERROR",

                "message":str(e),

                "traceback":traceback.format_exc()

            })

            print("[FAIL]",file.name)

    # --------------------------------------------------------

    def execute(self):

        print()

        print("="*70)

        print("PLUGIN MANAGER")

        print("="*70)

        print()

        for file in sorted(

            Path("builder").glob("*.py")

        ):

            if file.name.startswith("__"):

                continue

            self.load_plugin(file)

        Path("reports").mkdir(

            exist_ok=True

        )

        with open(

            "reports/plugins.json",

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

        print("[ OK ] reports/plugins.json")

        print()



