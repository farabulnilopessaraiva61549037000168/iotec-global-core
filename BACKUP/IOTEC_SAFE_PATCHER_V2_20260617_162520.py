import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
import shutil
from pathlib import Path

TARGET = Path(r"C:\IOTEC\FROZEN\visible_core_router.py")
BACKUP = TARGET.with_suffix(".SAFE_BACKUP.py")

REQUIRED_METHODS = [
    "dispatch"
]

def backup():
    shutil.copy2(TARGET, BACKUP)
    print(f"[OK] Backup criado: {BACKUP}")

def load():
    return TARGET.read_text(encoding="utf-8", errors="ignore")

def save(content: str):
    TARGET.write_text(content, encoding="utf-8")
    print("[OK] Arquivo atualizado com seguranÃƒÆ'Ã†â€™a")

def parse_ast(content: str):
    try:
        return ast.parse(content)
    except SyntaxError as e:
        print(f"[CRITICAL] SyntaxError detectado: {e}")
        return None

def get_class_methods(tree):
    methods = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods.add(item.name)

    return methods

def inject_dispatch(content: str) -> str:
    if "def dispatch" in content:
        return content

    patch = """

    def dispatch(self, payload: dict):
        """AUTO-GENERATED SAFE FALLBACK"""
        return {
            "status": "fallback",
            "input": payload,
            "message": "dispatch ausente ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â modo seguro ativo"
        }

"""

    # injeta dentro da primeira classe
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("class "):
            lines.insert(i + 1, patch)
            break

    return "\n".join(lines)

def ensure_config_safety(content: str) -> str:
    if "self.config" not in content:
        return content

    patch = """
        if getattr(self, "config", None) is None:
            self.config = {}

        self.config.setdefault("paths", {})
        self.config["paths"].setdefault("logs_dir", "logs")
        self.config["paths"].setdefault("snapshots_dir", "snapshots")
"""

    return content.replace("def __init__", f"def __init__{patch}")

def main():
    print("[IOTEC] SAFE PATCHER V2 iniciado")

    backup()

    content = load()

    tree = parse_ast(content)
    if tree is None:
        print("[ABORT] CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo nÃƒÆ'Ã†â€™o ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â restore necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio")
        return

    methods = get_class_methods(tree)

    print(f"[INFO] mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©todos encontrados: {methods}")

    # garante dispatch
    if "dispatch" not in methods:
        print("[PATCH] adicionando dispatch fallback")
        content = inject_dispatch(content)

    # injeta proteÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o config
    content = ensure_config_safety(content)

    # valida novamente
    if parse_ast(content) is None:
        print("[FAIL] Patch gerou erro ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â restaurando backup")
        TARGET.write_text(BACKUP.read_text(encoding="utf-8"))
        return

    save(content)

    print("[OK] PATCH FINALIZADO COM VALIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O AST")

if __name__ == "__main__":
    main()


