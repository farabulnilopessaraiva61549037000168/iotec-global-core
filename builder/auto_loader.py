import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import importlib.util
import sys
from pathlib import Path
from datetime import datetime

class AutoLoader:

    def __init__(self):

        self.results=[]

    # ----------------------------------------------------------

    def load_module(self,file):

        try:

            spec = importlib.util.spec_from_file_location(

                file.stem,

                file

            )

            module = importlib.util.module_from_spec(spec)

            sys.modules[spec.name] = module

            spec.loader.exec_module(module)

            status="LOADED"

            executed=False

            if hasattr(module,"Module"):

                obj=module.Module()

                if hasattr(obj,"execute"):

                    obj.execute()

                    executed=True

            self.results.append({

                "module":file.name,

                "status":status,

                "executed":executed

            })

            print("[ OK ]",file.name)

        except Exception as e:

            self.results.append({

                "module":file.name,

                "status":"ERROR",

                "error":str(e)

            })

            print("[FAIL]",file.name)

            print("      ",e)

    # ----------------------------------------------------------

    def execute(self):

        print()

        print("="*70)

        print("AUTO LOADER")

        print("="*70)

        print()

        for file in sorted(Path(".").glob("[0-9][0-9][0-9]_*.py")):

            self.load_module(file)

        Path("reports").mkdir(exist_ok=True)

        report={

            "generated_at":str(datetime.now()),

            "modules":self.results

        }

        with open(

            "reports/module_status.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                report,

                f,

                indent=4,

                ensure_ascii=False

            )

        print()

        print("[ OK ] reports/module_status.json")

        print()



