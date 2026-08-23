import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC COMPANY REASONING ENGINE
FASE 06
ETAPA 003

VersÃƒÂ£o 7.0

O Kernel aprende a raciocinar sobre empresas.

======================================================================
"""

from datetime import datetime


class CompanyReasoningEngine:

    VERSION = "7.0"

    def __init__(self):

        self.segmentos = {

            "Tecnologia":{

                "necessidades":[

                    "Grande volume de dados",

                    "IntegraÃƒÂ§ÃƒÂ£o entre sistemas",

                    "Business Intelligence",

                    "Dashboards",

                    "AutomaÃƒÂ§ÃƒÂ£o",

                    "Monitoramento",

                    "Indicadores Executivos"

                ],

                "produtos":[

                    "Dashboard Executivo",

                    "Business Intelligence",

                    "Analytics",

                    "AutomaÃƒÂ§ÃƒÂ£o",

                    "Consultoria"

                ],

                "mensagem":

                "A IOTEC transforma informaÃƒÂ§ÃƒÂµes em inteligÃƒÂªncia para apoiar decisÃƒÂµes estratÃƒÂ©gicas e aumentar a eficiÃƒÂªncia operacional."

            },

            "Energia":{

                "necessidades":[

                    "Monitoramento",

                    "Indicadores",

                    "RelatÃƒÂ³rios",

                    "Centros Operacionais",

                    "AnÃƒÂ¡lise de ProduÃƒÂ§ÃƒÂ£o"

                ],

                "produtos":[

                    "Dashboard",

                    "Analytics",

                    "Business Intelligence",

                    "Monitoramento"

                ],

                "mensagem":

                "A IOTEC integra informaÃƒÂ§ÃƒÂµes operacionais e executivas para fornecer uma visÃƒÂ£o consolidada da operaÃƒÂ§ÃƒÂ£o."

            },

            "Financeiro":{

                "necessidades":[

                    "Indicadores",

                    "AnÃƒÂ¡lise Financeira",

                    "Dashboards",

                    "AutomaÃƒÂ§ÃƒÂ£o",

                    "Compliance"

                ],

                "produtos":[

                    "Dashboard Executivo",

                    "Business Intelligence",

                    "AutomaÃƒÂ§ÃƒÂ£o",

                    "Consultoria"

                ],

                "mensagem":

                "A IOTEC organiza informaÃƒÂ§ÃƒÂµes financeiras para apoiar decisÃƒÂµes rÃƒÂ¡pidas e baseadas em dados."

            },

            "Automotivo":{

                "necessidades":[

                    "ProduÃƒÂ§ÃƒÂ£o",

                    "LogÃƒÂ­stica",

                    "Indicadores",

                    "Qualidade",

                    "Custos"

                ],

                "produtos":[

                    "Business Intelligence",

                    "Analytics",

                    "Dashboard",

                    "Consultoria"

                ],

                "mensagem":

                "A IOTEC auxilia na organizaÃƒÂ§ÃƒÂ£o da informaÃƒÂ§ÃƒÂ£o industrial e no acompanhamento de indicadores estratÃƒÂ©gicos."

            }

        }

    # =======================================================

    def analisar(self, empresa, segmento):

        print()

        print("="*70)

        print("IOTEC COMPANY REASONING ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("EMPRESA")

        print(empresa)

        print()

        print("SEGMENTO")

        print(segmento)

        print()

        if segmento not in self.segmentos:

            print("Segmento ainda nÃƒÂ£o cadastrado.")

            return

        dados = self.segmentos[segmento]

        print("="*70)

        print("NECESSIDADES PROVÃƒÂVEIS")

        print()

        for item in dados["necessidades"]:

            print("Ã¢â‚¬Â¢",item)

        print()

        print("="*70)

        print("PRODUTOS IOTEC MAIS COMPATÃƒÂVEIS")

        print()

        for produto in dados["produtos"]:

            print("Ã¢Å"â€œ",produto)

        print()

        print("="*70)

        print("COMO EXPLICAR AO CLIENTE")

        print()

        print(dados["mensagem"])

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Primeiro compreender.")

        print("Depois recomendar.")

        print("Somente entÃƒÂ£o oferecer.")

        print()

        print("="*70)

        print("COMPANY REASONING ENGINE ONLINE")

        print("="*70)


# ===========================================================

if __name__=="__main__":

    engine = CompanyReasoningEngine()

    engine.analisar(

        empresa="Microsoft",

        segmento="Tecnologia"

    )



