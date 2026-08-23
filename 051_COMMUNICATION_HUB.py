import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC COMMUNICATION HUB
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Centro Oficial de ComunicaÃƒÂ§ÃƒÂ£o

======================================================================
"""

from datetime import datetime


class CommunicationHub:

    def __init__(self):

        self.canais = [

            {
                "nome":"Telefone Comercial",
                "status":"ONLINE",
                "valor":"+55 88 99306-4168",
                "prioridade":"CRÃƒÂTICA"
            },

            {
                "nome":"WhatsApp Business",
                "status":"EM ATIVAÃƒâ€¡ÃƒÆ'O",
                "valor":"+55 88 99306-4168",
                "prioridade":"CRÃƒÂTICA"
            },

            {
                "nome":"E-mail Corporativo",
                "status":"ONLINE",
                "valor":"iotec.bl@proton.me",
                "prioridade":"CRÃƒÂTICA"
            },

            {
                "nome":"Portal Institucional",
                "status":"OFFLINE",
                "valor":"NÃƒÂ£o publicado",
                "prioridade":"ALTA"
            },

            {
                "nome":"LinkedIn",
                "status":"OFFLINE",
                "valor":"PÃƒÂ¡gina nÃƒÂ£o criada",
                "prioridade":"ALTA"
            },

            {
                "nome":"Google Business",
                "status":"OFFLINE",
                "valor":"NÃƒÂ£o cadastrado",
                "prioridade":"ALTA"
            },

            {
                "nome":"Landing Pages",
                "status":"OFFLINE",
                "valor":"NÃƒÂ£o publicadas",
                "prioridade":"MÃƒâ€°DIA"
            },

            {
                "nome":"CatÃƒÂ¡logo Comercial",
                "status":"OFFLINE",
                "valor":"NÃƒÂ£o publicado",
                "prioridade":"MÃƒâ€°DIA"
            }

        ]

    # ==========================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC COMMUNICATION HUB")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        online = 0

        for canal in self.canais:

            print(canal["nome"])

            print("Status.......",canal["status"])
            print("InformaÃƒÂ§ÃƒÂ£o...",canal["valor"])
            print("Prioridade...",canal["prioridade"])

            print()

            if canal["status"] == "ONLINE":

                online += 1

        maturidade = (online/len(self.canais))*100

        print("="*70)

        print("RESUMO")

        print()

        print("Canais..............",len(self.canais))
        print("Online..............",online)
        print("Maturidade.......... {:.1f}%".format(maturidade))

        print()

        print("="*70)

        print("MISSÃƒÆ'O DO KERNEL")

        print()

        print("Nenhuma campanha")
        print("deverÃƒÂ¡ ser iniciada")
        print("sem canais mÃƒÂ­nimos")
        print("de comunicaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("CHECKLIST")

        print()

        obrigatorios = [

            "Telefone Comercial",

            "WhatsApp Business",

            "E-mail Corporativo",

            "Portal Institucional",

            "LinkedIn"

        ]

        for item in obrigatorios:

            print("[ ]",item)

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA ETAPA")

        print()

        print("WHATSAPP BUSINESS MANAGER")

        print()

        print("="*70)

        print("COMMUNICATION HUB ONLINE")

        print("="*70)


if __name__ == "__main__":

    hub = CommunicationHub()

    hub.executar()



