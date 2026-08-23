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

Verso 9.0

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
                "prioridade":"CRTICA",
                "objetivo":"Gerar Leads",
                "canais":["WhatsApp","Email","LinkedIn"]
            },

            {
                "produto":"Dashboards Executivos",
                "prioridade":"ALTA",
                "objetivo":"Apresentao Comercial",
                "canais":["LinkedIn","Portal"]
            },

            {
                "produto":"Automao Empresarial",
                "prioridade":"ALTA",
                "objetivo":"Captao",
                "canais":["WhatsApp","Email"]
            },

            {
                "produto":"Consultoria Estratgica",
                "prioridade":"MDIA",
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
        print("CAMPANHAS DISPONVEIS")
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
        print("A'O DO KERNEL")
        print()

        if prontas:

            campanha = prontas[0][0]

            print("Campanha priorizada:")

            print()

            print(campanha["produto"])

            print()

            print("Prximas etapas:")

            print()

            print("Gerar conteudo")

            print("" Preparar mensagens")

            print("" Enviar para aprovao")

            print("" Publicar")

            print("" Monitorar leads")

        else:

            print("Nenhuma campanha pode ser executada.")

        print()

        print("="*70)
        print("FILOSOFIA")
        print()

        print("O Kernel no publica campanhas.")

        print("Ele identifica oportunidades,")

        print("prioriza aes")

        print("e prepara a execuo.")

        print()

        print("="*70)
        print("CAMPAIGN ORCHESTRATOR ONLINE")
        print("="*70)


if __name__=="__main__":

    CampaignOrchestrator().executar()



