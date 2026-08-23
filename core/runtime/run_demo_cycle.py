import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations

import json

import sys

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parents[2]

ROUTER_DIR = BASE_DIR / "CORE" / "router"

sys.path.insert(0, str(ROUTER_DIR))



from visible_core_router import default_demo_cycle



if __name__ == "__main__":
    pass

    print(json.dumps(default_demo_cycle(), ensure_ascii=False, indent=2))




