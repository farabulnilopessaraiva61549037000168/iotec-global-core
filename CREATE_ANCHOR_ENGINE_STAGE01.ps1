Clear-Host

Write-Host ""
Write-Host "==========================================================="
Write-Host " IOTEC ANCHOR ENGINE"
Write-Host " STAGE 001"
Write-Host "==========================================================="
Write-Host ""

$arquivo = "C:\IOTEC\ANCHOR_ENGINE.py"

$codigo = @'
"""
===============================================================

IOTEC ANCHOR ENGINE

A Voz Oficial da Torre de Comando

===============================================================

Missão

Transformar relatórios técnicos em um briefing executivo
voltado para tomada de decisão.

===============================================================
"""

from datetime import datetime


class AnchorEngine:

    def __init__(self):

        self.nome = "Farabulini"

        self.empresa = "IOTEC"

        self.status = "ESTÁVEL"


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

        print("O Núcleo Executivo concluiu mais um ciclo de monitoramento.")

        print()

        print(f"Horário da atualização: {datetime.now()}")

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

        print("RECOMENDAÇÕES")

        print()

        for item in lista:

            print(f"• {item}")

        print()

        print("-" * 70)


    def encerramento(self):

        print()

        print("NÚCLEO EXECUTIVO")

        print()

        print("Monitoramento........ATIVO")

        print("Próxima atualização..10 minutos")

        print()

        print('"Nós monitoramos."')

        print('"Nós analisamos."')

        print('"Nós explicamos."')

        print('"Você decide."')

        print()

        print("=" * 70)



if __name__ == "__main__":

    anchor = AnchorEngine()

    anchor.abertura()

    anchor.status_empresa("ATENÇÃO")

    anchor.narrar(

        "Situação Comercial",

        "O núcleo comercial concluiu a análise das oportunidades registradas. "
        "O pipeline permanece abaixo da meta mensal e ainda não existem contratos assinados neste ciclo."

    )

    anchor.narrar(

        "Impacto",

        "A infraestrutura tecnológica encontra-se estável. "
        "O principal desafio da empresa continua sendo transformar oportunidades em contratos."

    )

    anchor.recomendacoes([

        "Ampliar campanhas comerciais.",

        "Prospectar novos clientes.",

        "Priorizar mercados internacionais.",

        "Acelerar negociações em andamento.",

        "Expandir o portfólio de produtos."

    ])

    anchor.encerramento()
'@

Set-Content `
    -Path $arquivo `
    -Value $codigo `
    -Encoding UTF8

Write-Host ""
Write-Host "==========================================================="
Write-Host "ANCHOR ENGINE CRIADO COM SUCESSO"
Write-Host "==========================================================="
Write-Host ""
Write-Host $arquivo
Write-Host ""
Write-Host "Execute:"
Write-Host ""
Write-Host "python ANCHOR_ENGINE.py"
Write-Host ""