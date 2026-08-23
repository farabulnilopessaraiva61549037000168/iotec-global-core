import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC_CUSTOMER_SERVICE_CORE.py
# ============================================================
# NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO DE ATENDIMENTO COMERCIAL
# ============================================================
# OBJETIVO:
# ------------------------------------------------------------
# Este nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© EXCLUSIVAMENTE responsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel por:
#
# - atendimento
# - vendas
# - apresentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de catÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo
# - demonstraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de serviÃƒÆ'Ã†â€™os
# - investigaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do cliente
# - geraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de proposta
# - formalizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o financeira
# - confirmaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de pagamento
# - acompanhamento operacional
# - entrega do projeto
#
# ESTE NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EXPÃƒÆ'Ã†â€™E:
# - mapas econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´micos
# - inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia interna
# - sentinelas
# - metas financeiras
# - cartografia estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica
#
# ============================================================

import time
from dataclasses import dataclass, field
from typing import List, Dict

# ============================================================
# CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO PÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡BLICO
# ============================================================

PUBLIC_CATALOG = {

    "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Empresarial": {
        "descricao": "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de processos operacionais.",
        "valor_base": 15000
    },

    "ERP Empresarial": {
        "descricao": "Sistema completo de gestÃƒÆ'Ã†â€™o empresarial.",
        "valor_base": 35000
    },

    "Dashboard Inteligente": {
        "descricao": "Painel analÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico e operacional.",
        "valor_base": 12000
    },

    "Sistema Industrial": {
        "descricao": "Monitoramento industrial automatizado.",
        "valor_base": 45000
    },

    "Sistema JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico": {
        "descricao": "GestÃƒÆ'Ã†â€™o processual e jurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dica.",
        "valor_base": 25000
    },

    "Sistema Educacional": {
        "descricao": "GestÃƒÆ'Ã†â€™o escolar e pedagÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica.",
        "valor_base": 18000
    },

    "Sistema Hospitalar": {
        "descricao": "GestÃƒÆ'Ã†â€™o clÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nica e hospitalar.",
        "valor_base": 50000
    }
}

# ============================================================
# ESTRUTURAS
# ============================================================

@dataclass
class Client:
    pass

    nome: str
    email: str
    empresa: str


@dataclass
class Order:
    pass

    servico: str
    descricao: str
    valor: float
    entrada: float
    restante: float
    status: str = "AGUARDANDO PAGAMENTO"

# ============================================================
# NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO DE ATENDIMENTO
# ============================================================

