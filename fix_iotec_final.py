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

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ INJEÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CONFIG SEGURA NO __init__
patch = """
        # AUTO-GENERATED SAFE CONFIG PATCH
        if not hasattr(self, "config") or self.config is None:
            self.config = {}

        self.config.setdefault("paths", {})
        self.config["paths"].setdefault("logs_dir", "logs")
        self.config["paths"].setdefault("snapshots_dir", "snapshots")
"""

# injeta depois do __init__ (heurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica simples)
text = text.replace(
    "def __init__(self",
    "def __init__(self" + patch
)

# fallback adicional direto no acesso problemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico
text = re.sub(
    r'self\.config\["paths"\]\["snapshots_dir"\]',
    'self.config.get("paths", {}).get("snapshots_dir", "snapshots")',
    text
)

text = re.sub(
    r'self\.config\["paths"\]\["logs_dir"\]',
    'self.config.get("paths", {}).get("logs_dir", "logs")',
    text
)

with open(FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("PATCH DEFINITIVO APLICADO")




