# revenue/revenue_core.py

import json
import os
from pathlib import Path
from datetime import datetime


class RevenueCore:

    def __init__(self, root=r"C:\IOTEC"):

        self.root = Path(root)

        self.builder = self.root / "enterprise" / "builder"

        self.inventory = self.builder / "project_inventory.json"

        self.revenue = self.root / "enterprise" / "revenue"

        self.revenue.mkdir(parents=True, exist_ok=True)

        self.dashboard = {
            "generated_at": str(datetime.now()),
            "companies": 0,
            "buyers": 0,
            "contacts": 0,
            "leads": 0,
            "proposals": 0,
            "contracts": 0,
            "clients": 0,
            "estimated_revenue": 0,
            "next_mission": "",
            "biggest_bottleneck": ""
        }

    # --------------------------------------------------------

    def load_inventory(self):

        if not self.inventory.exists():

            print("InventÃƒÂ¡rio inexistente.")

            return []

        with open(self.inventory, encoding="utf-8") as f:

            data = json.load(f)

        return data["files"]

    # --------------------------------------------------------

    def scan_companies(self):

        files = self.load_inventory()

        companies = []

        for f in files:

            name = f["name"].lower()

            if "company" in name:

                companies.append(f)

            elif "empresa" in name:

                companies.append(f)

            elif "corporate" in name:

                companies.append(f)

            elif "crm" in name:

                companies.append(f)

        self.dashboard["companies"] = len(companies)

        return companies

    # --------------------------------------------------------

    def estimate_buyers(self):

        buyers = int(self.dashboard["companies"] * 0.35)

        self.dashboard["buyers"] = buyers

    # --------------------------------------------------------

    def estimate_contacts(self):

        contacts = int(self.dashboard["buyers"] * 0.70)

        self.dashboard["contacts"] = contacts

    # --------------------------------------------------------

    def estimate_leads(self):

        leads = int(self.dashboard["contacts"] * 0.60)

        self.dashboard["leads"] = leads

    # --------------------------------------------------------

    def estimate_proposals(self):

        proposals = int(self.dashboard["leads"] * 0.50)

        self.dashboard["proposals"] = proposals

    # --------------------------------------------------------

    def estimate_contracts(self):

        contracts = int(self.dashboard["proposals"] * 0.20)

        self.dashboard["contracts"] = contracts

    # --------------------------------------------------------

    def estimate_clients(self):

        self.dashboard["clients"] = self.dashboard["contracts"]

    # --------------------------------------------------------

    def estimate_revenue(self):

        self.dashboard["estimated_revenue"] = (
            self.dashboard["contracts"] * 8500
        )

    # --------------------------------------------------------

    def bottleneck(self):

        if self.dashboard["contacts"] == 0:

            self.dashboard["biggest_bottleneck"] = \
                "LOCALIZAR CONTATOS"

        elif self.dashboard["proposals"] == 0:

            self.dashboard["biggest_bottleneck"] = \
                "GERAR PROPOSTAS"

        elif self.dashboard["contracts"] == 0:

            self.dashboard["biggest_bottleneck"] = \
                "NEGOCIAÃƒâ€¡ÃƒÆ'O"

        else:

            self.dashboard["biggest_bottleneck"] = \
                "EXPANSÃƒÆ'O"

    # --------------------------------------------------------

    def mission(self):

        self.dashboard["next_mission"] = \
            "CAPTAR PRIMEIROS CLIENTES"

    # --------------------------------------------------------

    def save(self):

        file = self.revenue / "revenue_dashboard.json"

        with open(file, "w", encoding="utf-8") as f:

            json.dump(

                self.dashboard,

                f,

                indent=4,

                ensure_ascii=False

            )

    # --------------------------------------------------------

    def report(self):

        print("=" * 70)
        print("IOTEC REVENUE CORE")
        print("=" * 70)
        print()

        print("Empresas.............", self.dashboard["companies"])
        print("Compradores..........", self.dashboard["buyers"])
        print("Contatos.............", self.dashboard["contacts"])
        print("Leads................", self.dashboard["leads"])
        print("Propostas............", self.dashboard["proposals"])
        print("Contratos............", self.dashboard["contracts"])
        print("Clientes.............", self.dashboard["clients"])
        print()

        print("Receita Estimada..... R$ {:,.2f}".format(
            self.dashboard["estimated_revenue"]
        ))

        print()

        print("PrÃƒÂ³xima MissÃƒÂ£o.......",
              self.dashboard["next_mission"])

        print("Maior Gargalo........",
              self.dashboard["biggest_bottleneck"])

        print()

    # --------------------------------------------------------

    def run(self):

        self.scan_companies()

        self.estimate_buyers()

        self.estimate_contacts()

        self.estimate_leads()

        self.estimate_proposals()

        self.estimate_contracts()

        self.estimate_clients()

        self.estimate_revenue()

        self.bottleneck()

        self.mission()

        self.save()

        self.report()


if __name__ == "__main__":

    RevenueCore().run()

