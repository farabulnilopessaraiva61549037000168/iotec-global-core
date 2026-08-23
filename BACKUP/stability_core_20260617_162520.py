import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# C:\IOTEC\stability_core.py
import ast
from pathlib import Path
import shutil

class StabilityCore:
    pass

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.backup_path = self.file_path.with_suffix(".backup.py")

    def backup(self):
        shutil.copy2(self.file_path, self.backup_path)

    def validate_syntax(self, code: str):
        ast.parse(code)  # se quebrar, levanta SyntaxError

    def safe_load(self):
        return self.file_path.read_text(encoding="utf-8", errors="ignore")

    def repair_brutal(self, code: str):
        """
        Modo de emergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia:
        - remove blocos quebrados
        - evita execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de sintaxe invÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lida
        """
        lines = code.splitlines()
        fixed = []

        skip_block = False

        for line in lines:
            # heurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica simples: remove __init__ quebrado
            if "def __init__(" in line and not line.strip().endswith("):"):
                continue

            fixed.append(line)

        return "\n".join(fixed)

    def run(self):
        self.backup()

        code = self.safe_load()

        try:
            self.validate_syntax(code)
            print("[OK] CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lido")
            return True

        except SyntaxError as e:
            print(f"[CRITICAL] SyntaxError detectado: {e}")

            fixed = self.repair_brutal(code)

            try:
                self.validate_syntax(fixed)
                self.file_path.write_text(fixed, encoding="utf-8")
                print("[OK] CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo reparado automaticamente")
                return True

            except SyntaxError:
                print("[FAIL] ReparaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica nÃƒÆ'Ã†â€™o segura ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â restore backup")
                shutil.copy2(self.backup_path, self.file_path)
                return False


if __name__ == "__main__":
    core = StabilityCore(r"C:\IOTEC\FROZEN\visible_core_router.py")
    core.run()


