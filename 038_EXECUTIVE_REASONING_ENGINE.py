import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EXECUTIVE REASONING ENGINE
FASE 06
ETAPA 004

VersÃƒÂ£o 7.0

O Kernel aprende a pensar
como um consultor executivo.

======================================================================
"""

from datetime import datetime


class ExecutiveReasoningEngine:

    VERSION = "7.0"

    def __init__(self):

        self.base = {

            "Tecnologia":{

                "compreensao":

                "Empresas de tecnologia operam em ambientes altamente dinÃƒÂ¢micos, lidando com grandes volumes de dados, inovaÃƒÂ§ÃƒÂ£o contÃƒÂ­nua e necessidade permanente de integraÃƒÂ§ÃƒÂ£o.",

                "desafios":[

                    "Crescimento acelerado",

                    "IntegraÃƒÂ§ÃƒÂ£o entre sistemas",

                    "Tomada de decisÃƒÂ£o rÃƒÂ¡pida",

                    "Grandes volumes de indicadores",

                    "Escalabilidade"

                ],

                "valor":[

                    "CentralizaÃƒÂ§ÃƒÂ£o de indicadores",

                    "Business Intelligence",

                    "Dashboards",

                    "AutomaÃƒÂ§ÃƒÂ£o",

                    "AnÃƒÂ¡lise EstratÃƒÂ©gica"

                ],

                "beneficios":[

                    "Maior controle operacional",

                    "ReduÃƒÂ§ÃƒÂ£o do tempo de anÃƒÂ¡lise",

                    "Melhor qualidade das decisÃƒÂµes",

                    "VisÃƒÂ£o executiva integrada"

                ]

            }

        }

    # ===========================================================

    def analisar(self,empresa,segmento):

        print()

        print("="*70)
        print("IOTEC EXECUTIVE REASONING ENGINE")
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

        if segmento not in self.base:

            print("Segmento ainda nÃƒÂ£o modelado.")

            return

        dados=self.base[segmento]

        print("="*70)

        print("O QUE A IOTEC COMPREENDE")

        print()

        print(dados["compreensao"])

        print()

        print("="*70)

        print("DESAFIOS PROVÃƒÂVEIS")

        print()

        for desafio in dados["desafios"]:

            print("Ã¢â‚¬Â¢",desafio)

        print()

        print("="*70)

        print("ONDE A IOTEC PODE GERAR VALOR")

        print()

        for valor in dados["valor"]:

            print("Ã¢Å"â€œ",valor)

        print()

        print("="*70)

        print("BENEFÃƒÂCIOS ESPERADOS")

        print()

        for beneficio in dados["beneficios"]:

            print("Ã¢Å"â€œ",beneficio)

        print()

        print("="*70)

        print("PARECER EXECUTIVO")

        print()

        print(

        f"A anÃƒÂ¡lise inicial indica que {empresa} "

        "possui caracterÃƒÂ­sticas compatÃƒÂ­veis com "

        "soluÃƒÂ§ÃƒÂµes de inteligÃƒÂªncia, organizaÃƒÂ§ÃƒÂ£o "

        "de informaÃƒÂ§ÃƒÂµes, automaÃƒÂ§ÃƒÂ£o e apoio ÃƒÂ  "

        "tomada de decisÃƒÂ£o. "

        "A recomendaÃƒÂ§ÃƒÂ£o ÃƒÂ© aprofundar o estudo "

        "da organizaÃƒÂ§ÃƒÂ£o e elaborar uma proposta "

        "personalizada baseada em necessidades "

        "identificadas."

        )

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA AÃƒâ€¡ÃƒÆ'O")

        print()

        print("Ã¢Å"â€œ Estudar a empresa.")

        print("Ã¢Å"â€œ Identificar necessidades especÃƒÂ­ficas.")

        print("Ã¢Å"â€œ Priorizar oportunidades.")

        print("Ã¢Å"â€œ Preparar proposta personalizada.")

        print("Ã¢Å"â€œ Agendar contato comercial.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("A IOTEC nÃƒÂ£o vende software.")

        print("A IOTEC compreende organizaÃƒÂ§ÃƒÂµes,")

        print("gera inteligÃƒÂªncia")

        print("e entrega soluÃƒÂ§ÃƒÂµes.")

        print()

        print("="*70)

        print("EXECUTIVE REASONING ONLINE")

        print("="*70)


# ===============================================================

if __name__=="__main__":

    engine=ExecutiveReasoningEngine()

    engine.analisar(

        empresa="Microsoft",

        segmento="Tecnologia"

    )