class IOTECCustomerService:
    pass

    def __init__(self):
        pass

        self.client = None
        self.order = None
        self.payment_confirmed = False

    # ========================================================
    # IA VISUAL
    # ========================================================

    def think(self, text):
        pass

        print(f"\n[IOTEC AI] {text}")

        time.sleep(1)

    # ========================================================
    # APRESENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def welcome(self):
        pass

        print("\n================================================")
        print("            IOTEC GLOBAL PLATFORM")
        print("================================================")

        self.think(
            "Bem-vindo ao nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo inteligente de atendimento."
        )

    # ========================================================
    # COLETAR CLIENTE
    # ========================================================

    def collect_client_data(self):
        pass

        print("\n================ CLIENTE ================")

        nome = input("\nNome: ")

        email = input("\nE-mail: ")

        empresa = input("\nEmpresa: ")

        self.client = Client(
            nome=nome,
            email=email,
            empresa=empresa
        )

    # ========================================================
    # MOSTRAR CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO
    # ========================================================

    def show_catalog(self):
        pass

        print("\n================ CATÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂLOGO ================")

        for index, item in enumerate(PUBLIC_CATALOG.keys(), start=1):
            pass

            print(f"\n{index} - {item}")

    # ========================================================
    # EXPLICAR SERVIÃƒÆ'Ã†â€™O
    # ========================================================

    def explain_service(self, service):
        pass

        data = PUBLIC_CATALOG[service]

        self.think(
            f"Apresentando soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {service}"
        )

        print(f"\nSERVIÃƒÆ'Ã†â€™O: {service}")

        print(f"\nDESCRIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:")
        print(data["descricao"])

        print(f"\nVALOR BASE:")
        print(f"R$ {data['valor_base']:,.2f}")

    # ========================================================
    # INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def investigate(self):
        pass

        print("\n================ INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        setor = input(
            "\nQual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o setor da empresa?\n\n>>> "
        )

        problema = input(
            "\nQuais problemas enfrenta atualmente?\n\n>>> "
        )

        objetivo = input(
            "\nQual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o principal objetivo?\n\n>>> "
        )

        usuarios = input(
            "\nQuantas pessoas utilizarÃƒÆ'Ã†â€™o o sistema?\n\n>>> "
        )

        self.think(
            "Analisando contexto operacional..."
        )

        print("\n================ DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO ================")

        print(f"\nSETOR: {setor}")
        print(f"\nPROBLEMA: {problema}")
        print(f"\nOBJETIVO: {objetivo}")
        print(f"\nUSUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS: {usuarios}")

    # ========================================================
    # GERAR PEDIDO
    # ========================================================

    def create_order(self, service):
        pass

        valor = PUBLIC_CATALOG[service]["valor_base"]

        entrada = valor * 0.30

        restante = valor * 0.70

        self.order = Order(

            servico=service,
            descricao=PUBLIC_CATALOG[service]["descricao"],
            valor=valor,
            entrada=entrada,
            restante=restante
        )

    # ========================================================
    # FORMALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def formalize(self):
        pass

        print("\n================ PROPOSTA ================")

        print(f"\nCLIENTE: {self.client.nome}")

        print(f"\nEMPRESA: {self.client.empresa}")

        print(f"\nSERVIÃƒÆ'Ã†â€™O: {self.order.servico}")

        print(f"\nDESCRIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:")
        print(self.order.descricao)

        print(f"\nVALOR TOTAL:")
        print(f"R$ {self.order.valor:,.2f}")

        print(f"\nENTRADA OPERACIONAL 30%:")
        print(f"R$ {self.order.entrada:,.2f}")

        print(f"\nRESTANTE 70%:")
        print(f"R$ {self.order.restante:,.2f}")

    # ========================================================
    # PAGAMENTO
    # ========================================================

    def request_payment(self):
        pass

        self.think(
            "Para continuarmos o atendimento, ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio confirmar o pagamento da entrada operacional."
        )

        print("\n================ PAGAMENTO ================")

        print("\nMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TODOS DISPONÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS:")

        print("\n- PayPal")
        print("- PIX")
        print("- Stripe")
        print("- TransferÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia")

        confirmation = input(
            "\nPagamento confirmado?\n\n>>> "
        ).lower()

        if confirmation in ["sim", "s"]:
            pass

            self.payment_confirmed = True

            self.order.status = "PAGAMENTO CONFIRMADO"

            self.think(
                "Pagamento confirmado com sucesso."
            )

        else:
            pass

            self.payment_confirmed = False

            self.order.status = "AGUARDANDO PAGAMENTO"

            self.think(
                "Atendimento pausado atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© confirmaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o financeira."
            )

    # ========================================================
    # PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # ========================================================

    def production_pipeline(self):
        pass

        if not self.payment_confirmed:
            pass

            self.think(
                "ProduÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o bloqueada."
            )

            return

        print("\n================ PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ================")

        steps = [

            "Criando arquitetura",
            "Gerando banco de dados",
            "Configurando backend",
            "Construindo frontend",
            "Gerando APIs",
            "Configurando dashboards",
            "Executando validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
            "Preparando entrega"
        ]

        for step in steps:
            pass

            self.think(step)

        self.order.status = "PROJETO FINALIZADO"

    # ========================================================
    # ENTREGA
    # ========================================================

    def delivery(self):
        pass

        if self.order.status != "PROJETO FINALIZADO":
            pass

            self.think(
                "Projeto ainda nÃƒÆ'Ã†â€™o finalizado."
            )

            return

        print("\n================ ENTREGA ================")

        print("\nSTATUS:")
        print("PROJETO ENTREGUE")

        print("\nVERIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:")
        print("ValidaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o operacional concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")

        print("\nSUPORTE:")
        print("Sistema monitorado pela IA.")

    # ========================================================
    # FLUXO PRINCIPAL
    # ========================================================

    def start(self):
        pass

        self.welcome()

        self.collect_client_data()

        self.show_catalog()

        service_names = list(PUBLIC_CATALOG.keys())

        choice = int(
            input(
                "\nEscolha um serviÃƒÆ'Ã†â€™o:\n\n>>> "
            )
        )

        selected_service = service_names[choice - 1]

        self.explain_service(selected_service)

        self.investigate()

        self.create_order(selected_service)

        self.formalize()

        self.request_payment()

        if not self.payment_confirmed:
            pass

            return

        self.production_pipeline()

        self.delivery()

# ============================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

if __name__ == "__main__":
    pass

    system = IOTECCustomerService()

    system.start()


