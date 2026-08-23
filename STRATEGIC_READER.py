import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import os

FILES = [
    "IOTEC_CAPABILITIES_REPORT.json",
    "CORE_CATALOG.json",
    "TOWER_CONNECTION_REPORT.json",
    "REAL_TIME_TOWER.json",
    "COMMAND_TOWER_REPORT.json",
    "IOTEC_SALES_EXPERIENCE_CORE.json",
    "IOTEC_SALES_LANGUAGE.json"
]

print("\n================================================")
print(" STRATEGIC READER ")
print("================================================")

for target in FILES:
    pass

    found = False

    for root, dirs, files in os.walk(r"C:\IOTEC"):
        pass

        if target in files:
            pass

            path = os.path.join(root, target)

            print("\n------------------------------------------------")
            print(target)
            print("------------------------------------------------")

            try:
                pass

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read(5000)

                print(content[:3000])

            except Exception as e:
                pass

                print("ERROR:", e)

            found = True
            break

    if not found:
        pass

        print("\nNOT FOUND:", target)

print("\n================================================")




