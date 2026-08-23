import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EVENT ORCHESTRATOR ENGINE
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Orquestrador Central de Eventos

======================================================================
"""

from datetime import datetime


class EventOrchestrator:

    def __init__(self):

        self.eventos = [

            {
                "evento":"WhatsApp Business ONLINE",
                "prioridade":"CRÃƒÂTICA",
                "departamento":"Campaign Manager",
                "acao":"Preparar campanha institucional",
                "status":"PRONTO"
            },

            {
                "evento":"Email Corporativo ONLINE",
                "prioridade":"ALTA",
                "departamento":"Email Campaign",
                "acao":"Preparar campanha por email",
                "status":"PRONTO"
            },

            {
                "evento":"LinkedIn ONLINE",
                "prioridade":"ALTA",
                "departamento":"LinkedIn Campaign",
                "acao":"Publicar conteÃƒÂºdo institucional",
                "status":"AGUARDANDO"
            },

            {
                "evento":"Portal ONLINE",
                "prioridade":"ALTA",
                "departamento":"Website",
                "acao":"Liberar Landing Pages",
                "status":"AGUARDANDO"
            },

            {
                "evento":"Google Business ONLINE",
                "prioridade":"MÃƒâ€°DIA",
                "departamento":"Google Business",
                "acao":"Publicar perfil corporativo",
                "status":"AGUARDANDO"
            }

        ]

    # =========================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC EVENT ORCHESTRATOR ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("FILA DE EVENTOS")

        print()

        prontos = 0

        for numero, evento in enumerate(self.eventos,1):

            print(f"[{numero:02d}] {evento['evento']}")

            print("Prioridade....",evento["prioridade"])
            print("Destino.......",evento["departamento"])
            print("AÃƒÂ§ÃƒÂ£o..........",evento["acao"])
            print("Status........",evento["status"])

            print()

            if evento["status"] == "PRONTO":
                prontos += 1

        print("="*70)

        print("RESUMO")

        print()

        print("Eventos.............",len(self.eventos))
        print("Prontos............",prontos)
        print("Aguardando.........",len(self.eventos)-prontos)

        print()

        print("="*70)

        print("EVENTOS LIBERADOS")

        print()

        for evento in self.eventos:

            if evento["status"] == "PRONTO":

                print("Ã¢Å"â€œ",evento["evento"])

                print("  Kernel prepararÃƒÂ¡:")

                print(" ",evento["acao"])

                print()

        print("="*70)

        print("FLUXO OPERACIONAL")

        print()

        print("Evento")

        print("Ã¢â€ â€œ")

        print("Kernel")

        print("Ã¢â€ â€œ")

        print("Campaign Manager")

        print("Ã¢â€ â€œ")

        print("ConteÃƒÂºdo")

        print("Ã¢â€ â€œ")

        print("Fila de AprovaÃƒÂ§ÃƒÂ£o")

        print("Ã¢â€ â€œ")

        print("PublicaÃƒÂ§ÃƒÂ£o")

        print("Ã¢â€ â€œ")

        print("Leads")

        print("Ã¢â€ â€œ")

        print("CRM")

        print("Ã¢â€ â€œ")

        print("Receita")

        print()

        print("="*70)

        print("REGRA DO KERNEL")

        print()

        print("Nenhuma campanha serÃƒÂ¡ publicada")

        print("automaticamente.")

        print()

        print("O Kernel prepara,")

        print("organiza e envia")

        print("para aprovaÃƒÂ§ÃƒÂ£o humana.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA EVOLUÃƒâ€¡ÃƒÆ'O")

        print()

        print("Campaign Orchestrator")

        print("Content Generator")

        print("Lead Capture")

        print("CRM Automation")

        print()

        print("="*70)

        print("EVENT ORCHESTRATOR ONLINE")

        print("="*70)


if __name__=="__main__":

    EventOrchestrator().executar()



