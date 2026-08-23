Write-Host ""
Write-Host "========================================="
Write-Host " IOTEC AUTO CORE BUILDER"
Write-Host "========================================="
Write-Host ""

Set-Location "C:\IOTEC"

# =====================================================
# STRUCTURE
# =====================================================

$folders = @(
    "core",
    "data",
    "dashboard",
    "backups"
)

foreach ($folder in $folders) {

    if (!(Test-Path $folder)) {

        New-Item `
            -ItemType Directory `
            -Path $folder | Out-Null

        Write-Host "[OK] Folder created: $folder"
    }
}

# =====================================================
# FILES
# =====================================================

$files = @(
    "core\module.py",
    "core\registry.py",
    "core\alignment.py",
    "core\advisor.py",
    "core\perception.py",
    "core\experience.py",
    "core\midas.py",
    "core\concierge.py",
    "core\revenue.py",
    "core\governance.py",
    "core\prospection.py",
    "core\persistence.py",
    "core\orchestrator.py",
    "core\command_center.py",
    "Iotec_Spine_Core.py"
)

foreach ($file in $files) {

    if (!(Test-Path $file)) {

        New-Item `
            -ItemType File `
            -Path $file | Out-Null
    }

    Write-Host "[OK] File ready: $file"
}

# =====================================================
# MODULE.PY
# =====================================================

@'
import uuid
from datetime import datetime


class Module:

    def __init__(
        self,
        name,
        category,
        priority=1,
        description=""
    ):

        self.id = f"MOD-{uuid.uuid4().hex[:8].upper()}"

        self.name = name
        self.category = category
        self.priority = priority
        self.description = description

        self.status = "ACTIVE"

        self.created_at = datetime.now()

    def execute(self):

        print(f"\n[EXECUTION] {self.name}")
        print(f"ID: {self.id}")
        print(f"CATEGORY: {self.category}")
        print(f"STATUS: {self.status}")
        print(f"TIME: {datetime.now()}")
'@ | Set-Content core\module.py

Write-Host "[OK] module.py built"

# =====================================================
# REGISTRY.PY
# =====================================================

@'
class ModuleRegistry:

    def __init__(self):

        self.modules = {}

    def register(self, module):

        self.modules[module.id] = module

        print("\n[REGISTRY]")
        print(f"MODULE REGISTERED: {module.name}")
        print(f"ID: {module.id}")

    def ordered_modules(self):

        return sorted(
            self.modules.values(),
            key=lambda x: x.priority,
            reverse=True
        )

    def show_modules(self):

        print("\n========== ACTIVE MODULES ==========")

        for mod in self.ordered_modules():

            print(
                f"{mod.name} | "
                f"{mod.category} | "
                f"PRIORITY {mod.priority} | "
                f"{mod.status}"
            )
'@ | Set-Content core\registry.py

Write-Host "[OK] registry.py built"

# =====================================================
# MAIN CORE
# =====================================================

@'
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

registry.register(sales)

registry.show_modules()

print("\n========================================")
print(" IOTEC CORE STABLE")
print("========================================")
'@ | Set-Content Iotec_Spine_Core.py

Write-Host "[OK] Iotec_Spine_Core.py built"

# =====================================================
# TEST
# =====================================================

Write-Host ""
Write-Host "========================================="
Write-Host " TESTING CORE"
Write-Host "========================================="
Write-Host ""

python Iotec_Spine_Core.py

Write-Host ""
Write-Host "========================================="
Write-Host " ARCHITECTURE READY"
Write-Host "========================================="