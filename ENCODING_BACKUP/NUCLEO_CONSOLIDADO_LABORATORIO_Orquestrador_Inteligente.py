import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC CORE AI
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Orquestrador Inteligente
# =========================================================

class Cliente:
    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa


class Pedido:
    def __init__(self, cliente, descricao):
        self.cliente = cliente
        self.descricao = descricao
        self.status = "Recebido"
        self.valor_total = 0
        self.entrada = 0
        self.restante = 0
        self.tipo_servico = None
        self.escopo = {}
        self.contrato_gerado = False


class IOTEC_AI:
    pass

    def __init__(self):
        self.pedidos = []

    # =====================================================
    # RECEBER PEDIDO
    # =====================================================

    def receber_pedido(self, cliente, descricao):
        pass

        pedido = Pedido(cliente, descricao)

        print("\n[IA] Novo pedido recebido.")
        print(f"[CLIENTE] {cliente.nome}")
        print(f"[EMPRESA] {cliente.empresa}")
        print(f"[DESCRIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] {descricao}")

        self.pedidos.append(pedido)

        return pedido

    # =====================================================
    # ANALISAR PEDIDO
    # =====================================================

    def analisar_pedido(self, pedido):
        pass

        descricao = pedido.descricao.lower()

        if "sistema" in descricao:
            pedido.tipo_servico = "Desenvolvimento de Sistema"

        elif "auditoria" in descricao:
            pedido.tipo_servico = "Auditoria Empresarial"

        elif "dashboard" in descricao:
            pedido.tipo_servico = "Business Intelligence"

        else:
            pedido.tipo_servico = "ServiÃƒÆ'Ã†â€™o Personalizado"

        print("\n[IA] Pedido analisado.")
        print(f"[TIPO IDENTIFICADO] {pedido.tipo_servico}")

    # =====================================================
    # DEFINIR ESCOPO
    # =====================================================

    def criar_escopo(self, pedido):
        pass

        pedido.escopo = {
            "frontend": True,
            "backend": True,
            "banco_de_dados": True,
            "painel_admin": True,
            "api": True
        }

        print("\n[IA] Escopo criado com sucesso.")

    # =====================================================
    # CALCULAR ORÃƒÆ'Ã†â€™AMENTO
    # =====================================================

    def calcular_orcamento(self, pedido):
        pass

        base = 5000

        if pedido.tipo_servico == "Desenvolvimento de Sistema":
            base = 15000

        elif pedido.tipo_servico == "Auditoria Empresarial":
            base = 7000

        elif pedido.tipo_servico == "Business Intelligence":
            base = 12000

        pedido.valor_total = base
        pedido.entrada = base * 0.30
        pedido.restante = base * 0.70

        print("\n[IA] OrÃƒÆ'Ã†â€™amento calculado.")
        print(f"[TOTAL] R$ {pedido.valor_total:.2f}")
        print(f"[ENTRADA 30%] R$ {pedido.entrada:.2f}")
        print(f"[RESTANTE 70%] R$ {pedido.restante:.2f}")

    # =====================================================
    # GERAR CONTRATO
    # =====================================================

    def gerar_contrato(self, pedido):
        pass

        pedido.contrato_gerado = True

        print("\n[IA] Contrato gerado automaticamente.")

    # =====================================================
    # CONFIRMAR PAGAMENTO
    # =====================================================

    def confirmar_pagamento_entrada(self, pedido):
        pass

        pedido.status = "Projeto Liberado"

        print("\n[IA] Entrada confirmada.")
        print("[STATUS] Projeto liberado para produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")

    # =====================================================
    # INICIAR PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # =====================================================

    def iniciar_producao(self, pedido):
        pass

        print("\n[IA] Iniciando produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do projeto...")

        etapas = [
            "Criando arquitetura",
            "Gerando banco de dados",
            "Configurando backend",
            "Construindo frontend",
            "Integrando APIs",
            "Executando testes",
            "Preparando entrega"
        ]

        for etapa in etapas:
            print(f"[PRODUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] {etapa}")

        pedido.status = "Projeto Finalizado"

    # =====================================================
    # ENTREGA FINAL
    # =====================================================

    def entregar_projeto(self, pedido):
        pass

        print("\n[IA] Projeto concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")
        print(f"[COBRANÃƒÆ'Ã†â€™A FINAL 70%] R$ {pedido.restante:.2f}")

        pedido.status = "Entregue"

        print("[STATUS FINAL] Projeto entregue com sucesso.")


# =========================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

cliente = Cliente(
    nome="Bruno Lopes",
    empresa="IOTEC"
)

ia = IOTEC_AI()

pedido = ia.receber_pedido(
    cliente,
    "Preciso de um sistema empresarial inteligente com painel administrativo."
)

ia.analisar_pedido(pedido)

ia.criar_escopo(pedido)

ia.calcular_orcamento(pedido)

ia.gerar_contrato(pedido)

ia.confirmar_pagamento_entrada(pedido)

ia.iniciar_producao(pedido)

ia.entregar_projeto(pedido)


