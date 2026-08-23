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

012 - CLIENT DISCOVERY PROTOCOL

======================================================================
"""

from datetime import datetime


class ClientDiscoveryProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("="*70)
        print("IOTEC CLIENT DISCOVERY PROTOCOL")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Descobrir organizaÃƒÂ§ÃƒÂµes")
        print("que possuem necessidades")
        print("compatÃƒÂ­veis com os produtos")
        print("e serviÃƒÂ§os da IOTEC.")

        print()

        print("="*70)

        print("FILOSOFIA")

        filosofia=[

        "Nem toda empresa ÃƒÂ© cliente.",

        "Nem todo cliente possui aderÃƒÂªncia.",

        "O Kernel deverÃƒÂ¡ encontrar os clientes ideais.",

        "Qualidade ÃƒÂ© mais importante que quantidade.",

        "Conhecimento aumenta a conversÃƒÂ£o."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ",f)

        print()

        print("="*70)

        print("PERFIL IDEAL")

        perfil=[

        "Segmento",

        "Porte",

        "NÃƒÂºmero de colaboradores",

        "Faturamento estimado",

        "LocalizaÃƒÂ§ÃƒÂ£o",

        "NÃƒÂ­vel de maturidade digital",

        "Necessidade de tecnologia",

        "Capacidade de investimento",

        "UrgÃƒÂªncia",

        "Potencial de recorrÃƒÂªncia"

        ]

        for p in perfil:

            print("Ã¢â‚¬Â¢",p)

        print()

        print("="*70)

        print("DECISORES")

        decisores=[

        "CEO",

        "Diretor",

        "Gerente",

        "Coordenador",

        "Compras",

        "Tecnologia",

        "Financeiro",

        "OperaÃƒÂ§ÃƒÂµes",

        "TransformaÃƒÂ§ÃƒÂ£o Digital"

        ]

        for d in decisores:

            print("Ã¢Å"â€œ",d)

        print()

        print("="*70)

        print("PERGUNTAS")

        perguntas=[

        "Quem decide?",

        "Quem influencia?",

        "Quem utilizarÃƒÂ¡ a soluÃƒÂ§ÃƒÂ£o?",

        "Quem aprova o orÃƒÂ§amento?",

        "Qual o principal problema?",

        "Existe urgÃƒÂªncia?",

        "Existe orÃƒÂ§amento disponÃƒÂ­vel?",

        "Existe potencial de parceria?"

        ]

        for p in perguntas:

            print("Ã¢Å"â€œ",p)

        print()

        print("="*70)

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ Cliente EstratÃƒÂ©gico")

        print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ Cliente PrioritÃƒÂ¡rio")

        print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ Cliente Potencial")

        print("Ã¢Ëœâ€¦Ã¢Ëœâ€¦ Cliente em ObservaÃƒÂ§ÃƒÂ£o")

        print("Ã¢Ëœâ€¦ Cliente Futuro")

        print()

        print("="*70)

        print("MISSÃƒÆ'O FINAL")

        print()

        print("Encontrar as organizaÃƒÂ§ÃƒÂµes")

        print("onde a IOTEC poderÃƒÂ¡")

        print("gerar maior valor")

        print("e construir relacionamentos")

        print("de longo prazo.")

        print()

        print("="*70)
        print("CLIENT DISCOVERY CARREGADO")
        print("="*70)


if __name__=="__main__":

    ClientDiscoveryProtocol().executar()



