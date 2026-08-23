import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import re

FILE = r"C:\IOTEC\FROZEN\visible_core_router.py"

with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# 1. Corrige acesso perigoso a config["paths"]["logs_dir"]
text = text.replace(
    'self.config["paths"]["logs_dir"]',
    'self.config.get("paths", {}).get("logs_dir", "logs")'
)

# 2. Garante paths no config
if "paths" not in text:
    text = text.replace(
        "self.config =",
        "self.config = self.config or {}\n        self.config.setdefault('paths', {})\n        self.config ="
    )

with open(FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("AUTO-FIX concluÃƒÆ'Ã‚Â­do com sucesso")


