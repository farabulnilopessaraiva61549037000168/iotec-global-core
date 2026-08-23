"""
===============================================================================
007_MODULE_DISCOVERY.py
Sensor de Descoberta de MÃ³dulos da Plataforma IOTEC
===============================================================================
"""

from pathlib import Path
from datetime import datetime
import re


class ModuleDiscovery:

    def __init__(self, root_folder="."):

        self.root = Path(root_folder)

        self.modules = []

        self.errors = []

        self.discovery_time = None

    # -------------------------------------------------------------------------

    def discover(self):

        self.modules.clear()

        self.errors.clear()

        self.discovery_time = datetime.now()

        pattern = re.compile(r"^\d{3}_.+\.py$")

        for file in sorted(self.root.glob("*.py")):

            if pattern.match(file.name):

                code = file.name[:3]

                name = file.stem[4:]

                self.modules.append({

                    "code": code,

                    "file": file.name,

                    "name": name,

                    "path": str(file.resolve())

                })

    # -------------------------------------------------------------------------

    def validate_sequence(self):

        if not self.modules:

            return

        codes = sorted(int(m["code"]) for m in self.modules)

        first = codes[0]
        last = codes[-1]

        for expected in range(first, last + 1):

            if expected not in codes:

                self.errors.append(

                    f"MÃ³dulo {expected:03d} nÃ£o encontrado."

                )

    # -------------------------------------------------------------------------

    def report(self):

        print()

        print("=" * 70)
        print("IOTEC MODULE DISCOVERY")
        print("=" * 70)

        print()

        print(f"PASTA............. {self.root.resolve()}")

        print(f"MÃ"DULOS........... {len(self.modules)}")

        print()

        print("MÃ"DULOS LOCALIZADOS")

        for module in self.modules:

            print(

                f"{module['code']}  {module['file']}"

            )

        print()

        if self.errors:

            print("INCONSISTÃŠNCIAS")

            for error in self.errors:

                print(f" â€¢ {error}")

        else:

            print("Nenhuma inconsistÃªncia encontrada.")

        print()

        print("=" * 70)


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    discovery = ModuleDiscovery()

    discovery.discover()

    discovery.validate_sequence()

    discovery.report()

