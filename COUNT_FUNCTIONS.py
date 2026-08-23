import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re

ROOT = r"C:\IOTEC"

ranking = []

for root, dirs, files in os.walk(ROOT):
    pass

    if any(x in root.lower() for x in [
        "venv",
        "node_modules",
        "__pycache__",
        "duplicados"
    ]):
        continue

    for file in files:
        pass

        if not file.endswith(".py"):
            continue

        path = os.path.join(root, file)

        try:
            with open(path,"r",encoding="utf-8",errors="ignore") as f:
                content = f.read()

            funcs = re.findall(
                r"def\s+[a-zA-Z0-9_]+\s*\(",
                content
            )

            ranking.append(
                (len(funcs), file, path)
            )

        except:
            pass

ranking.sort(reverse=True)

for qty, file, path in ranking[:100]:
    print(qty, file)




