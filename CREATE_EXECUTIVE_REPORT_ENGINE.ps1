Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC EXECUTIVE REPORT ENGINE"
Write-Host " STAGE 001"
Write-Host "==============================================="
Write-Host ""

$arquivo = "C:\IOTEC\EXECUTIVE_REPORT_ENGINE.py"

$codigo = @'
"""
===============================================================

EXECUTIVE REPORT ENGINE

IOTEC GLOBAL CORE

===============================================================

MISSÃO

Traduzir todas as informações técnicas da plataforma
para linguagem executiva compreensível por seres humanos.

Todo motor da IOTEC deverá conversar com este módulo.

Este módulo produzirá:

• Plantões
• Relatórios
• Briefings
• Resumos
• Recomendações
• Explicações

===============================================================
"""

from datetime import datetime


class ExecutiveReporter:


    def __init__(self):

        self.version = "2.0"

        self.platform = "IOTEC"



    def header(self,titulo):

        print()

        print("="*70)

        print(titulo.upper())

        print(datetime.now())

        print("="*70)


    def footer(self):

        print()

        print("-"*70)

        print("Fim do Plantão Executivo")

        print("-"*70)



    def commercial_report(

        self,

        pipeline,

        receita,

        meta,

        contratos,

        propostas,

        campanhas

    ):

        self.header("PLANTÃO EXECUTIVO")

        print()

        print("Situação Comercial")

        print()

        print(f"Pipeline Comercial : R$ {pipeline:,.2f}")

        print(f"Receita Contratada : R$ {receita:,.2f}")

        print(f"Meta Mensal         : R$ {meta:,.2f}")

        print(f"Contratos           : {contratos}")

        print(f"Propostas           : {propostas}")

        print(f"Campanhas           : {campanhas}")

        print()

        percentual = 0

        if meta>0:

            percentual=(pipeline/meta)*100

        print(f"Atingimento Atual   : {percentual:.2f}%")

        print()

        if percentual < 20:

            print("ANÁLISE")

            print()

            print("O volume atual de oportunidades")

            print("está abaixo do necessário")

            print("para atingir a meta mensal.")

            print()

            print("RECOMENDAÇÕES")

            print()

            print("- Intensificar prospecção.")

            print("- Ativar novas campanhas.")

            print("- Buscar mercados internacionais.")

            print("- Priorizar clientes governamentais.")

        elif percentual < 70:

            print()

            print("Situação em evolução.")

            print("A empresa está aumentando")

            print("o pipeline comercial.")

        else:

            print()

            print("Excelente desempenho.")

            print("A meta encontra-se")

            print("dentro da projeção.")

        self.footer()


if __name__=="__main__":


    r=ExecutiveReporter()


    r.commercial_report(

        pipeline=17500,

        receita=0,

        meta=5000000,

        contratos=0,

        propostas=0,

        campanhas=0

    )
'@

Set-Content `
    -Path $arquivo `
    -Value $codigo `
    -Encoding UTF8

Write-Host ""
Write-Host "==============================================="
Write-Host "ARQUIVO CRIADO"
Write-Host "==============================================="
Write-Host ""

Write-Host $arquivo

Write-Host ""

Write-Host "Execute:"

Write-Host ""

Write-Host "python EXECUTIVE_REPORT_ENGINE.py"

Write-Host ""