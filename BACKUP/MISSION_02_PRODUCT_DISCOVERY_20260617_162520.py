import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

with open(
    "MISSION_01_CAPABILITY_REPORT.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

print("\n===================================")
print(" PRODUCT DISCOVERY")
print("===================================\n")

for category, info in sorted(
    data.items(),
    key=lambda x: x[1]["total"],
    reverse=True
):

    print(
        f"{category:<20} "
        f"{info['total']:>10}"
    )

print("\n===================================")

top = sorted(
    data.items(),
    key=lambda x: x[1]["total"],
    reverse=True
)[:10]

print("\nTOP CAPABILITIES\n")

for category, info in top:
    pass

    print(
        f"- {category} "
        f"({info['total']})"
    )

print("\n===================================")


