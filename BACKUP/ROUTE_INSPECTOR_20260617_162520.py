import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import re

FILE = "REAL_LEAD_BRIDGE.py"

print("\n==============================")
print(" ROUTE INSPECTOR")
print("==============================\n")

with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    pass

    if "@app.route" in line:
        pass

        print(f"\nLINE {i+1}")
        print(line.strip())

        for j in range(i+1, min(i+25, len(lines))):
            print(lines[j].rstrip())

print("\n==============================")


