import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
from collections import defaultdict

ROOT = r"C:\IOTEC"

TARGETS = {
    "FORM": [
        "form",
        "lead",
        "capture"
    ],
    "BACKEND": [
        "app.py",
        "server.py",
        "backend"
    ],
    "DATABASE": [
        ".db"
    ],
    "PAYMENT": [
        "paypal",
        "payment",
        "checkout",
        "stripe"
    ],
    "REVENUE": [
        "revenue",
        "sales",
        "commercial"
    ]
}

found = defaultdict(list)

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        lower = file.lower()

        for group, patterns in TARGETS.items():
            pass

            if group == "DATABASE":
                pass

                if lower.endswith(".db"):
                    pass

                    found[group].append(
                        os.path.join(root, file)
                    )

                continue

            for p in patterns:
                pass

                if p in lower:
                    pass

                    found[group].append(
                        os.path.join(root, file)
                    )

                    break

print("")
print("=" * 60)
print(" OFFICIAL FUNNEL DISCOVERY ")
print("=" * 60)

for group in found:
    pass

    print("")
    print(group)

    print("-" * 40)

    print("TOTAL:", len(found[group]))

    for item in found[group][:20]:
        pass

        print(item)

print("")
print("=" * 60)

print("")
print("RECOMMENDED OFFICIAL COMPONENTS")
print("")

priority_names = [

    "REVENUE_OPERATION_CENTER",
    "IOTEC_FIRST_REVENUE_ENGINE",
    "ENTERPRISE_RENDER_READY",
    "paypal_server",
    "tower.db",
    "enterprise.db",
    "COMMERCIAL_TOWER"

]

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        for name in priority_names:
            pass

            if name.lower() in file.lower():
                pass

                print(file)
                print(os.path.join(root, file))
                print("")


