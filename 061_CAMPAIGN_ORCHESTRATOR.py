import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CAMPAIGN ORCHESTRATOR
FASE 08

VersÃƒÂ£o 9.0

Orquestrador Inteligente de Campanhas

======================================================================
"""

from datetime import datetime


class CampaignOrchestrator:

    def __init__(self):

        self.canais = {

            "WhatsApp": True,
            "Email": True,
            "LinkedIn": False,
            "Portal": False,
            "Google Business": False

        }

        self.campanhas = [

            {
                "produto":"Business Intelligence",
                "prioridade":"CRÃƒÂTICA",
                "objetivo":"Gerar Leads",
                "canais":["WhatsApp","Email","LinkedIn"]
            },

            {
                "produto":"Dashboards Executivos",
                "prioridade":"ALTA",
                "objetivo":"ApresentaÃƒÂ§ÃƒÂ£o Comercial",
                "canais":["LinkedIn","Portal"]
            },

            {
                "produto":"AutomaÃƒÂ§ÃƒÂ£o Empresarial",
                "prioridade":"ALTA",
                "objetivo":"CaptaÃƒÂ§ÃƒÂ£o",
                "canais":["WhatsApp","Email"]
            },

            {
                "produto":"Consultoria EstratÃƒÂ©gica",
                "prioridade":"MÃƒâ€°DIA",
                "objetivo":"Relacionamento",
                "canais":["LinkedIn","Portal"]
            }

        ]

    # ===================================================

    def executar(self):

        print()
        print("="*70)
        print("IOTEC CAMPAIGN ORCHESTRATOR")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("CAMPANHAS DISPONÃƒÂVEIS")
        print()

        prontas = []

        for campanha in self.campanhas:

            ativos = []

            for canal in campanha["canais"]:

                if self.canais.get(canal,False):
                    ativos.append(canal)

            if ativos:

                prontas.append((campanha,ativos))

                print("Produto........",campanha["produto"])
                print("Objetivo.......",campanha["objetivo"])
                print("Prioridade.....",campanha["prioridade"])
                print("Canais.........",", ".join(ativos))
                print("Status......... PRONTA")
                print()

        print("="*70)
        print("RESUMO")
        print()

        print("Campanhas prontas.....",len(prontas))
        print()

        print("="*70)
        print("AÃƒâ€¡ÃƒÆ'O DO KERNEL")
        print()

        if prontas:

            campanha = prontas[0][0]

            print("Campanha priorizada:")

            print()

            print(campanha["produto"])

            print()

            print("PrÃƒÂ³ximas etapas:")

            print()

            print("Ã¢Å"â€œ Gerar conteÃƒÂºdo")

            print("Ã¢Å"â€œ Preparar mensagens")

            print("Ã¢Å"â€œ Enviar para aprovaÃƒÂ§ÃƒÂ£o")

            print("Ã¢Å"â€œ Publicar")

            print("Ã¢Å"â€œ Monitorar leads")

        else:

            print("Nenhuma campanha pode ser executada.")

        print()

        print("="*70)
        print("FILOSOFIA")
        print()

        print("O Kernel nÃƒÂ£o publica campanhas.")

        print("Ele identifica oportunidades,")

        print("prioriza aÃƒÂ§ÃƒÂµes")

        print("e prepara a execuÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)
        print("CAMPAIGN ORCHESTRATOR ONLINE")
        print("="*70)


if __name__=="__main__":

    CampaignOrchestrator().executar()



