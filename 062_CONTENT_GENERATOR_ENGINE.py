import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CONTENT GENERATOR ENGINE
FASE 08

VersÃƒÂ£o 9.0

Gerador de ConteÃƒÂºdo Comercial

======================================================================
"""

from datetime import datetime


class ContentGenerator:

    def __init__(self):

        self.produto = "Business Intelligence"

        self.publico = "Empresas"

        self.canal = "WhatsApp"

        self.objetivo = "Gerar Leads"

    # =====================================================

    def gerar_titulo(self):

        return f"Transforme dados em decisÃƒÂµes inteligentes"

    # =====================================================

    def gerar_texto(self):

        return f"""
Sua empresa possui informaÃƒÂ§ÃƒÂµes espalhadas em planilhas,
sistemas ou bancos de dados?

A IOTEC ajuda organizaÃƒÂ§ÃƒÂµes a transformar esses dados
em inteligÃƒÂªncia para apoiar decisÃƒÂµes mais rÃƒÂ¡pidas,
reduzir desperdÃƒÂ­cios e aumentar a eficiÃƒÂªncia.

ConheÃƒÂ§a nossas soluÃƒÂ§ÃƒÂµes em:

Ã¢â‚¬Â¢ Business Intelligence
Ã¢â‚¬Â¢ Dashboards Executivos
Ã¢â‚¬Â¢ AutomaÃƒÂ§ÃƒÂ£o
Ã¢â‚¬Â¢ Analytics
Ã¢â‚¬Â¢ Consultoria EstratÃƒÂ©gica

Se desejar uma conversa sem compromisso,
responda esta mensagem e agendaremos uma apresentaÃƒÂ§ÃƒÂ£o.
"""

    # =====================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC CONTENT GENERATOR ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("PRODUTO")

        print(self.produto)

        print()

        print("CANAL")

        print(self.canal)

        print()

        print("OBJETIVO")

        print(self.objetivo)

        print()

        print("="*70)

        print("TÃƒÂTULO")

        print()

        print(self.gerar_titulo())

        print()

        print("="*70)

        print("MENSAGEM")

        print(self.gerar_texto())

        print("="*70)

        print("STATUS")

        print()

        print("RASCUNHO PRONTO PARA APROVAÃƒâ€¡ÃƒÆ'O")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA ETAPA")

        print()

        print("Enviar para fila de aprovaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("CONTENT GENERATOR ONLINE")

        print("="*70)


if __name__ == "__main__":

    ContentGenerator().executar()



