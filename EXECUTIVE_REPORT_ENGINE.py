import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================

EXECUTIVE REPORT ENGINE

IOTEC GLOBAL CORE

===============================================================

MISSÃƒO

Traduzir todas as informaÃ§Ãµes tÃ©cnicas da plataforma
para linguagem executiva compreensÃ­vel por seres humanos.

Todo motor da IOTEC deverÃ¡ conversar com este mÃ³dulo.

Este mÃ³dulo produzirÃ¡:

â€¢ PlantÃµes
â€¢ RelatÃ³rios
â€¢ Briefings
â€¢ Resumos
â€¢ RecomendaÃ§Ãµes
â€¢ ExplicaÃ§Ãµes

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

        print("Fim do PlantÃ£o Executivo")

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

        self.header("PLANTÃƒO EXECUTIVO")

        print()

        print("SituaÃ§Ã£o Comercial")

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

            print("ANÃLISE")

            print()

            print("O volume atual de oportunidades")

            print("estÃ¡ abaixo do necessÃ¡rio")

            print("para atingir a meta mensal.")

            print()

            print("RECOMENDAÃ‡Ã•ES")

            print()

            print("- Intensificar prospecÃ§Ã£o.")

            print("- Ativar novas campanhas.")

            print("- Buscar mercados internacionais.")

            print("- Priorizar clientes governamentais.")

        elif percentual < 70:

            print()

            print("SituaÃ§Ã£o em evoluÃ§Ã£o.")

            print("A empresa estÃ¡ aumentando")

            print("o pipeline comercial.")

        else:

            print()

            print("Excelente desempenho.")

            print("A meta encontra-se")

            print("dentro da projeÃ§Ã£o.")

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




