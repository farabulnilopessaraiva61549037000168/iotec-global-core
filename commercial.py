# ============================================================
# C:\IOTEC\commercial.py
# IOTEC COMMERCIAL CENTER
# ============================================================

import sys
from pathlib import Path
from datetime import datetime

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


class CommercialCenter:

    def __init__(self):

        self.companies = CompanyDB.load()
        self.crm = CRMDB.load()
        self.pipeline = PipelineDB.load()
        self.opportunities = OpportunityDB.load()

    # ========================================================

    def _crm_index(self):

        return {
            x["company_name"]: x
            for x in self.crm
            if "company_name" in x
        }

    # ========================================================

    def _pipeline_index(self):

        return {
            x["company_name"]: x
            for x in self.pipeline
            if "company_name" in x
        }

    # ========================================================

    def _opportunity_index(self):

        return {
            x["company_name"]: x
            for x in self.opportunities
            if "company_name" in x
        }

    # ========================================================

    def synchronize(self):

        crm = self._crm_index()
        pipeline = self._pipeline_index()
        opportunities = self._opportunity_index()

        novos_crm = 0
        novos_pipeline = 0
        novas_oportunidades = 0

        for company in self.companies:

            nome = company.get("company_name")

            if not nome:
                continue

            # ----------------------------------------------
            # CRM
            # ----------------------------------------------

            if nome not in crm:

                self.crm.append({

                    "company_name": nome,

                    "segment": company.get("segmento",""),

                    "email": "",

                    "phone": "",

                    "website": "",

                    "linkedin": "",

                    "contact_person": "",

                    "proposal_sent": False,

                    "contract_signed": False,

                    "client": False,

                    "created_at": str(datetime.now()),

                    "updated_at": str(datetime.now())

                })

                novos_crm += 1

            # ----------------------------------------------
            # PIPELINE
            # ----------------------------------------------

            if nome not in pipeline:

                self.pipeline.append({

                    "company_name": nome,

                    "stage": "NOVO_LEAD",

                    "history": [

                        {

                            "stage": "NOVO_LEAD",

                            "date": str(datetime.now())

                        }

                    ]

                })

                novos_pipeline += 1

            # ----------------------------------------------
            # OPORTUNIDADES
            # ----------------------------------------------

            if nome not in opportunities:

                self.opportunities.append({

                    "company_name": nome,

                    "score": company.get("market_score",70),

                    "priority": "ALTA",

                    "status": "NOVA"

                })

                novas_oportunidades += 1

        CRMDB.save(self.crm)
        PipelineDB.save(self.pipeline)
        OpportunityDB.save(self.opportunities)

        print("="*70)
        print("IOTEC COMMERCIAL CENTER")
        print("="*70)
        print()

        print("Empresas................",len(self.companies))
        print("CRM.....................",len(self.crm))
        print("Pipeline................",len(self.pipeline))
        print("Oportunidades...........",len(self.opportunities))

        print()

        print("Novos CRM...............",novos_crm)
        print("Novos Pipeline..........",novos_pipeline)
        print("Novas Oportunidades.....",novas_oportunidades)

        print()

        contatos = 0

        for item in self.crm:

            if (
                item.get("email")
                or item.get("phone")
                or item.get("website")
            ):
                contatos += 1

        print("Contatos Encontrados....",contatos)

        print()

        if contatos == 0:

            print("MISSÃƒÆ'O PRIORITÃƒÂRIA")
            print("------------------")
            print("LOCALIZAR CONTATOS OFICIAIS")

        else:

            print("MISSÃƒÆ'O PRIORITÃƒÂRIA")
            print("------------------")
            print("GERAR PROPOSTAS")

        print()

        print("AtualizaÃƒÂ§ÃƒÂ£o concluÃƒÂ­da.")

# ============================================================

if __name__ == "__main__":

    CommercialCenter().synchronize()

