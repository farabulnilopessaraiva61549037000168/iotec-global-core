import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from core.module import Module
from core.registry import ModuleRegistry


print("\n========================================")

print(" IOTEC SPINE CORE ONLINE")

print("========================================")

registry = ModuleRegistry()

sales = Module(
    "Commercial Intelligence",
    "BUSINESS",
    10,
    "Recurring revenue intelligence"
)

automation = Module(
    "Automation Spine",
    "AUTOMATION",
    9,
    "Global orchestration"
)

registry.register(sales)

registry.register(automation)

registry.show_modules()

print("\n========================================")

print(" IOTEC CORE STABLE")

print("========================================")



