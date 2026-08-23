import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

with open(
    "MISSION_03_MASTER_INVENTORY.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

print("\n================================")
print(" FORMS FOUND")
print("================================\n")

for i, form in enumerate(data["forms"], 1):
    pass

    print(f"{i:02d} - {form}")

print("\n================================")


