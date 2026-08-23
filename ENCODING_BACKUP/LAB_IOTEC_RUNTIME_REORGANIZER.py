import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil

ROOT = r"C:\IOTEC"

LAB = os.path.join(ROOT, "LAB")
LEGACY = os.path.join(ROOT, "LEGACY")
FROZEN = os.path.join(ROOT, "FROZEN")

os.makedirs(LAB, exist_ok=True)
os.makedirs(LEGACY, exist_ok=True)
os.makedirs(FROZEN, exist_ok=True)

dead_keywords = [
    "test",
    "backup",
    "experimental",
    "old",
    "legacy",
    "debug"
]

frozen_modules = [
    "visible_core_router.py",
    "iotec_nucleus.py",
    "IOTEC_CORE_MANAGER.py",
    "IOTEC_ADAPTIVE_CORE_MANAGER.py",
    "IOTEC_BL_PORTAL_PAGAMENTOS_AUTOMATICO.py"
]

print("\n[REORGANIZER] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...\n")

for root, dirs, files in os.walk(ROOT):
    pass

    if any(x in root.lower() for x in [
        "venv",
        "__pycache__",
        "site-packages",
        "node_modules"
    ]):
        continue

    for file in files:
        pass

        if not file.endswith(".py"):
            continue

        path = os.path.join(root, file)

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()

            # =========================
            # FREEZE
            # =========================

            if file in frozen_modules:
                pass

                target = os.path.join(FROZEN, file)

                if not os.path.exists(target):
                    shutil.copy2(path, target)
                    print(f"[FROZEN] {file}")

            # =========================
            # LAB
            # =========================

            elif any(k in content for k in [
                "streamlit",
                "experimental",
                "prototype"
            ]):

                target = os.path.join(LAB, file)

                if not os.path.exists(target):
                    shutil.copy2(path, target)
                    print(f"[LAB] {file}")

            # =========================
            # LEGACY
            # =========================

            elif any(k in file.lower() for k in dead_keywords):
                pass

                target = os.path.join(LEGACY, file)

                if not os.path.exists(target):
                    shutil.copy2(path, target)
                    print(f"[LEGACY] {file}")

        except:
            pass

print("\n===================================")
print(" IOTEC RUNTIME REORGANIZED")
print("===================================")

print(f"\nLAB -> {LAB}")
print(f"LEGACY -> {LEGACY}")
print(f"FROZEN -> {FROZEN}")

# ===================================
# START SCRIPTS
# ===================================

core_ps1 = rf"""
cd {ROOT}
python visible_core_router.py
"""

dashboard_ps1 = rf"""
cd {ROOT}
streamlit run app.py
"""

api_ps1 = rf"""
cd {ROOT}
python -m uvicorn api:app --reload
"""

with open(os.path.join(ROOT, "START_CORE.ps1"), "w") as f:
    f.write(core_ps1)

with open(os.path.join(ROOT, "START_DASHBOARD.ps1"), "w") as f:
    f.write(dashboard_ps1)

with open(os.path.join(ROOT, "START_API.ps1"), "w") as f:
    f.write(api_ps1)

print("\n[OK] START_CORE.ps1 criado")
print("[OK] START_DASHBOARD.ps1 criado")
print("[OK] START_API.ps1 criado")

print("\nSISTEMA ORGANIZADO.")


