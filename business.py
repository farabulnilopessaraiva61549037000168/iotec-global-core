"""
==============================================================
IOTEC BUSINESS OPERATING SYSTEM
BUSINESS.PY
PARTE 1
==============================================================
"""

from pathlib import Path
from datetime import datetime
import sys

ROOT = Path(r"C:\IOTEC")
ENTERPRISE = ROOT / "enterprise"

if str(ENTERPRISE) not in sys.path:
    sys.path.insert(0, str(ENTERPRISE))

from enterprise_database import (
    CompanyDB,
    CRMDB,
    PipelineDB,
    OpportunityDB
)


class BusinessSystem:

    def __init__(self):

        self.started = datetime.now()

        self.stats = {
            "companies": 0,
            "crm": 0,
            "pipeline": 0,
            "opportunities": 0,
            "proposals": 0,
            "contracts": 0,
            "clients": 0
        }

        self.missions = []

        self.gargalos = []

    # =====================================================

    def load_databases(self):

        self.companies = CompanyDB.load()

        self.crm = CRMDB.load()

        self.pipeline = PipelineDB.load()

        self.opportunities = OpportunityDB.load()

        self.stats["companies"] = len(self.companies)
        self.stats["crm"] = len(self.crm)
        self.stats["pipeline"] = len(self.pipeline)
        self.stats["opportunities"] = len(self.opportunities)

    # =====================================================

    def validate(self):

        if self.stats["companies"] == 0:

            self.gargalos.append(
                "Nenhuma empresa cadastrada."
            )

        if self.stats["crm"] == 0:

            self.gargalos.append(
                "CRM vazio."
            )

        if self.stats["pipeline"] == 0:

            self.gargalos.append(
                "Pipeline vazio."
            )

        if self.stats["opportunities"] == 0:

            self.gargalos.append(
                "Banco de oportunidades vazio."
            )

    # =====================================================

    def detect_bottleneck(self):

        if self.stats["companies"] == 0:

            return "DESCOBRIR EMPRESAS"

        if self.stats["pipeline"] < self.stats["companies"]:

            return "CRIAR PIPELINE"

        contatos = 0

        for item in self.crm:

            if (
                item.get("email")
                or item.get("phone")
                or item.get("website")
            ):
                contatos += 1

        if contatos == 0:

            return "LOCALIZAR CONTATOS"

        propostas = 0

        for item in self.crm:

            if item.get("proposal_sent"):

                propostas += 1

        if propostas == 0:

            return "GERAR PROPOSTAS"

        contratos = 0

        for item in self.crm:

            if item.get("contract_signed"):

                contratos += 1

        if contratos == 0:

            return "NEGOCIAR"

        return "EXPANDIR MERCADO"

    # =====================================================

    def create_mission(self):

        self.missions.append({

            "created_at": str(datetime.now()),

            "priority": "CRÃƒÂTICA",

            "objective": self.detect_bottleneck()

        })

    # =====================================================

    def executive_report(self):

        print("=" * 70)
        print("IOTEC BUSINESS OPERATING SYSTEM")
        print("=" * 70)
        print()

        print("Empresas...........", self.stats["companies"])
        print("CRM................", self.stats["crm"])
        print("Pipeline...........", self.stats["pipeline"])
        print("Oportunidades......", self.stats["opportunities"])

        print()

        print("Gargalo Atual......", self.detect_bottleneck())

        print()

        print("MissÃƒÂµes............", len(self.missions))

        print()

        print("Sistema iniciado em:")

        print(self.started)

        print()

    # =====================================================

    def run(self):

        self.load_databases()

        self.validate()

        self.create_mission()

        self.executive_report()


if __name__ == "__main__":

    BusinessSystem().run()

