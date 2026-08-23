import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC VALUE TRANSLATION ENGINE
FASE 06
ETAPA 002

VersÃƒÂ£o 7.0

Traduz capacidades tÃƒÂ©cnicas
para linguagem comercial.

======================================================================
"""

from datetime import datetime


class ValueTranslationEngine:

    VERSION = "7.0"

    def __init__(self):

        self.produtos = [

            {

                "produto":"Dashboard Executivo",

                "tecnico":"CentralizaÃƒÂ§ÃƒÂ£o de indicadores corporativos.",

                "executivo":"VisÃƒÂ£o estratÃƒÂ©gica do negÃƒÂ³cio.",

                "cliente":"VocÃƒÂª acompanha sua empresa em um ÃƒÂºnico painel.",

                "resultado":"Mais controle e decisÃƒÂµes mais rÃƒÂ¡pidas."

            },

            {

                "produto":"Business Intelligence",

                "tecnico":"AnÃƒÂ¡lise inteligente de dados.",

                "executivo":"IdentificaÃƒÂ§ÃƒÂ£o de oportunidades.",

                "cliente":"VocÃƒÂª descobre onde ganhar mais dinheiro.",

                "resultado":"Maior eficiÃƒÂªncia comercial."

            },

            {

                "produto":"AutomaÃƒÂ§ÃƒÂ£o",

                "tecnico":"AutomatizaÃƒÂ§ÃƒÂ£o de processos repetitivos.",

                "executivo":"ReduÃƒÂ§ÃƒÂ£o de custos operacionais.",

                "cliente":"Sua equipe trabalha menos com tarefas repetitivas.",

                "resultado":"Mais produtividade."

            },

            {

                "produto":"Consultoria",

                "tecnico":"DiagnÃƒÂ³stico organizacional.",

                "executivo":"IdentificaÃƒÂ§ÃƒÂ£o de melhorias.",

                "cliente":"Receba recomendaÃƒÂ§ÃƒÂµes claras para evoluir sua empresa.",

                "resultado":"Maior competitividade."

            },

            {

                "produto":"AnÃƒÂ¡lise de Dados",

                "tecnico":"Tratamento e organizaÃƒÂ§ÃƒÂ£o de dados.",

                "executivo":"TransformaÃƒÂ§ÃƒÂ£o de dados em inteligÃƒÂªncia.",

                "cliente":"VocÃƒÂª entende melhor o que estÃƒÂ¡ acontecendo no seu negÃƒÂ³cio.",

                "resultado":"DecisÃƒÂµes baseadas em informaÃƒÂ§ÃƒÂµes."

            }

        ]

    # ===========================================================

    def executar(self):

        print()

        print("="*70)

        print("IOTEC VALUE TRANSLATION ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        for produto in self.produtos:

            print("PRODUTO")

            print(produto["produto"])

            print()

            print("LINGUAGEM TÃƒâ€°CNICA")

            print(produto["tecnico"])

            print()

            print("LINGUAGEM EXECUTIVA")

            print(produto["executivo"])

            print()

            print("LINGUAGEM DO CLIENTE")

            print(produto["cliente"])

            print()

            print("VALOR ENTREGUE")

            print(produto["resultado"])

            print()

            print("-"*70)

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Toda capacidade tÃƒÂ©cnica")

        print("deverÃƒÂ¡ ser traduzida")

        print("para uma linguagem")

        print("que o cliente compreenda.")

        print()

        print("="*70)

        print("VALUE TRANSLATION ENGINE ONLINE")

        print("="*70)


# ===============================================================

if __name__=="__main__":

    ValueTranslationEngine().executar()



