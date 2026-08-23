import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
import json
from pathlib import Path
from datetime import datetime

class DependencyAnalyzer:

    def __init__(self):

        self.dependencies = {}

    # -----------------------------------------------------

    def analyze_file(self,file):

        imports=[]

        try:

            tree=ast.parse(

                Path(file).read_text(

                    encoding="utf-8",

                    errors="ignore"

                )

            )

            for node in ast.walk(tree):

                if isinstance(node,ast.Import):

                    for name in node.names:

                        imports.append(name.name)

                elif isinstance(node,ast.ImportFrom):

                    if node.module:

                        imports.append(node.module)

        except Exception as e:

            imports.append(f"ERROR: {e}")

        return sorted(set(imports))

    # -----------------------------------------------------

    def execute(self):

        print()

        print("="*70)
        print("DEPENDENCY ANALYZER")
        print("="*70)

        for file in sorted(Path(".").glob("*.py")):

            if file.name.startswith("0"):

                self.dependencies[file.name]=self.analyze_file(file)

                print("[ OK ]",file.name)

        Path("reports").mkdir(exist_ok=True)

        report={

            "generated_at":str(datetime.now()),

            "modules":self.dependencies

        }

        with open(

            "reports/dependencies.json",

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

        print("[ OK ] reports/dependencies.json")



