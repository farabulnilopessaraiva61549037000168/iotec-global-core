import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from __future__ import annotations

import os
import sys
import json
from pathlib import Path
from typing import Any, Dict


# =========================================================
# BASE PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[0]
MODULES_DIR = BASE_DIR / "MODULES"
FROZEN_DIR = BASE_DIR / "FROZEN"
CONFIG_PATH = BASE_DIR / "CONFIG" / "iotec_config.json"


# =========================================================
# PYTHONPATH FIX
# =========================================================

if str(MODULES_DIR) not in sys.path:
    sys.path.insert(0, str(MODULES_DIR))


# =========================================================
# SAFE CONFIG LOADER (ANTI-KEYERROR)
# =========================================================

DEFAULT_CONFIG = {
    "paths": {
        "logs_dir": "logs",
        "snapshots_dir": "snapshots"
    },
    "reliability": {
        "minimum_score": 0.5,
        "block_on_untrusted_formula": True
    }
}


def load_safe_config() -> Dict[str, Any]:
    """
    Garante que config nunca quebre o sistema.
    """

    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                config = json.load(f)
        except Exception:
            config = {}
    else:
        config = {}

    # merge seguro
    merged = DEFAULT_CONFIG.copy()

    for k, v in config.items():
        if isinstance(v, dict) and isinstance(merged.get(k), dict):
            merged[k].update(v)
        else:
            merged[k] = v

    return merged


# =========================================================
# SAFE ENVIRONMENT BOOT
# =========================================================

def boot_environment():
    os.environ["PYTHONUTF8"] = "1"
    os.environ["PYTHONPATH"] = str(MODULES_DIR)

    print("[IOTEC] ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ambiente seguro ativado")
    print(f"[IOTEC] ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MODULES: {MODULES_DIR}")
    print(f"[IOTEC] ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â BASE: {BASE_DIR}")


# =========================================================
# SAFE RUNNER
# =========================================================

def run_core():
    """
    Executa visible_core_router sem permitir crash silencioso
    """

    config = load_safe_config()

    target = FROZEN_DIR / "visible_core_router.py"

    if not target.exists():
        print("[ERRO] visible_core_router.py nÃƒÆ'Ã†â€™o encontrado")
        return

    try:
        import runpy

        print("[IOTEC] ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å"Ãƒâ€šÃ‚Â¶ Iniciando core em modo protegido...")
        runpy.run_path(str(target), run_name="__main__")

    except SyntaxError as e:
        print("\n[CRITICAL SYNTAX ERROR]")
        print(e)
        print("\n[SISTEMA BLOQUEADO PARA EVITAR CORRUPÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O]")
        return

    except Exception as e:
        print("\n[ERRO DE EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O]")
        print(str(e))
        return


# =========================================================
# ENTRYPOINT
# =========================================================

if __name__ == "__main__":
    boot_environment()
    run_core()


