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

013 - CAMPAIGN ORCHESTRATION PROTOCOL

======================================================================
"""

from datetime import datetime


class CampaignOrchestrationProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("=" * 70)
        print("IOTEC CAMPAIGN ORCHESTRATION PROTOCOL")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Planejar, executar, acompanhar")
        print("e aperfeiÃƒÂ§oar continuamente")
        print("as campanhas comerciais")
        print("da IOTEC.")

        print()

        print("=" * 70)

        print("FILOSOFIA")

        filosofia = [

            "Toda campanha deverÃƒÂ¡ possuir objetivo.",

            "Toda campanha deverÃƒÂ¡ possuir pÃƒÂºblico.",

            "Toda campanha deverÃƒÂ¡ possuir indicadores.",

            "Toda campanha deverÃƒÂ¡ gerar aprendizado.",

            "Nenhuma campanha ficarÃƒÂ¡ sem acompanhamento."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ", f)

        print()

        print("=" * 70)

        print("OBJETIVOS POSSÃƒÂVEIS")

        objetivos = [

            "Gerar Leads",

            "Agendar ReuniÃƒÂµes",

            "Apresentar Produtos",

            "Fortalecer Marca",

            "Gerar Propostas",

            "Fechar Contratos",

            "Expandir Mercado",

            "Atrair Parceiros"

        ]

        for o in objetivos:

            print("Ã¢â‚¬Â¢", o)

        print()

        print("=" * 70)

        print("CANAIS DE DIVULGAÃƒâ€¡ÃƒÆ'O")

        canais = [

            "Portal Institucional",

            "LinkedIn",

            "WhatsApp Business",

            "Instagram",

            "YouTube",

            "E-mail Corporativo",

            "Google Business Profile",

            "Eventos",

            "ReuniÃƒÂµes",

            "Networking"

        ]

        for c in canais:

            print("Ã¢Å"â€œ", c)

        print()

        print("=" * 70)

        print("CHECKLIST")

        checklist = [

            "Produto definido",

            "PÃƒÂºblico definido",

            "Mensagem definida",

            "Material preparado",

            "Landing Page pronta",

            "FormulÃƒÂ¡rio funcionando",

            "WhatsApp operacional",

            "CRM conectado",

            "Pagamento disponÃƒÂ­vel",

            "Indicadores configurados"

        ]

        for item in checklist:

            print("[ ]", item)

        print()

        print("=" * 70)

        print("INDICADORES")

        indicadores = [

            "VisualizaÃƒÂ§ÃƒÂµes",

            "Cliques",

            "Leads",

            "ConversÃƒÂµes",

            "ReuniÃƒÂµes",

            "Propostas",

            "Contratos",

            "Receita",

            "ROI"

        ]

        for indicador in indicadores:

            print("Ã¢Å"â€œ", indicador)

        print()

        print("=" * 70)

        print("ENCERRAMENTO")

        print()

        print("Toda campanha deverÃƒÂ¡ produzir")
        print("um relatÃƒÂ³rio executivo")
        print("contendo aprendizados")
        print("e recomendaÃƒÂ§ÃƒÂµes")
        print("para a prÃƒÂ³xima campanha.")

        print()

        print("=" * 70)
        print("CAMPAIGN ORCHESTRATION CARREGADA")
        print("=" * 70)


if __name__ == "__main__":

    CampaignOrchestrationProtocol().executar()



