import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================

IOTEC ANCHOR ENGINE

A Voz Oficial da Torre de Comando

===============================================================

MissÃ£o

Transformar relatÃ³rios tÃ©cnicos em um briefing executivo
voltado para tomada de decisÃ£o.

===============================================================
"""

from datetime import datetime


class AnchorEngine:

    def __init__(self):

        self.nome = "Farabulini"

        self.empresa = "IOTEC"

        self.status = "ESTÃVEL"


    def saudacao(self):

        hora = datetime.now().hour

        if hora < 12:
            return "Bom dia"

        elif hora < 18:
            return "Boa tarde"

        return "Boa noite"


    def abertura(self):

        print()

        print("=" * 70)
        print("TORRE DE COMANDO EXECUTIVA")
        print(self.empresa)
        print("=" * 70)

        print()

        print(f"{self.saudacao()}, {self.nome}.")

        print()

        print("O NÃºcleo Executivo concluiu mais um ciclo de monitoramento.")

        print()

        print(f"HorÃ¡rio da atualizaÃ§Ã£o: {datetime.now()}")

        print()

        print("-" * 70)


    def status_empresa(self, status):

        self.status = status

        print()

        print("STATUS GERAL")

        print()

        print(self.status)

        print()

        print("-" * 70)


    def narrar(self, titulo, texto):

        print()

        print(titulo.upper())

        print()

        print(texto)

        print()

        print("-" * 70)


    def recomendacoes(self, lista):

        print()

        print("RECOMENDAÃ‡Ã•ES")

        print()

        for item in lista:

            print(f"â€¢ {item}")

        print()

        print("-" * 70)


    def encerramento(self):

        print()

        print("NÃšCLEO EXECUTIVO")

        print()

        print("Monitoramento........ATIVO")

        print("PrÃ³xima atualizaÃ§Ã£o..10 minutos")

        print()

        print('"NÃ³s monitoramos."')

        print('"NÃ³s analisamos."')

        print('"NÃ³s explicamos."')

        print('"VocÃª decide."')

        print()

        print("=" * 70)



if __name__ == "__main__":

    anchor = AnchorEngine()

    anchor.abertura()

    anchor.status_empresa("ATENÃ‡ÃƒO")

    anchor.narrar(

        "SituaÃ§Ã£o Comercial",

        "O nÃºcleo comercial concluiu a anÃ¡lise das oportunidades registradas. "
        "O pipeline permanece abaixo da meta mensal e ainda nÃ£o existem contratos assinados neste ciclo."

    )

    anchor.narrar(

        "Impacto",

        "A infraestrutura tecnolÃ³gica encontra-se estÃ¡vel. "
        "O principal desafio da empresa continua sendo transformar oportunidades em contratos."

    )

    anchor.recomendacoes([

        "Ampliar campanhas comerciais.",

        "Prospectar novos clientes.",

        "Priorizar mercados internacionais.",

        "Acelerar negociaÃ§Ãµes em andamento.",

        "Expandir o portfÃ³lio de produtos."

    ])

    anchor.encerramento()




