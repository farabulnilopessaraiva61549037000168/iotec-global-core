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
BACKUP = FILE.with_suffix(".PREPARSER_BACKUP.py")

def backup():
    shutil.copy2(FILE, BACKUP)
    print(f"[OK] Backup criado: {BACKUP}")

def fix_missing_colons(text: str) -> str:
    # adiciona ":" em def/class quebrado (heurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica segura)
    text = re.sub(r"^\s*(def .+)\)\s*$", r"\1):", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*(class .+)\s*$", r"\1:", text, flags=re.MULTILINE)
    return text

def fix_unbalanced_parentheses(text: str) -> str:
    open_p = text.count("(")
    close_p = text.count(")")
    if open_p > close_p:
        text += ")" * (open_p - close_p)
    return text

def fix_tabs(text: str) -> str:
    return text.replace("\t", "    ")

def main():
    print("[IOTEC] PREPARSER iniciado")

    backup()

    text = FILE.read_text(encoding="utf-8", errors="ignore")

    original = text

    text = fix_tabs(text)
    text = fix_missing_colons(text)
    text = fix_unbalanced_parentheses(text)

    if text == original:
        print("[INFO] Nenhuma correÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o aplicada")
    else:
        FILE.write_text(text, encoding="utf-8")
        print("[OK] PrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©-correÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes aplicadas")

    print("[DONE] PREPARSER finalizado")

if __name__ == "__main__":
    main()




