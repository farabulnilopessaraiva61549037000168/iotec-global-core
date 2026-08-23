import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import runpy
import sys

sys.path.insert(0, r"C:\IOTEC\MODULES")

print("[IOTEC] iniciando visible_core_router em modo seguro...")

runpy.run_path(r"C:\IOTEC\FROZEN\visible_core_router.py", run_name="__main__")



