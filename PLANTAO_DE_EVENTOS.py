import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================
IOTEC
PLANTAO_DE_EVENTOS.py
CENTRAL EXECUTIVA DO KERNEL
==============================================================
"""

from datetime import datetime


class PlantaoEventos:

    def __init__(self):

        self.data = datetime.now()

        self.operacao = "NORMAL"

        self.comercial = "ATIVO"

        self.financeiro = "EM MONITORAMENTO"

        self.tecnologia = "OPERACIONAL"

        self.crm = "ONLINE"

        self.kernel = "ESTÃƒÂVEL"

        self.recomendacoes = []


    def cabecalho(self):

        print("=" * 70)
        print("              IOTEC - PLANTÃƒÆ'O DE EVENTOS")
        print("=" * 70)
        print("Data:", self.data.strftime("%d/%m/%Y"))
        print("Hora:", self.data.strftime("%H:%M:%S"))
        print("=" * 70)


    def situacao_empresa(self):

        print("\nSITUAÃƒâ€¡ÃƒÆ'O GERAL\n")

        print(f"Kernel.................... {self.kernel}")

        print(f"OperaÃƒÂ§ÃƒÂ£o................. {self.operacao}")

        print(f"Comercial................ {self.comercial}")

        print(f"Financeiro............... {self.financeiro}")

        print(f"Tecnologia............... {self.tecnologia}")

        print(f"CRM...................... {self.crm}")


    def indicadores(self):

        print("\nINDICADORES OPERACIONAIS\n")

        print("Agentes Ativos........... 0")

        print("MissÃƒÂµes................. 0")

        print("Leads................... 0")

        print("Clientes................ 0")

        print("ReuniÃƒÂµes................ 0")

        print("Propostas............... 0")

        print("Contratos............... 0")

        print("Projetos................ 0")

        print("Parceiros............... 0")

        print("Receita Prevista........ R$ 0,00")

        print("Receita Confirmada...... R$ 0,00")


    def monitoramento(self):

        print("\nMONITORAMENTO\n")

        print("Ã¢Å"â€œ Banco de Dados........ OK")

        print("Ã¢Å"â€œ Kernel................ OK")

        print("Ã¢Å"â€œ Control Center........ OK")

        print("Ã¢Å"â€œ CRM................... OK")

        print("Ã¢Å"â€œ Comercial............. OK")

        print("Ã¢Å"â€œ Agentes............... OK")


    def alertas(self):

        print("\nALERTAS\n")

        print("Nenhum alerta crÃƒÂ­tico registrado.")


    def oportunidades(self):

        print("\nOPORTUNIDADES\n")

        print("Ã¢â‚¬Â¢ Procurar novos clientes.")

        print("Ã¢â‚¬Â¢ Prospectar empresas.")

        print("Ã¢â‚¬Â¢ Atualizar portfÃƒÂ³lio.")

        print("Ã¢â‚¬Â¢ Buscar parceiros.")

        print("Ã¢â‚¬Â¢ Monitorar editais.")

        print("Ã¢â‚¬Â¢ Verificar contratos pendentes.")


    def inteligencia_kernel(self):

        print("\nANÃƒÂLISE DO KERNEL\n")

        print("O Kernel informa:")

        print()

        print("A operaÃƒÂ§ÃƒÂ£o encontra-se estÃƒÂ¡vel.")

        print("NÃƒÂ£o foram identificadas falhas crÃƒÂ­ticas.")

        print("O principal objetivo continua sendo:")

        print("GERAR NOVOS CONTRATOS.")

        print()

        print("Prioridade nÃƒÂºmero 1:")

        print("ProspecÃƒÂ§ÃƒÂ£o Comercial.")

        print()

        print("Prioridade nÃƒÂºmero 2:")

        print("Acompanhar negociaÃƒÂ§ÃƒÂµes abertas.")

        print()

        print("Prioridade nÃƒÂºmero 3:")

        print("Converter oportunidades em receita.")


    def plano_de_acao(self):

        print("\nPLANO DE AÃƒâ€¡ÃƒÆ'O\n")

        etapas = [

            "Pesquisar oportunidades.",

            "Qualificar Leads.",

            "Entrar em contato.",

            "Agendar reuniÃƒÂ£o.",

            "Preparar proposta.",

            "Negociar.",

            "Fechar contrato.",

            "Entregar soluÃƒÂ§ÃƒÂ£o.",

            "Receber pagamento.",

            "Fazer pÃƒÂ³s-venda."

        ]

        for i, etapa in enumerate(etapas, start=1):

            print(f"{i:02d} - {etapa}")


    def rodape(self):

        print()

        print("=" * 70)

        print("FIM DO PLANTÃƒÆ'O")

        print("=" * 70)


    def executar(self):

        self.cabecalho()

        self.situacao_empresa()

        self.indicadores()

        self.monitoramento()

        self.alertas()

        self.oportunidades()

        self.inteligencia_kernel()

        self.plano_de_acao()

        self.rodape()


if __name__ == "__main__":

    painel = PlantaoEventos()

    painel.executar()



