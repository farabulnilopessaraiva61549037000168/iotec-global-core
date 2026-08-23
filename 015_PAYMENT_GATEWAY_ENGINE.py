# ==============================================================================
# 015_PAYMENT_GATEWAY_ENGINE.py
# ==============================================================================
# IOTEC PAYMENT GATEWAY ENGINE
# Estrutura para pagamentos reais
# ==============================================================================

from dataclasses import dataclass, asdict
from datetime import datetime
import uuid
import json
import os

DATABASE = "database/payments"

os.makedirs(DATABASE, exist_ok=True)


@dataclass
class Payment:

    id: str

    proposal_id: str

    cliente: str

    descricao: str

    valor: float

    metodo: str

    status: str

    criado: str

    confirmado: str | None = None


class PaymentGatewayEngine:

    def __init__(self):

        self.pagamentos = {}

        print("PAYMENT GATEWAY ENGINE ONLINE")

    # ----------------------------------------------------------------------

    def criar_pagamento(
            self,
            proposal_id,
            cliente,
            descricao,
            valor,
            metodo="PIX"
    ):

        pagamento = Payment(

            id=str(uuid.uuid4())[:8],

            proposal_id=proposal_id,

            cliente=cliente,

            descricao=descricao,

            valor=valor,

            metodo=metodo,

            status="AGUARDANDO_PAGAMENTO",

            criado=datetime.now().isoformat()

        )

        self.pagamentos[pagamento.id] = pagamento

        self.salvar(pagamento)

        print()
        print("=" * 60)
        print("NOVA COBRANÃ‡A")
        print("=" * 60)
        print(f"ID............. {pagamento.id}")
        print(f"CLIENTE........ {cliente}")
        print(f"VALOR.......... R$ {valor:,.2f}")
        print(f"MÃ‰TODO......... {metodo}")
        print(f"STATUS......... {pagamento.status}")

        return pagamento

    # ----------------------------------------------------------------------

    def confirmar_pagamento(self, payment_id):

        if payment_id not in self.pagamentos:

            print("Pagamento nÃ£o encontrado.")

            return

        pagamento = self.pagamentos[payment_id]

        pagamento.status = "PAGO"

        pagamento.confirmado = datetime.now().isoformat()

        self.salvar(pagamento)

        print()
        print("=" * 60)
        print("PAGAMENTO CONFIRMADO")
        print("=" * 60)
        print(f"CLIENTE........ {pagamento.cliente}")
        print(f"VALOR.......... R$ {pagamento.valor:,.2f}")
        print(f"STATUS......... {pagamento.status}")

    # ----------------------------------------------------------------------

    def salvar(self, pagamento):

        arquivo = os.path.join(

            DATABASE,

            f"{pagamento.id}.json"

        )

        with open(

            arquivo,

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                asdict(pagamento),

                f,

                indent=4,

                ensure_ascii=False

            )


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    engine = PaymentGatewayEngine()

    pagamento = engine.criar_pagamento(

        proposal_id="PROP001",

        cliente="ABC Engenharia",

        descricao="DiagnÃ³stico Digital",

        valor=49.90

    )

    # SimulaÃ§Ã£o de confirmaÃ§Ã£o.
    # Quando houver integraÃ§Ã£o com um gateway real,
    # esta chamada serÃ¡ feita apÃ³s a confirmaÃ§Ã£o do provedor.

    engine.confirmar_pagamento(pagamento.id)

