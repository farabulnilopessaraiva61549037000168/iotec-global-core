import os
import json
import hashlib
from pathlib import Path
from datetime import datetime


class ProjectScanner:

    def __init__(self, root):

        self.root = Path(root)

        self.database = {
            "generated_at": str(datetime.now()),
            "root": str(self.root),
            "files": [],
            "summary": {}
        }

    # -----------------------------------------------------

    def sha256(self, file):

        h = hashlib.sha256()

        try:

            with open(file, "rb") as f:

                while True:

                    chunk = f.read(8192)

                    if not chunk:
                        break

                    h.update(chunk)

            return h.hexdigest()

        except:

            return ""

    # -----------------------------------------------------

    def scan(self):

        counters = {}

        for path in self.root.rglob("*"):

            if not path.is_file():
                continue

            ext = path.suffix.lower()

            counters.setdefault(ext, 0)

            counters[ext] += 1

            try:

                size = path.stat().st_size

            except:

                size = 0

            item = {

                "name": path.name,

                "extension": ext,

                "path": str(path),

                "size": size,

                "hash": self.sha256(path)

            }

            self.database["files"].append(item)

        self.database["summary"] = counters

    # -----------------------------------------------------

    def save(self):

        out = self.root / "enterprise" / "builder"

        out.mkdir(parents=True, exist_ok=True)

        file = out / "project_inventory.json"

        with open(file, "w", encoding="utf-8") as f:

            json.dump(

                self.database,

                f,

                indent=4,

                ensure_ascii=False

            )

        return file


if __name__ == "__main__":

    ROOT = r"C:\IOTEC"

    scanner = ProjectScanner(ROOT)

    scanner.scan()

    file = scanner.save()

    print("=" * 70)
    print("IOTEC ENTERPRISE BUILDER")
    print("=" * 70)
    print()
    print("Arquivos:", len(scanner.database["files"]))
    print()
    print("InventÃƒÂ¡rio salvo em:")
    print(file)

