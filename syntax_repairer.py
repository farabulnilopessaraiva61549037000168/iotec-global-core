import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import re
import shutil

FILE = Path(r"C:\IOTEC\FROZEN\visible_core_router.py")
BACKUP = FILE.with_suffix(".backup.py")

def backup():
    shutil.copy(FILE, BACKUP)
    print("[OK] Backup criado:", BACKUP)

def fix_constructor(text: str) -> str:
    """
    Corrige especificamente erros de __init__ quebrado
    """

    # remove inserÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lidas dentro da assinatura
    text = re.sub(
        r"def __init__\(self\s*\n\s*#.*?\n",
        "def __init__(self, config: dict, log_path=None) -> None:\n",
        text,
        flags=re.DOTALL
    )

    # garante corpo mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nimo vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido
    text = re.sub(
        r"(def __init__.*?:)\s*\n",
        r"\1\n        self.config = config or {}\n        self.log_path = log_path\n",
        text
    )

    return text

def main():
    if not FILE.exists():
        print("[ERRO] Arquivo nÃƒÆ'Ã†â€™o encontrado")
        return

    backup()

    text = FILE.read_text(encoding="utf-8", errors="ignore")

    fixed = fix_constructor(text)

    FILE.write_text(fixed, encoding="utf-8")

    print("[OK] ReparaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o estrutural aplicada")

if __name__ == "__main__":
    main()




