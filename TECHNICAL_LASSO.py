"""
=========================================================
IOTEC - TECHNICAL LASSO
=========================================================
Controla o estado do LaÃƒÂ§o TÃƒÂ©cnico do Primeiro PavilhÃƒÂ£o.
=========================================================
"""

from datetime import datetime


class TechnicalLasso:

    def __init__(self):

        self.state = "ATIVO"
        self.created_at = datetime.now()
        self.released_at = None

    # -----------------------------------------------------

    def is_active(self):

        return self.state == "ATIVO"

    # -----------------------------------------------------

    def release(self):

        if self.state == "LIBERADO":
            return

        self.state = "LIBERADO"
        self.released_at = datetime.now()

    # -----------------------------------------------------

    def lock(self):

        self.state = "ATIVO"
        self.released_at = None

    # -----------------------------------------------------

    def report(self):

        print("\n===================================")
        print("TECHNICAL LASSO")
        print("===================================")
        print(f"Estado      : {self.state}")
        print(f"Criado em   : {self.created_at}")

        if self.released_at:
            print(f"Liberado em : {self.released_at}")
        else:
            print("Liberado em : ---")

        print("===================================\n")


if __name__ == "__main__":

    lasso = TechnicalLasso()

    print("SituaÃƒÂ§ÃƒÂ£o Inicial")
    lasso.report()

    print("Liberando LaÃƒÂ§o TÃƒÂ©cnico...\n")

    lasso.release()

    lasso.report()

