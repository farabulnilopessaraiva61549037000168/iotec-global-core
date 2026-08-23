# ==============================================================================
# 011_LEAD_ENGINE.py
# IOTEC LEAD ENGINE
# ==============================================================================

from dataclasses import dataclass, asdict
from datetime import datetime
import uuid
import json
import os


DATABASE = "database"

os.makedirs(DATABASE, exist_ok=True)


@dataclass
class Lead:

    id: str
    created: str

    nome: str
    empresa: str
    email: str
    telefone: str
    cidade: str

    interesse: str

    origem: str = "SITE"

    status: str = "NOVO"

    valor_estimado: float = 0.0


class LeadEngine:

    def __init__(self):

        self.leads = {}

        print("LEAD ENGINE ONLINE")

    def novo_lead(
        self,
        nome,
        empresa,
        email,
        telefone,
        cidade,
        interesse,
        valor=0
    ):

        lead = Lead(

            id=str(uuid.uuid4())[:8],

            created=datetime.now().isoformat(),

            nome=nome,

            empresa=empresa,

            email=email,

            telefone=telefone,

            cidade=cidade,

            interesse=interesse,

            valor_estimado=valor

        )

        self.leads[lead.id] = lead

        self.salvar(lead)

        print(f"\nNOVO LEAD -> {lead.nome}")

        return lead

    def salvar(self, lead):

        arquivo = os.path.join(

            DATABASE,

            f"{lead.id}.json"

        )

        with open(

            arquivo,

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                asdict(lead),

                f,

                indent=4,

                ensure_ascii=False

            )

    def dashboard(self):

        print()

        print("=" * 60)

        print("LEAD ENGINE")

        print("=" * 60)

        print(f"TOTAL LEADS : {len(self.leads)}")

        print("=" * 60)

        print()

        for lead in self.leads.values():

            print(f"{lead.nome:25} {lead.status:12} {lead.cidade}")

        print()


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    engine = LeadEngine()

    engine.novo_lead(

        nome="ABC Engenharia",

        empresa="ABC Engenharia",

        email="contato@abc.com",

        telefone="(85)99999-9999",

        cidade="Fortaleza",

        interesse="Auditoria de Dados",

        valor=8900

    )

    engine.novo_lead(

        nome="Prefeitura de Ibicuitinga",

        empresa="Prefeitura",

        email="licitacao@ibicuitinga.ce.gov.br",

        telefone="(88)3333-3333",

        cidade="Ibicuitinga",

        interesse="Cidade Digital",

        valor=125000

    )

    engine.dashboard()

