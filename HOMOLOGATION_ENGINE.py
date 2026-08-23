"""
=========================================================
IOTEC - HOMOLOGATION ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
ResponsÃƒÂ¡vel por verificar se todos os requisitos foram
cumpridos antes da liberaÃƒÂ§ÃƒÂ£o do Primeiro PavilhÃƒÂ£o.
=========================================================
"""

from datetime import datetime


class HomologationEngine:

    def __init__(self):

        self.started_at = datetime.now()

        self.requirements = {

            "SYSTEM_HEALTH": False,
            "TECHNICAL_LASSO": False,
            "TECHNICAL_REPORT": False,
            "BILLING": False,
            "PAYMENT": False,
            "CASHBOX": False

        }

    # ----------------------------------------------------

    def approve(self, item):

        if item in self.requirements:
            self.requirements[item] = True

    # ----------------------------------------------------

    def percentage(self):

        total = len(self.requirements)
        approved = sum(self.requirements.values())

        return round((approved / total) * 100, 2)

    # ----------------------------------------------------

    def ready(self):

        return all(self.requirements.values())

    # ----------------------------------------------------

    def report(self):

        print("\n========================================")
        print("HOMOLOGATION REPORT")
        print("========================================")

        for item, status in self.requirements.items():

            state = "OK" if status else "PENDENTE"

            print(f"{item:<25}{state}")

        print("----------------------------------------")
        print(f"CONCLUSÃƒÆ'O : {self.percentage()}%")

        if self.ready():
            print("STATUS    : APROVADO")
        else:
            print("STATUS    : AGUARDANDO")

        print("========================================\n")


# ======================================================

if __name__ == "__main__":

    engine = HomologationEngine()

    engine.approve("SYSTEM_HEALTH")
    engine.approve("TECHNICAL_LASSO")

    engine.report()

    print("Aprovando os demais requisitos...\n")

    engine.approve("TECHNICAL_REPORT")
    engine.approve("BILLING")
    engine.approve("PAYMENT")
    engine.approve("CASHBOX")

    engine.report()

