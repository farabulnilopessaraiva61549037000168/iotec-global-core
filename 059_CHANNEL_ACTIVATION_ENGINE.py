import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CHANNEL ACTIVATION ENGINE
FASE 08

VersÃƒÂ£o 9.0

Monitor de AtivaÃƒÂ§ÃƒÂ£o Comercial

======================================================================
"""

from datetime import datetime


class ChannelActivationEngine:

    def __init__(self):

        self.canais=[

            {

                "nome":"WhatsApp Business",

                "status":"ONLINE",

                "acao":"Iniciar Campanha Comercial"

            },

            {

                "nome":"LinkedIn",

                "status":"OFFLINE",

                "acao":"Publicar ConteÃƒÂºdo"

            },

            {

                "nome":"Portal",

                "status":"OFFLINE",

                "acao":"Publicar Landing Page"

            },

            {

                "nome":"Google Business",

                "status":"OFFLINE",

                "acao":"Ativar Perfil"

            },

            {

                "nome":"Email",

                "status":"ONLINE",

                "acao":"Enviar Campanha"

            }

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)

        print("IOTEC CHANNEL ACTIVATION ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("MONITORAMENTO")

        print()

        for canal in self.canais:

            print(canal["nome"])

            print("Status.......",canal["status"])

            if canal["status"]=="ONLINE":

                print("AÃƒâ€¡ÃƒÆ'O......... LIBERADA")

                print("Kernel....... ACIONANDO CAMPANHA")

                print("MissÃƒÂ£o.......",canal["acao"])

            else:

                print("AÃƒâ€¡ÃƒÆ'O......... BLOQUEADA")

                print("Kernel....... AGUARDANDO")

            print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Toda restriÃƒÂ§ÃƒÂ£o")

        print("eliminada")

        print("gera imediatamente")

        print("uma oportunidade")

        print("de receita.")

        print()

        print("="*70)

        print("REAÃƒâ€¡ÃƒÆ'O DO KERNEL")

        print()

        print("Canal Online")

        print("Ã¢â€ â€œ")

        print("Campanha")

        print("Ã¢â€ â€œ")

        print("Lead")

        print("Ã¢â€ â€œ")

        print("CRM")

        print("Ã¢â€ â€œ")

        print("Contrato")

        print("Ã¢â€ â€œ")

        print("Receita")

        print()

        print("="*70)

        print("CHANNEL ACTIVATION ONLINE")

        print("="*70)


if __name__=="__main__":

    ChannelActivationEngine().executar()



