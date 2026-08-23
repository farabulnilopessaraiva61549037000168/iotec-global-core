import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC AUTOPILOT ENGINE
# TORRE AUTONOMA
# ==========================================================

import subprocess
from datetime import datetime

ENGINES = [

    (
        "EVENT ROUTER",
        r"C:\IOTEC\IOTEC_EVENT_ROUTER.py"
    ),

    (
        "EVENT CONSUMER",
        r"C:\IOTEC\IOTEC_EVENT_CONSUMER.py"
    ),

    (
        "AUTONOMOUS MISSION",
        r"C:\IOTEC\IOTEC_AUTONOMOUS_MISSION_ENGINE.py"
    ),

    (
        "MISSION CYCLE",
        r"C:\IOTEC\IOTEC_MISSION_CYCLE_ENGINE.py"
    ),

    (
        "EXECUTIVE COCKPIT",
        r"C:\IOTEC\IOTEC_EXECUTIVE_COCKPIT.py"
    ),

    (
        "CYCLE AUDITOR",
        r"C:\IOTEC\IOTEC_CYCLE_AUDITOR.py"
    )

]

print("")
print("===================================")
print("IOTEC AUTOPILOT ENGINE")
print("===================================")

print("")
print(
    "START:",
    datetime.now()
)

executed = 0

for name, file in ENGINES:
    pass

    print("")
    print("-----------------------------------")
    print(name)
    print("-----------------------------------")

    try:
        pass

        result = subprocess.run(

            ["python", file],

            capture_output=True,
            text=True

        )

        print(result.stdout)

        if result.stderr:
            pass

            print("ERRO:")
            print(result.stderr)

        executed += 1

    except Exception as e:
        pass

        print(
            f"FALHA: {e}"
        )

print("")
print("===================================")

print(
    "ENGINES EXECUTADOS:",
    executed
)

print(
    "END:",
    datetime.now()
)

print("===================================")
print("")
print("CONCLUIDO")




