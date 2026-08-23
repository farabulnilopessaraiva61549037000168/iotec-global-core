"""
===============================================================================
011_ARCHITECTURE_KNOWLEDGE_BASE.py
IOTEC Architecture Knowledge Base
===============================================================================
"""

from pathlib import Path
import ast
import sqlite3
import re

DB = "iotec_architecture.db"


class ArchitectureKnowledgeBase:

    def __init__(self, root="."):

        self.root = Path(root)

        self.pattern = re.compile(r"^\d{3}_.+\.py$")

        self.db = sqlite3.connect(DB, timeout=30)

        self.cursor = self.db.cursor()

        self.create_tables()

    # ------------------------------------------------------------------

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS modules(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT UNIQUE,

            classes INTEGER,

            functions INTEGER,

            imports INTEGER,

            status TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS module_imports(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            imported_module TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS module_classes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            class_name TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS module_functions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            function_name TEXT

        )

        """)

        self.db.commit()

    # ------------------------------------------------------------------

    def clear(self):

        self.cursor.execute("DELETE FROM modules")

        self.cursor.execute("DELETE FROM module_imports")

        self.cursor.execute("DELETE FROM module_classes")

        self.cursor.execute("DELETE FROM module_functions")

        self.db.commit()

    # ------------------------------------------------------------------

    def analyze(self):

        self.clear()

        for file in sorted(self.root.glob("*.py")):

            if not self.pattern.match(file.name):
                continue

            self.process(file)

    # ------------------------------------------------------------------

    def process(self, file):

        try:

            source = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = ast.parse(source)

            imports = []
            classes = []
            functions = []

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for item in node.names:
                        imports.append(item.name)

                elif isinstance(node, ast.ImportFrom):

                    imports.append(node.module or "")

                elif isinstance(node, ast.ClassDef):

                    classes.append(node.name)

                elif isinstance(node, ast.FunctionDef):

                    functions.append(node.name)

            self.cursor.execute("""

            INSERT OR REPLACE INTO modules(

                filename,
                classes,
                functions,
                imports,
                status

            )

            VALUES(?,?,?,?,?)

            """, (

                file.name,

                len(classes),

                len(functions),

                len(imports),

                "OK"

            ))

            for item in imports:

                self.cursor.execute("""

                INSERT INTO module_imports

                VALUES(NULL,?,?)

                """,(file.name,item))

            for item in classes:

                self.cursor.execute("""

                INSERT INTO module_classes

                VALUES(NULL,?,?)

                """,(file.name,item))

            for item in functions:

                self.cursor.execute("""

                INSERT INTO module_functions

                VALUES(NULL,?,?)

                """,(file.name,item))

        except Exception:

            self.cursor.execute("""

            INSERT OR REPLACE INTO modules(

                filename,
                classes,
                functions,
                imports,
                status

            )

            VALUES(?,?,?,?,?)

            """,(

                file.name,
                0,
                0,
                0,
                "ERROR"

            ))

        self.db.commit()

    # ------------------------------------------------------------------

    def dashboard(self):

        print()
        print("="*70)
        print("ARCHITECTURE KNOWLEDGE BASE")
        print("="*70)
        print()

        total=self.cursor.execute(

            "SELECT COUNT(*) FROM modules"

        ).fetchone()[0]

        ok=self.cursor.execute(

            "SELECT COUNT(*) FROM modules WHERE status='OK'"

        ).fetchone()[0]

        errors=self.cursor.execute(

            "SELECT COUNT(*) FROM modules WHERE status='ERROR'"

        ).fetchone()[0]

        imports=self.cursor.execute(

            "SELECT COUNT(*) FROM module_imports"

        ).fetchone()[0]

        classes=self.cursor.execute(

            "SELECT COUNT(*) FROM module_classes"

        ).fetchone()[0]

        functions=self.cursor.execute(

            "SELECT COUNT(*) FROM module_functions"

        ).fetchone()[0]

        print(f"MÃ³dulos........... {total}")
        print(f"Analisados........ {ok}")
        print(f"Com erro.......... {errors}")
        print(f"Imports........... {imports}")
        print(f"Classes........... {classes}")
        print(f"FunÃ§Ãµes........... {functions}")

        print()

        print("MÃ"DULOS COM ERRO")

        print("-"*70)

        for row in self.cursor.execute("""

            SELECT filename

            FROM modules

            WHERE status='ERROR'

            ORDER BY filename

        """):

            print(" â€¢",row[0])

        print()

    # ------------------------------------------------------------------

    def close(self):

        self.db.close()


# =============================================================================

if __name__=="__main__":

    kb=ArchitectureKnowledgeBase()

    kb.analyze()

    kb.dashboard()

    kb.close()

