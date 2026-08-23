"""
===============================================================================
009_MODULE_CLASSIFIER.py
Classificador Arquitetural da Plataforma IOTEC
===============================================================================
"""

from pathlib import Path
from collections import defaultdict
import re


# =============================================================================
# CLASSIFICADOR
# =============================================================================

class ModuleClassifier:

    def __init__(self, root="."):

        self.root = Path(root)

        self.categories = defaultdict(list)

        self.rules = {

            "KERNEL": [
                "KERNEL", "CORE"
            ],

            "MISSION": [
                "MISSION", "MISSAO"
            ],

            "EVENT": [
                "EVENT"
            ],

            "OBSERVABILITY": [
                "OBSERV",
                "OBSERVATORY"
            ],

            "COMMERCIAL": [
                "COMMERCIAL",
                "SALE",
                "SALES",
                "MARKETING"
            ],

            "CLIENT": [
                "CLIENT",
                "CRM",
                "LEAD",
                "CONTACT"
            ],

            "PRODUCT": [
                "PRODUCT",
                "PRODUCTION"
            ],

            "REVENUE": [
                "REVENUE",
                "FINANCIAL",
                "PAYMENT",
                "BUDGET"
            ],

            "DATABASE": [
                "DATABASE",
                "DATA"
            ],

            "CONNECTOR": [
                "CONNECTOR",
                "API",
                "GATEWAY"
            ],

            "DISCOVERY": [
                "DISCOVERY",
                "HUNTER",
                "SEARCH",
                "IMPORT"
            ],

            "KNOWLEDGE": [
                "KNOWLEDGE",
                "MEMORY",
                "CATALOG",
                "DOSSIER"
            ],

            "SECURITY": [
                "SECURITY",
                "AUDIT",
                "FORENSIC",
                "GUARD",
                "VALIDATION"
            ],

            "ARCHITECTURE": [
                "ARCHITECTURE",
                "DEPENDENCY",
                "CONSTITUTION",
                "FRAMEWORK"
            ],

            "INTELLIGENCE": [
                "INTELLIGENCE",
                "REASONING",
                "EVIDENCE",
                "CLASSIFIER",
                "GENOME",
                "EVOLUTION"
            ],

            "EXECUTION": [
                "EXECUTION",
                "TASK",
                "WORKFLOW",
                "ORCHESTRATOR",
                "PLANNER",
                "DISPATCH",
                "SCHEDULER"
            ]

        }

    # -------------------------------------------------------------------------

    def classify(self):

        pattern = re.compile(r"^\d{3}_.+\.py$")

        for file in sorted(self.root.glob("*.py")):

            if not pattern.match(file.name):
                continue

            filename = file.stem.upper()

            category = self.detect(filename)

            self.categories[category].append(file.name)

    # -------------------------------------------------------------------------

    def detect(self, filename):

        score = {}

        for category, words in self.rules.items():

            points = 0

            for word in words:

                if word in filename:
                    points += 1

            if points:
                score[category] = points

        if not score:
            return "OTHER"

        return max(score, key=score.get)

    # -------------------------------------------------------------------------

    def report(self):

        print()

        print("=" * 70)
        print("IOTEC MODULE CLASSIFIER")
        print("=" * 70)
        print()

        total = 0

        for category in sorted(self.categories):

            quantity = len(self.categories[category])

            total += quantity

            print(f"{category:<20} {quantity:>5}")

        print()

        print("=" * 70)
        print(f"TOTAL............... {total}")
        print("=" * 70)

        print()

        print("MÃ"DULOS NÃƒO CLASSIFICADOS")

        others = self.categories.get("OTHER", [])

        if not others:

            print("Nenhum.")

        else:

            for module in others:

                print(f" â€¢ {module}")

        print()

    # -------------------------------------------------------------------------

    def statistics(self):

        total = sum(len(x) for x in self.categories.values())

        classified = total - len(self.categories.get("OTHER", []))

        print()

        print("=" * 70)

        print("QUALIDADE DA CLASSIFICAÃ‡ÃƒO")

        print("=" * 70)

        if total == 0:

            print("Nenhum mÃ³dulo encontrado.")

            return

        percentage = (classified / total) * 100

        print(f"MÃ³dulos............. {total}")

        print(f"Classificados....... {classified}")

        print(f"NÃ£o classificados... {total-classified}")

        print(f"Cobertura........... {percentage:.2f}%")

        print()


# =============================================================================
# TESTE
# =============================================================================

if __name__ == "__main__":

    classifier = ModuleClassifier()

    classifier.classify()

    classifier.report()

    classifier.statistics()

