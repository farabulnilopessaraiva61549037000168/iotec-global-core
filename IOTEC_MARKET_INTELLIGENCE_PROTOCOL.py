import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC MARKET INTELLIGENCE PROTOCOL

PROTOCOLO DE INTELIGÃƒÅ NCIA DE MERCADO

VersÃƒÂ£o 1.0

==============================================================
"""

from datetime import datetime


class MarketIntelligenceProtocol:

    def executar(self):

        print("="*70)
        print("IOTEC MARKET INTELLIGENCE PROTOCOL")
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("A IOTEC existe para identificar oportunidades,")
        print("compreender organizaÃƒÂ§ÃƒÂµes,")
        print("gerar inteligÃƒÂªncia")
        print("e transformar conhecimento em contratos.")
        print()

        print("-"*70)

        print()
        print("PRINCÃƒÂPIOS")

        principios=[

        "Toda empresa ÃƒÂ© uma oportunidade potencial.",

        "Toda oportunidade deve ser estudada.",

        "Toda empresa possui necessidades.",

        "Toda necessidade pode gerar um serviÃƒÂ§o.",

        "Toda soluÃƒÂ§ÃƒÂ£o gera valor.",

        "O valor entregue sustenta a monetizaÃƒÂ§ÃƒÂ£o.",

        "A IOTEC vende capacidade e inteligÃƒÂªncia.",

        "O foco comercial ÃƒÂ© gerar contratos.",

        "Toda negociaÃƒÂ§ÃƒÂ£o produz aprendizado.",

        "O nÃƒÂºcleo deve aprender continuamente."

        ]

        for p in principios:

            print("Ã¢Å"â€œ",p)

        print()

        print("-"*70)

        print()

        print("COMO ANALISAR UMA EMPRESA")

        perguntas=[

        "Quem ÃƒÂ© a empresa?",

        "Qual o paÃƒÂ­s de origem?",

        "Quais produtos fabrica?",

        "Quais serviÃƒÂ§os oferece?",

        "Como recruta pessoas?",

        "Quais tecnologias utiliza?",

        "Quais desafios enfrenta?",

        "Onde a IOTEC pode gerar valor?",

        "Existe oportunidade comercial?",

        "Qual a prÃƒÂ³xima aÃƒÂ§ÃƒÂ£o?"

        ]

        for p in perguntas:

            print("Ã¢â‚¬Â¢",p)

        print()

        print("-"*70)

        print()

        print("REGRA DE MONETIZAÃƒâ€¡ÃƒÆ'O")

        print()

        print("A IOTEC nÃƒÂ£o vende cÃƒÂ³digo.")

        print("A IOTEC vende resultados.")

        print()

        print("Clientes compram:")

        print()

        print("- OrganizaÃƒÂ§ÃƒÂ£o")

        print("- InteligÃƒÂªncia")

        print("- AutomaÃƒÂ§ÃƒÂ£o")

        print("- Dashboards")

        print("- Consultoria")

        print("- EficiÃƒÂªncia")

        print("- Apoio ÃƒÂ  decisÃƒÂ£o")

        print()

        print("-"*70)

        print()

        print("MISSÃƒÆ'O FINAL")

        print()

        print("Transformar inteligÃƒÂªncia")

        print("em receita.")

        print()

        print("Transformar oportunidades")

        print("em contratos.")

        print()

        print("="*70)

        print("PROTOCOLO CARREGADO COM SUCESSO")

        print("="*70)


if __name__=="__main__":

    MarketIntelligenceProtocol().executar()



