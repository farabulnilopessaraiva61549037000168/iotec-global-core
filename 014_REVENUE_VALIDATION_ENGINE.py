# ==============================================================================
# 014_REVENUE_VALIDATION_ENGINE.py
# ==============================================================================
# IOTEC - REVENUE VALIDATION ENGINE
# Primeira validaÃ§Ã£o monetÃ¡ria da plataforma
# ==============================================================================

from dataclasses import dataclass, asdict
from datetime import datetime
import json
import os
import uuid

DATABASE = "database/revenue"

os.makedirs(DATABASE, exist_ok=True)


# ==============================================================================
# VALIDAÃ‡ÃƒO
# ==============================================================================

@dataclass
class RevenueRecord:

    id: str

    cliente: str

    empresa: str

    descricao: str

    valor: float

    status: str

    criado: str


# ==============================================================================
# ENGINE
# ==============================================================================

class RevenueValidationEngine:

    def __init__(self):

        self.registros = {}

        print("REVENUE VALIDATION ENGINE ONLINE")

    # -------------------------------------------------------------------------

    def registrar(self,
                  cliente,
                  empresa,
                  descricao,
                  valor):

        registro = RevenueRecord(

            id=str(uuid.uuid4())[:8],

            cliente=cliente,

            empresa=empresa,

            descricao=descricao,

            valor=valor,

            status="CONFIRMADO",

            criado=datetime.now().isoformat()

        )

        self.registros[registro.id] = registro

        self.salvar(registro)

        print()
        print("=" * 65)
        print(" PRIMEIRA RECEITA REGISTRADA ")
        print("=" * 65)
        print(f"Cliente.....: {cliente}")
        print(f"Empresa.....: {empresa}")
        print(f"Valor.......: R$ {valor:,.2f}")
        print(f"Status......: {registro.status}")
        print("=" * 65)

        return registro

    # -------------------------------------------------------------------------

    def salvar(self, registro):

        arquivo = os.path.join(

            DATABASE,

            f"{registro.id}.json"

        )

        with open(arquivo, "w", encoding="utf8") as f:

            json.dump(

                asdict(registro),

                f,

                indent=4,

                ensure_ascii=False

            )

    # -------------------------------------------------------------------------

    def dashboard(self):

        total = sum(r.valor for r in self.registros.values())

        print()
        print("=" * 65)
        print("REVENUE VALIDATION")
        print("=" * 65)
        print(f"Receitas............. {len(self.registros)}")
        print(f"Valor Total.......... R$ {total:,.2f}")
        print("=" * 65)

        for r in self.registros.values():

            print(

                f"{r.cliente:25}"

                f"R$ {r.valor:10,.2f}"

            )


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    engine = RevenueValidationEngine()

    engine.registrar(

        cliente="Primeiro Cliente",

        empresa="IOTEC DEMO",

        descricao="ValidaÃ§Ã£o MonetÃ¡ria",

        valor=1.00

    )

    engine.dashboard()

