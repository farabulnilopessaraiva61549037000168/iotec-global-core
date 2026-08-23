import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import ast
import shutil

FILE = Path(r"C:\IOTEC\FROZEN\visible_core_router.py")
BACKUP = FILE.with_suffix(".rebuild_backup.py")

def backup():
    shutil.copy2(FILE, BACKUP)
    print(f"[OK] Backup criado: {BACKUP}")

def extract_valid_head(lines):
    """
    MantÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©m apenas imports e constantes iniciais atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© quebrar AST
    """
    buffer = []

    for line in lines:
        buffer.append(line)
        try:
            ast.parse("\n".join(buffer))
        except SyntaxError:
            buffer.pop()
            break

    return buffer

def rebuild_init_safely(text: str):
    """
    Substitui qualquer __init__ quebrado por versÃƒÆ'Ã†â€™o segura mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nima
    """

    safe_init = """
    def __init__(self, config=None, log_path=None):
        self.config = config or {}
        self.config.setdefault("paths", {})
        self.config["paths"].setdefault("logs_dir", "logs")
        self.config["paths"].setdefault("snapshots_dir", "snapshots")
        self.log_path = log_path
"""

    # remove blocos quebrados de __init__
    lines = text.splitlines()
    cleaned = []

    skip = False
    for line in lines:
        if "def __init__" in line:
            skip = True
            cleaned.append(safe_init)
            continue

        if skip:
            if line.startswith("class ") or line.startswith("def ") and "init" not in line:
                skip = False
                cleaned.append(line)
            continue

        cleaned.append(line)

    return "\n".join(cleaned)

def main():
    backup()

    raw = FILE.read_text(encoding="utf-8", errors="ignore")

    lines = raw.splitlines()
    safe_head = extract_valid_head(lines)

    rebuilt = rebuild_init_safely("\n".join(safe_head + lines[len(safe_head):]))

    try:
        ast.parse(rebuilt)
    except Exception as e:
        print("[FALHA] Ainda invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido apÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³s rebuild:")
        print(e)
        return

    FILE.write_text(rebuilt, encoding="utf-8")
    print("[OK] REBUILD COMPLETO COM SUCESSO")

if __name__ == "__main__":
    main()




