"""
===============================================================================
008_ARCHITECTURE_ASSIMILATOR.py
Assimilador da Arquitetura da Plataforma IOTEC
===============================================================================
"""

from collections import defaultdict
from pathlib import Path
import re


class ArchitectureAssimilator:

    def __init__(self, root="."):

        self.root = Path(root)

        self.groups = defaultdict(list)

        self.total_modules = 0

    # -------------------------------------------------------------------------

    def classify(self):

        pattern = re.compile(r"^\d{3}_.+\.py$")

        for file in sorted(self.root.glob("*.py")):

            if not pattern.match(file.name):
                continue

            name = file.stem.upper()

            category = self.detect_category(name)

            self.groups[category].append(file.name)

            self.total_modules += 1

    # -------------------------------------------------------------------------

    def detect_category(self, name):

        if "KERNEL" in name or "CORE" in name:
            return "KERNEL"

        if "MISSION" in name:
            return "MISSION"

        if "EVENT" in name:
            return "EVENT"

        if "PRODUCT" in name:
            return "PRODUCT"

        if "COMMERCIAL" in name:
            return "COMMERCIAL"

        if "REVENUE" in name:
            return "REVENUE"

        if "PAYMENT" in name:
            return "PAYMENT"

        if "CLIENT" in name or "CRM" in name:
            return "CLIENT"

        if "DISCOVERY" in name:
            return "DISCOVERY"

        if "CONNECTOR" in name:
            return "CONNECTOR"

        if "DATABASE" in name:
            return "DATABASE"

        if "KNOWLEDGE" in name:
            return "KNOWLEDGE"

        if "INTELLIGENCE" in name:
            return "INTELLIGENCE"

        if "OBSERV" in name:
            return "OBSERVABILITY"

        return "OTHER"

    # -------------------------------------------------------------------------

    def report(self):

        print()

        print("=" * 70)
        print("IOTEC ARCHITECTURE ASSIMILATOR")
        print("=" * 70)

        print()

        print(f"MÃ"DULOS ANALISADOS : {self.total_modules}")

        print()

        for category in sorted(self.groups.keys()):

            modules = self.groups[category]

            print(f"{category:<20} {len(modules):>4}")

        print()

        print("=" * 70)

        print()

        for category in sorted(self.groups.keys()):

            print(f"[ {category} ]")

            for module in self.groups[category]:

                print(f"   â€¢ {module}")

            print()


# =============================================================================

if __name__ == "__main__":

    assimilator = ArchitectureAssimilator()

    assimilator.classify()

    assimilator.report()

