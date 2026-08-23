import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
015_PRODUCTION_LINE_ENGINE.py
LINHA DE PRODUÃƒâ€¡ÃƒÆ'O INTELIGENTE
======================================================================
"""

from datetime import datetime
import random


class Produto:

    def __init__(self, codigo, nome):

        self.codigo = codigo
        self.nome = nome

        self.etapa = 0

        self.status = "EM PRODUÃƒâ€¡ÃƒÆ'O"

        self.historico = []

        self.pendencias = []

        self.qualidade = "PENDENTE"


class Agente:

    def __init__(self, nome, responsabilidade):

        self.nome = nome
        self.responsabilidade = responsabilidade

    def executar(self, produto):

        print("="*70)

        print("AGENTE:", self.nome)

        print("Responsabilidade:", self.responsabilidade)

        print()

        # SimulaÃƒÂ§ÃƒÂ£o de verificaÃƒÂ§ÃƒÂ£o

        problema = random.randint(1,10)

        if problema == 1:

            pendencia = "Material incompleto"

            produto.pendencias.append(pendencia)

            produto.status = "AGUARDANDO LOGÃƒÂSTICA"

            print("STATUS: BLOQUEADO")

            print("Motivo:", pendencia)

            print()

            print("Kernel acionou automaticamente")

            print("a Central LogÃƒÂ­stica.")

            return False

        print("STATUS: CONCLUÃƒÂDO")

        produto.historico.append(self.nome)

        produto.etapa += 1

        return True


class LinhaProducao:

    def __init__(self):

        self.produto = Produto(

            "PRD-000001",

            "Projeto Executivo"

        )

        self.agentes = [

            Agente(

                "AGENTE 01",

                "RecepÃƒÂ§ÃƒÂ£o"

            ),

            Agente(

                "AGENTE 02",

                "ConferÃƒÂªncia"

            ),

            Agente(

                "AGENTE 03",

                "Qualidade"

            ),

            Agente(

                "AGENTE 04",

                "ProduÃƒÂ§ÃƒÂ£o"

            ),

            Agente(

                "AGENTE 05",

                "RevisÃƒÂ£o"

            ),

            Agente(

                "AGENTE 06",

                "Entrega"

            )

        ]


    def iniciar(self):

        print("="*70)

        print("IOTEC")

        print("LINHA DE PRODUÃƒâ€¡ÃƒÆ'O")

        print("="*70)

        print()

        print("Produto:", self.produto.nome)

        print("CÃƒÂ³digo :", self.produto.codigo)

        print()

        for agente in self.agentes:

            sucesso = agente.executar(self.produto)

            if not sucesso:

                break

        self.finalizar()


    def finalizar(self):

        print()

        print("="*70)

        print("OBSERVABILIDADE")

        print("="*70)

        print()

        print("Etapas concluÃƒÂ­das:", self.produto.etapa)

        print("Status:", self.produto.status)

        print()

        print("HistÃƒÂ³rico:")

        for item in self.produto.historico:

            print("Ã¢Å"â€", item)

        print()

        if self.produto.pendencias:

            print("PendÃƒÂªncias:")

            for p in self.produto.pendencias:

                print("Ã¢Å¡Â ", p)

        else:

            self.produto.qualidade = "APROVADO"

            print("Produto aprovado.")

            print()

            print("Pronto para entrega.")

        print()

        print("="*70)

        print("KERNEL")

        print("="*70)

        print()

        if self.produto.pendencias:

            print("AÃƒâ€¡ÃƒÆ'O AUTOMÃƒÂTICA:")

            print()

            print("Solicitar novos dados")

            print("ÃƒÂ  Central LogÃƒÂ­stica.")

        else:

            print("Produto encaminhado")

            print("para o setor Comercial.")

        print()

        print("="*70)


if __name__ == "__main__":

    linha = LinhaProducao()

    linha.iniciar()



