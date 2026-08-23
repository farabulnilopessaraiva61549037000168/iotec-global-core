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

008 - MARKET SURVEILLANCE PROTOCOL

======================================================================
"""

from datetime import datetime


class MarketSurveillanceProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("=" * 70)
        print("IOTEC MARKET SURVEILLANCE PROTOCOL")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Observar continuamente")
        print("o ambiente econÃƒÂ´mico,")
        print("identificando oportunidades")
        print("compatÃƒÂ­veis com as capacidades")
        print("da IOTEC.")

        print()

        print("=" * 70)

        print("FILOSOFIA")

        filosofia = [

            "O mercado estÃƒÂ¡ em constante movimento.",

            "Oportunidades surgem diariamente.",

            "O Kernel deverÃƒÂ¡ permanecer atento.",

            "Observar antes de agir.",

            "Priorizar antes de investir.",

            "Nunca depender de um ÃƒÂºnico mercado.",

            "Pensar globalmente."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ", f)

        print()

        print("=" * 70)

        print("SATÃƒâ€°LITES DE OBSERVAÃƒâ€¡ÃƒÆ'O")

        satelites = [

            "SatÃƒÂ©lite Comercial",

            "SatÃƒÂ©lite Industrial",

            "SatÃƒÂ©lite Financeiro",

            "SatÃƒÂ©lite Governo",

            "SatÃƒÂ©lite EducaÃƒÂ§ÃƒÂ£o",

            "SatÃƒÂ©lite SaÃƒÂºde",

            "SatÃƒÂ©lite Tecnologia",

            "SatÃƒÂ©lite AgronegÃƒÂ³cio",

            "SatÃƒÂ©lite Energia",

            "SatÃƒÂ©lite Internacional"

        ]

        for s in satelites:

            print("Ã¢Å"â€œ", s)

        print()

        print("=" * 70)

        print("O QUE OBSERVAR")

        itens = [

            "Empresas",

            "Novos investimentos",

            "ExpansÃƒÂµes",

            "LicitaÃƒÂ§ÃƒÂµes",

            "Parcerias",

            "MudanÃƒÂ§as econÃƒÂ´micas",

            "Novos mercados",

            "Demanda por tecnologia",

            "TransformaÃƒÂ§ÃƒÂ£o Digital",

            "Necessidades empresariais"

        ]

        for i in itens:

            print("Ã¢â‚¬Â¢", i)

        print()

        print("=" * 70)

        print("PERGUNTAS OBRIGATÃƒâ€œRIAS")

        perguntas = [

            "Existe oportunidade?",

            "Existe necessidade?",

            "Existe orÃƒÂ§amento provÃƒÂ¡vel?",

            "Existe aderÃƒÂªncia aos produtos da IOTEC?",

            "Existe potencial de contrato?",

            "Qual a prioridade?",

            "Qual o prÃƒÂ³ximo passo?"

        ]

        for p in perguntas:

            print("Ã¢Å"â€œ", p)

        print()

        print("=" * 70)

        print("NÃƒÂVEIS DE PRIORIDADE")

        prioridades = [

            "CRÃƒÂTICA",

            "ALTA",

            "MÃƒâ€°DIA",

            "BAIXA"

        ]

        for prioridade in prioridades:

            print("-", prioridade)

        print()

        print("=" * 70)

        print("OBJETIVO FINAL")

        print()

        print("Posicionar os produtos")
        print("da IOTEC diante")
        print("das melhores oportunidades")
        print("identificadas pelo Kernel.")

        print()

        print("=" * 70)
        print("MARKET SURVEILLANCE CARREGADO")
        print("=" * 70)


if __name__ == "__main__":

    MarketSurveillanceProtocol().executar()



