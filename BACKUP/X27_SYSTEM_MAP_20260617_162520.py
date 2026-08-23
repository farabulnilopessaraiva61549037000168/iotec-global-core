import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 SYSTEM MAP
# ============================================================

from datetime import datetime

print("\n================================================")
print("X27 SYSTEM MAP")
print("================================================")

print(f"DATA : {datetime.now()}")

print("""

COMMAND_CENTER
      |
MISSION_CONTROL
      |
ORCHESTRATOR
      |
EVENT_BUS
      |
OPERATIONAL_DATABASE

----------------------------------------

DIGITAL_TWIN
      |
CAPACITY
      |
DEPENDENCY
      |
PRIORITY
      |
RISK_FORECAST
      |
STRATEGIC_AI

----------------------------------------

PROJECT
      |
PROGRAM
      |
PORTFOLIO
      |
GOVERNANCE

""")

print("================================================")
print("MAPA SISTEMICO DISPONIVEL")
print("================================================")


