from dataclasses import dataclass, asdict
from datetime import datetime
import json
from pathlib import Path


@dataclass
class Lead:

    company: str
    contact: str
    source: str
    product: str
    status: str
    created_at: str


class FirstLeadRegistryEngine:

    def __init__(self):

        self.file = Path("first_real_lead.json")

    def create(self):

        lead = Lead(

            company="IOTEC",
            contact="PresidÃƒÂªncia",
            source="OperaÃƒÂ§ÃƒÂ£o Interna",
            product="Plataforma IOTEC",
            status="LEAD",
            created_at=datetime.now().isoformat()

        )

        self.file.write_text(

            json.dumps(

                asdict(lead),

                indent=4,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )

        return lead


if __name__ == "__main__":

    engine = FirstLeadRegistryEngine()

    lead = engine.create()

    print("=" * 70)
    print("FIRST LEAD REGISTRY ENGINE")
    print("=" * 70)

    print("COMPANY :", lead.company)
    print("CONTACT :", lead.contact)
    print("SOURCE  :", lead.source)
    print("PRODUCT :", lead.product)
    print("STATUS  :", lead.status)

    print()
    print("Arquivo criado: first_real_lead.json")

