"""
=========================================================
IOTEC - TECHNICAL REPORT ENGINE
Primeiro PavilhÃƒÂ£o
=========================================================
Gera o RelatÃƒÂ³rio TÃƒÂ©cnico Oficial.
=========================================================
"""

from datetime import datetime


class TechnicalReportEngine:

    def __init__(self):

        self.report = {
            "PavilhÃƒÂ£o": "Primeiro PavilhÃƒÂ£o",
            "VersÃƒÂ£o": "1.0",
            "Data": datetime.now(),
            "Status": "EM PREPARAÃƒâ€¡ÃƒÆ'O",
            "Componentes": [],
            "ObservaÃƒÂ§ÃƒÂµes": []
        }

    # -----------------------------------------------------

    def add_component(self, component, status):

        self.report["Componentes"].append({
            "nome": component,
            "status": status
        })

    # -----------------------------------------------------

    def add_observation(self, text):

        self.report["ObservaÃƒÂ§ÃƒÂµes"].append(text)

    # -----------------------------------------------------

    def finalize(self):

        self.report["Status"] = "CONCLUÃƒÂDO"

    # -----------------------------------------------------

    def show(self):

        print("\n========================================")
        print("RELATÃƒâ€œRIO TÃƒâ€°CNICO")
        print("========================================")

        print(f"PavilhÃƒÂ£o : {self.report['PavilhÃƒÂ£o']}")
        print(f"VersÃƒÂ£o   : {self.report['VersÃƒÂ£o']}")
        print(f"Status   : {self.report['Status']}")
        print(f"Data     : {self.report['Data']}")

        print("\nCOMPONENTES")

        for item in self.report["Componentes"]:
            print(f" - {item['nome']:<30}{item['status']}")

        print("\nOBSERVAÃƒâ€¡Ãƒâ€¢ES")

        if self.report["ObservaÃƒÂ§ÃƒÂµes"]:
            for obs in self.report["ObservaÃƒÂ§ÃƒÂµes"]:
                print(f" * {obs}")
        else:
            print(" Nenhuma.")

        print("========================================\n")


# =======================================================

if __name__ == "__main__":

    report = TechnicalReportEngine()

    report.add_component("SYSTEM_HEALTH_ENGINE", "ONLINE")
    report.add_component("TECHNICAL_LASSO", "LIBERADO")
    report.add_component("HOMOLOGATION_ENGINE", "100%")

    report.add_observation("Primeiro PavilhÃƒÂ£o apto para homologaÃƒÂ§ÃƒÂ£o.")

    report.finalize()

    report.show()

