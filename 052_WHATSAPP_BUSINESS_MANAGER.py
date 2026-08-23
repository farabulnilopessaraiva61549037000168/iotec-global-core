import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC WHATSAPP BUSINESS MANAGER
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Gerenciador de ImplantaÃƒÂ§ÃƒÂ£o
WhatsApp Business

======================================================================
"""

from datetime import datetime


class WhatsAppBusinessManager:

    def __init__(self):

        self.numero = "+55 88 99306-4168"

        self.etapas = [

            ("Linha telefÃƒÂ´nica ativa", True),

            ("WhatsApp Business instalado", False),

            ("Conta criada", False),

            ("Nome da empresa configurado", False),

            ("Logo da empresa", False),

            ("DescriÃƒÂ§ÃƒÂ£o institucional", False),

            ("HorÃƒÂ¡rio de atendimento", False),

            ("Mensagem de boas-vindas", False),

            ("Mensagem de ausÃƒÂªncia", False),

            ("CatÃƒÂ¡logo de serviÃƒÂ§os", False),

            ("Etiquetas comerciais", False),

            ("IntegraÃƒÂ§ÃƒÂ£o com CRM", False),

            ("IntegraÃƒÂ§ÃƒÂ£o com Kernel", False)

        ]

    # =====================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC WHATSAPP BUSINESS MANAGER")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("NÃƒÅ¡MERO OFICIAL")

        print(self.numero)

        print()

        concluidas = 0

        print("="*70)
        print("CHECKLIST DE IMPLANTAÃƒâ€¡ÃƒÆ'O")
        print()

        for etapa, status in self.etapas:

            if status:

                print("[Ã¢Å"â€œ]", etapa)
                concluidas += 1

            else:

                print("[ ]", etapa)

        percentual = (concluidas / len(self.etapas)) * 100

        print()

        print("="*70)

        print("MATURIDADE")

        print()

        print(f"{percentual:.1f}%")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA AÃƒâ€¡ÃƒÆ'O")

        print()

        if percentual < 100:

            print("Concluir configuraÃƒÂ§ÃƒÂ£o do WhatsApp Business.")

        else:

            print("WhatsApp pronto para integraÃƒÂ§ÃƒÂ£o com o Kernel.")

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Transformar o WhatsApp")
        print("no principal canal")
        print("de comunicaÃƒÂ§ÃƒÂ£o")
        print("entre a IOTEC")
        print("e seus clientes.")

        print()

        print("="*70)

        print("WHATSAPP BUSINESS MANAGER ONLINE")

        print("="*70)


if __name__ == "__main__":

    WhatsAppBusinessManager().executar()



