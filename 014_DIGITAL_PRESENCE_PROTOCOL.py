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

014 - DIGITAL PRESENCE PROTOCOL

======================================================================
"""

from datetime import datetime


class DigitalPresenceProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("=" * 70)
        print("IOTEC DIGITAL PRESENCE PROTOCOL")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Garantir que toda presenÃƒÂ§a")
        print("digital da IOTEC transmita")
        print("credibilidade, organizaÃƒÂ§ÃƒÂ£o")
        print("e capacidade profissional.")

        print()

        print("=" * 70)

        print("FILOSOFIA")

        filosofia = [

            "Uma empresa premium deve parecer premium.",

            "Toda comunicaÃƒÂ§ÃƒÂ£o deve transmitir confianÃƒÂ§a.",

            "A marca deve ser consistente em todos os canais.",

            "Toda campanha comeÃƒÂ§a pela presenÃƒÂ§a digital.",

            "O cliente deve compreender rapidamente quem somos."

        ]

        for item in filosofia:

            print("Ã¢Å"â€œ", item)

        print()

        print("=" * 70)

        print("ATIVOS DIGITAIS")

        ativos = [

            "Portal Institucional",

            "Landing Pages",

            "LinkedIn",

            "WhatsApp Business",

            "Instagram",

            "YouTube",

            "E-mail Corporativo",

            "Google Business Profile",

            "DomÃƒÂ­nio Oficial",

            "CRM Comercial"

        ]

        for ativo in ativos:

            print("[ ]", ativo)

        print()

        print("=" * 70)

        print("VERIFICAÃƒâ€¡ÃƒÆ'O")

        verificacoes = [

            "Todos os links respondem.",

            "Contato funcionando.",

            "FormulÃƒÂ¡rios funcionando.",

            "VÃƒÂ­deos publicados.",

            "Logotipo atualizado.",

            "PortfÃƒÂ³lio atualizado.",

            "Produtos publicados.",

            "Tabela comercial disponÃƒÂ­vel.",

            "PolÃƒÂ­tica de privacidade publicada.",

            "InformaÃƒÂ§ÃƒÂµes institucionais consistentes."

        ]

        for item in verificacoes:

            print("Ã¢Å"â€œ", item)

        print()

        print("=" * 70)

        print("PADRÃƒÆ'O VISUAL")

        visual = [

            "Identidade consistente.",

            "Layout moderno.",

            "Boa legibilidade.",

            "Responsivo.",

            "Carregamento rÃƒÂ¡pido.",

            "Linguagem profissional.",

            "NavegaÃƒÂ§ÃƒÂ£o intuitiva."

        ]

        for item in visual:

            print("Ã¢â‚¬Â¢", item)

        print()

        print("=" * 70)

        print("CHECKLIST PRÃƒâ€°-CAMPANHA")

        checklist = [

            "Portal publicado",

            "LinkedIn atualizado",

            "WhatsApp ativo",

            "Instagram atualizado",

            "YouTube atualizado",

            "Landing Pages funcionando",

            "CRM operacional",

            "Recebimento de pagamentos ativo"

        ]

        for item in checklist:

            print("[ ]", item)

        print()

        print("=" * 70)

        print("MISSÃƒÆ'O FINAL")

        print()

        print("Nenhuma campanha deverÃƒÂ¡")
        print("ser iniciada antes que")
        print("a presenÃƒÂ§a digital")
        print("esteja completamente")
        print("operacional.")

        print()

        print("=" * 70)
        print("DIGITAL PRESENCE PROTOCOL CARREGADO")
        print("=" * 70)


if __name__ == "__main__":

    DigitalPresenceProtocol().executar()



