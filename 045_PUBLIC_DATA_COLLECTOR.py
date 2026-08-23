import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC PUBLIC DATA COLLECTOR
FASE 07
ETAPA 002

VersÃƒÂ£o 8.0

Centro de Coleta de Dados PÃƒÂºblicos

======================================================================
"""

from datetime import datetime


class PublicDataCollector:

    VERSION = "8.0"

    def __init__(self):

        self.fontes = [

            {
                "nome":"Site Oficial",
                "tipo":"Institucional",
                "status":"AGUARDANDO IMPLEMENTAÃƒâ€¡ÃƒÆ'O"
            },

            {
                "nome":"LinkedIn Corporativo",
                "tipo":"Corporativo",
                "status":"AGUARDANDO IMPLEMENTAÃƒâ€¡ÃƒÆ'O"
            },

            {
                "nome":"Portal Governamental",
                "tipo":"Dados PÃƒÂºblicos",
                "status":"AGUARDANDO IMPLEMENTAÃƒâ€¡ÃƒÆ'O"
            },

            {
                "nome":"API PÃƒÂºblica",
                "tipo":"IntegraÃƒÂ§ÃƒÂ£o",
                "status":"AGUARDANDO IMPLEMENTAÃƒâ€¡ÃƒÆ'O"
            },

            {
                "nome":"Banco Corporativo Interno",
                "tipo":"IOTEC",
                "status":"ONLINE"
            }

        ]

    # =======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC PUBLIC DATA COLLECTOR")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("FONTES DE DADOS")

        print()

        online = 0

        for numero, fonte in enumerate(self.fontes,1):

            print(f"[{numero:02d}] {fonte['nome']}")

            print("     Tipo.......",fonte["tipo"])

            print("     Status.....",fonte["status"])

            print()

            if fonte["status"] == "ONLINE":
                online += 1

        print("="*70)

        print("RESUMO")

        print()

        print("Fontes cadastradas.....",len(self.fontes))

        print("Online.................",online)

        print("Pendentes..............",len(self.fontes)-online)

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Coletar informaÃƒÂ§ÃƒÂµes")

        print("pÃƒÂºblicas, confiÃƒÂ¡veis")

        print("e verificÃƒÂ¡veis,")

        print("para enriquecer")

        print("o conhecimento")

        print("corporativo da IOTEC.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMAS ETAPAS")

        print()

        print("Ã¢Å"â€œ ValidaÃƒÂ§ÃƒÂ£o")

        print("Ã¢Å"â€œ NormalizaÃƒÂ§ÃƒÂ£o")

        print("Ã¢Å"â€œ Enriquecimento")

        print("Ã¢Å"â€œ AtualizaÃƒÂ§ÃƒÂ£o do Banco")

        print("Ã¢Å"â€œ GeraÃƒÂ§ÃƒÂ£o do DossiÃƒÂª")

        print()

        print("="*70)

        print("PUBLIC DATA COLLECTOR ONLINE")

        print("="*70)


if __name__ == "__main__":

    PublicDataCollector().executar()



