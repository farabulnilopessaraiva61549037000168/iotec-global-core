import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

ENV_FILE = r"C:\IOTEC\X27_SECRETS.env"

configs = {}

if os.path.exists(ENV_FILE):

    with open(
        ENV_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if "=" in line:

                k, v = line.split("=", 1)

                configs[k.strip()] = v.strip()

print("=" * 70)
print("X27 INTEGRATION CORE")
print("=" * 70)

for k, v in configs.items():

    status = "ONLINE" if v else "OFFLINE"

    print(f"{k:30} {status}")

print()
print("INTEGRATION CORE READY")



