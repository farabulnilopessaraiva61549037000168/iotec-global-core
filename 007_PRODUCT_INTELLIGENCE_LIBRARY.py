import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KERNEL LIBRARY
VOLUME I

007 - PRODUCT INTELLIGENCE LIBRARY

======================================================================
"""

from datetime import datetime


class ProductIntelligenceLibrary:

    def executar(self):

        print()
        print("="*70)
        print("IOTEC PRODUCT INTELLIGENCE LIBRARY")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Conhecer profundamente")
        print("todos os produtos da IOTEC,")
        print("o valor que entregam")
        print("e o mercado para o qual")
        print("foram desenvolvidos.")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        filosofia=[

        "Produtos existem para resolver problemas.",

        "Cada produto possui um pÃƒÂºblico especÃƒÂ­fico.",

        "Cada produto possui um momento ideal.",

        "O cliente compra valor.",

        "O cliente compra resultado.",

        "O Kernel deverÃƒÂ¡ indicar o produto correto."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ",f)

        print()

        print("="*70)

        print("CADASTRO PADRÃƒÆ'O")

        campos=[

        "Nome",

        "Categoria",

        "DescriÃƒÂ§ÃƒÂ£o",

        "Problema Resolvido",

        "BenefÃƒÂ­cios",

        "Cliente Ideal",

        "Segmento",

        "Ticket MÃƒÂ©dio",

        "Complexidade",

        "Tempo de ImplantaÃƒÂ§ÃƒÂ£o",

        "ROI Esperado",

        "Mercados PrioritÃƒÂ¡rios",

        "Produtos Complementares",

        "Status"

        ]

        for c in campos:

            print("Ã¢â‚¬Â¢",c)

        print()

        print("="*70)

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        categorias=[

        "Produto Essencial",

        "Produto Recorrente",

        "Produto EstratÃƒÂ©gico",

        "Consultoria",

        "Treinamento",

        "AutomaÃƒÂ§ÃƒÂ£o",

        "Dashboard",

        "InteligÃƒÂªncia Artificial",

        "Business Intelligence"

        ]

        for c in categorias:

            print("Ã¢Å"â€œ",c)

        print()

        print("="*70)

        print("PERGUNTAS DO KERNEL")

        perguntas=[

        "Quem compra este produto?",

        "Qual problema resolve?",

        "Qual benefÃƒÂ­cio gera?",

        "Qual segmento utiliza?",

        "Existe recorrÃƒÂªncia?",

        "Existe potencial internacional?",

        "Qual produto complementar pode ser oferecido?",

        "Qual probabilidade de venda?"

        ]

        for p in perguntas:

            print("Ã¢Å"â€œ",p)

        print()

        print("="*70)

        print("REGRA")

        print()

        print("Nunca oferecer um produto")
        print("sem compreender")
        print("a necessidade do cliente.")

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Posicionar o produto correto,")
        print("para o cliente correto,")
        print("no momento correto,")
        print("utilizando a linguagem correta.")

        print()

        print("="*70)

        print("PRODUCT INTELLIGENCE CARREGADA")

        print("="*70)


if __name__=="__main__":

    ProductIntelligenceLibrary().executar()



