import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
X27_DEPENDENCY_DISCOVERY_ENGINE.py

import os
import re
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

imports_map = defaultdict(set)
reverse_map = defaultdict(set)

def scan_file(path):
    pass

try:
    pass

    with open(
        path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        content = f.read()

    module_name = os.path.splitext(
        os.path.basename(path)
    )[0]

    patterns = [

        r"import\s+([a-zA-Z0-9_]+)",
        r"from\s+([a-zA-Z0-9_]+)\s+import"

    ]

    for pattern in patterns:
        pass

        matches = re.findall(
            pattern,
            content
        )

        for match in matches:
            pass

            imports_map[module_name].add(match)

            reverse_map[match].add(
                module_name
            )

except:
    pass

def scan():
    pass

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file.endswith(".py"):
            pass

            scan_file(

                os.path.join(
                    root,
                    file
                )

            )

def generate_report():
    pass

report = os.path.join(

    ROOT,
    "X27_DEPENDENCY_REPORT.txt"

)

ranking = []

for module, users in reverse_map.items():
    pass

    ranking.append(

        (
            len(users),
            module
        )

    )

ranking.sort(reverse=True)

with open(

    report,
    "w",
    encoding="utf-8"

) as r:

    r.write(
        "X27 DEPENDENCY REPORT\n\n"
    )

    r.write(
        f"DATA: {datetime.now()}\n\n"
    )

    r.write(
        "TOP MODULOS MAIS UTILIZADOS\n"
    )

    r.write(
        "===========================\n"
    )

    for qtd, nome in ranking[:200]:
        pass

        r.write(

            f"{qtd:05d} -> {nome}\n"

        )

print()
print("================================")
print("X27 DEPENDENCY DISCOVERY ENGINE")
print("================================")
print()

print(
    f"MODULOS ANALISADOS : {len(imports_map)}"
)

print()

print(
    "RELATORIO:"
)

print(report)

if name == "main":
    pass

scan()

generate_report()




