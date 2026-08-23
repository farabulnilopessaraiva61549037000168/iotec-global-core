import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KERNEL LIBRARY
VOLUME II

011 - EXECUTIVE SALES PROTOCOL

======================================================================
"""

from datetime import datetime


class ExecutiveSalesProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("="*70)
        print("IOTEC EXECUTIVE SALES PROTOCOL")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Transformar oportunidades")
        print("em relacionamentos comerciais")
        print("duradouros e sustentÃƒÂ¡veis.")

        print()

        print("="*70)

        print("FILOSOFIA")

        filosofia=[

        "A IOTEC nÃƒÂ£o vende software.",

        "A IOTEC vende soluÃƒÂ§ÃƒÂµes.",

        "A IOTEC vende inteligÃƒÂªncia.",

        "A IOTEC vende capacidade.",

        "A IOTEC vende confianÃƒÂ§a.",

        "A IOTEC vende resultados."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ",f)

        print()

        print("="*70)

        print("CICLO DA VENDA")

        etapas=[

        "Identificar empresa",

        "Compreender contexto",

        "Descobrir necessidades",

        "Mapear decisores",

        "Selecionar produtos",

        "Preparar abordagem",

        "Realizar reuniÃƒÂ£o",

        "Apresentar soluÃƒÂ§ÃƒÂ£o",

        "Responder objeÃƒÂ§ÃƒÂµes",

        "Enviar proposta",

        "Negociar",

        "Fechar contrato",

        "Implantar soluÃƒÂ§ÃƒÂ£o",

        "Acompanhar cliente"

        ]

        for e in etapas:

            print("Ã¢Å"â€œ",e)

        print()

        print("="*70)

        print("ANTES DE VENDER")

        perguntas=[

        "Quem ÃƒÂ© o cliente?",

        "O que ele precisa resolver?",

        "Qual o impacto financeiro?",

        "Existe orÃƒÂ§amento?",

        "Quem decide?",

        "Qual produto possui maior aderÃƒÂªncia?",

        "Qual benefÃƒÂ­cio serÃƒÂ¡ percebido?"

        ]

        for p in perguntas:

            print("Ã¢â‚¬Â¢",p)

        print()

        print("="*70)

        print("NUNCA FAZER")

        regras=[

        "Empurrar produtos.",

        "Prometer resultados impossÃƒÂ­veis.",

        "Esconder limitaÃƒÂ§ÃƒÂµes.",

        "Ignorar necessidades do cliente.",

        "Negociar sem preparaÃƒÂ§ÃƒÂ£o.",

        "Encerrar contato sem registrar histÃƒÂ³rico."

        ]

        for r in regras:

            print("Ã¢Å"â€"",r)

        print()

        print("="*70)

        print("SEMPRE FAZER")

        boas=[

        "Ouvir primeiro.",

        "Compreender o negÃƒÂ³cio.",

        "Falar a linguagem do cliente.",

        "Explicar benefÃƒÂ­cios.",

        "Apresentar evidÃƒÂªncias.",

        "Registrar aprendizados.",

        "Manter relacionamento."

        ]

        for b in boas:

            print("Ã¢Å"â€œ",b)

        print()

        print("="*70)

        print("INDICADORES")

        indicadores=[

        "Leads",

        "Primeiro contato",

        "ReuniÃƒÂµes",

        "Propostas",

        "NegociaÃƒÂ§ÃƒÂµes",

        "Contratos",

        "Receita",

        "RenovaÃƒÂ§ÃƒÂµes",

        "SatisfaÃƒÂ§ÃƒÂ£o",

        "IndicaÃƒÂ§ÃƒÂµes"

        ]

        for i in indicadores:

            print("Ã¢â‚¬Â¢",i)

        print()

        print("="*70)

        print("MISSÃƒÆ'O FINAL")

        print()

        print("Todo cliente deverÃƒÂ¡")
        print("sair da conversa")
        print("compreendendo claramente")
        print("o valor entregue")
        print("pela IOTEC.")

        print()

        print("="*70)
        print("EXECUTIVE SALES PROTOCOL CARREGADO")
        print("="*70)


if __name__=="__main__":

    ExecutiveSalesProtocol().executar()



