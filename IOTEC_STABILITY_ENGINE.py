import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
import sys
from pathlib import Path

BASE = Path("C:/IOTEC")
FILE = BASE / "FROZEN/visible_core_router.py"

MODULES = BASE / "MODULES"

def clean_encoding(text: str) -> str:
    return text.replace("\ufeff", "").strip()

def fix_import_path(text: str) -> str:
    if "MODULES" not in text:
        return text

    if "sys.path.insert" not in text:
        injection = (
            "import sys\n"
            f"sys.path.insert(0, r'{MODULES.as_posix()}')\n"
        )
        text = injection + "\n" + text

    return text

def ensure_safe_config(text: str) -> str:
    """
    Injeta fallback seguro SEM quebrar syntax.
    SÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ adiciona helper global.
    """
    if "SAFE_CONFIG_FALLBACK" in text:
        return text

    helper = """

# ===== IOTEC SAFE CONFIG FALLBACK =====
def _safe_config(cfg):
    if not isinstance(cfg, dict):
        cfg = {}
    cfg.setdefault("paths", {})
    cfg["paths"].setdefault("logs_dir", "logs")
    cfg["paths"].setdefault("snapshots_dir", "snapshots")
    return cfg
# ======================================
"""

    return helper + "\n" + text

def validate_syntax(text: str):
    try:
        ast.parse(text)
        return True, None
    except Exception as e:
        return False, str(e)

def write_safe(text: str):
    FILE.write_text(text, encoding="utf-8", errors="ignore")

def main():
    print("[IOTEC] Stability Engine iniciado")

    raw = FILE.read_text(encoding="utf-8", errors="ignore")

    raw = clean_encoding(raw)
    raw = fix_import_path(raw)
    raw = ensure_safe_config(raw)

    ok, err = validate_syntax(raw)

    if not ok:
        print("[BLOQUEADO] Syntax ainda invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido:")
        print(err)
        return

    write_safe(raw)

    print("[OK] Arquivo estabilizado com sucesso")
    print("[OK] Syntax validado")

if __name__ == "__main__":
    main()




