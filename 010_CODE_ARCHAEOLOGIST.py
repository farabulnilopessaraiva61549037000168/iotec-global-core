"""
===============================================================================
010_CODE_ARCHAEOLOGIST.py
ArqueÃ³logo de CÃ³digo da Plataforma IOTEC
===============================================================================
"""

from pathlib import Path
import ast
import re


# =============================================================================
# ARQUEÃ"LOGO
# =============================================================================

class CodeArchaeologist:

    def __init__(self, root="."):

        self.root = Path(root)

        self.pattern = re.compile(r"^\d{3}_.+\.py$")

    # -------------------------------------------------------------------------

    def scan(self):

        for file in sorted(self.root.glob("*.py")):

            if not self.pattern.match(file.name):
                continue

            self.inspect(file)

    # -------------------------------------------------------------------------

    def inspect(self, file):

        print("=" * 70)
        print(file.name)
        print("=" * 70)

        try:

            source = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = ast.parse(source)

        except Exception as e:

            print(f"ERRO: {e}")
            print()

            return

        imports = []
        classes = []
        functions = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for item in node.names:

                    imports.append(item.name)

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                imports.append(module)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

        print(f"Imports............. {len(imports)}")
        print(f"Classes............. {len(classes)}")
        print(f"FunÃ§Ãµes............. {len(functions)}")

        print()

        if imports:

            print("IMPORTS")

            for item in sorted(imports):

                print(f"  â€¢ {item}")

            print()

        if classes:

            print("CLASSES")

            for item in classes:

                print(f"  â€¢ {item}")

            print()

        if functions:

            print("FUNÃ‡Ã•ES")

            for item in functions:

                print(f"  â€¢ {item}")

            print()

        print()

# =============================================================================

if __name__ == "__main__":

    archaeologist = CodeArchaeologist()

    archaeologist.scan()

