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
BACKUP = FILE.with_suffix(".STRUCTURE_BACKUP.py")

def backup():
    shutil.copy2(FILE, BACKUP)
    print(f"[OK] Backup criado: {BACKUP}")

def is_valid_block(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except:
        return False

def extract_classes(text: str):
    lines = text.splitlines()
    blocks = []
    current = []
    inside = False

    for line in lines:
        if line.strip().startswith("class "):
            if current:
                blocks.append("\n".join(current))
            current = [line]
            inside = True
        elif inside:
            if line.startswith("class ") and current:
                blocks.append("\n".join(current))
                current = [line]
            else:
                current.append(line)

    if current:
        blocks.append("\n".join(current))

    return blocks

def rebuild(valid_blocks):
    header = """from __future__ import annotations

# AUTO-REBUILT SAFE CORE

"""

    return header + "\n\n".join(valid_blocks)

def main():
    print("[IOTEC] STRUCTURE RECOVERY ENGINE")

    backup()

    raw = FILE.read_text(encoding="utf-8", errors="ignore")

    blocks = extract_classes(raw)

    good_blocks = []

    for b in blocks:
        if is_valid_block(b):
            good_blocks.append(b)
        else:
            print("[SKIP] bloco invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido removido")

    if not good_blocks:
        print("[FAIL] Nenhuma estrutura vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida encontrada")
        return

    new_code = rebuild(good_blocks)

    if is_valid_block(new_code):
        FILE.write_text(new_code, encoding="utf-8")
        print("[OK] REBUILD estrutural concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do com seguranÃƒÆ'Ã†â€™a")
    else:
        print("[FAIL] reconstruÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ainda invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â rollback necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio")

if __name__ == "__main__":
    main()


