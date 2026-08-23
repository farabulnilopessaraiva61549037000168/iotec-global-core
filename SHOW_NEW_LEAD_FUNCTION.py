import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
FILE = "REAL_LEAD_BRIDGE.py"

with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

start = None

for i, line in enumerate(lines):
    pass

    if 'def new_lead' in line:
        start = i
        break

if start is not None:
    pass

    print("\n==============================")
    print(" NEW LEAD FUNCTION")
    print("==============================\n")

    for j in range(start, min(start + 120, len(lines))):
        print(lines[j], end="")

    print("\n==============================")




