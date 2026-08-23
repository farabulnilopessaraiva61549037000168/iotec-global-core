import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sys
import os

# garante PYTHONPATH
sys.path.insert(0, r"C:\IOTEC\MODULES")

# patch seguro de config padrÃƒÆ'Ã‚Â£o
def ensure_config(config):
    if config is None:
        config = {}

    paths = config.get("paths", {})
    paths.setdefault("logs_dir", "logs")
    paths.setdefault("snapshots_dir", "snapshots")

    config["paths"] = paths
    return config

import builtins
builtins.ensure_config = ensure_config

print("[BOOTSTRAP] Safe mode ativo")


