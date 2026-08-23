import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
from pathlib import Path
import shutil

TARGET = Path(r"C:\IOTEC\FROZEN\visible_core_router.py")
BACKUP = TARGET.with_suffix(".backup.py")

def backup():
    shutil.copy2(TARGET, BACKUP)
    print(f"[OK] Backup criado: {BACKUP}")

def remove_bom(text: str) -> str:
    return text.lstrip("\ufeff")

def safe_parse(text: str):
    try:
        return ast.parse(text)
    except SyntaxError as e:
        print(f"[ERROR] SyntaxError detectado: {e}")
        return None

def fix_common_config_patterns(text: str) -> str:
    # PATCH SEGURO: garante config padrÃƒÆ'Ã†â€™o sem quebrar sintaxe
    if "self.config.setdefault" not in text:
        patch = """
        if getattr(self, "config", None) is None:
            self.config = {}

        self.config.setdefault("paths", {})
        self.config["paths"].setdefault("logs_dir", "logs")
        self.config["paths"].setdefault("snapshots_dir", "snapshots")
"""
        text = text.replace("def __init__", "def __init__\n" + patch)
    return text

def main():
    backup()

    text = TARGET.read_text(encoding="utf-8", errors="ignore")

    text = remove_bom(text)
    text = fix_common_config_patterns(text)

    if safe_parse(text) is None:
        print("[FAIL] Ainda invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â abortando escrita")
        return

    TARGET.write_text(text, encoding="utf-8")
    print("[OK] ReparaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o aplicada com AST vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida")

if __name__ == "__main__":
    main()


