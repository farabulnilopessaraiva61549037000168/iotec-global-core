import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC MISSION CONTROL ENGINE
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Centro de MissÃƒÂµes Executivas

======================================================================
"""

from datetime import datetime


class MissionControlEngine:

    def __init__(self):

        self.meta = "FECHAR O PRIMEIRO CONTRATO"

        self.missoes = [

            ("WhatsApp Business", False, "CRÃƒÂTICA"),
            ("Landing Page", False, "CRÃƒÂTICA"),
            ("FormulÃƒÂ¡rio de Contato", False, "CRÃƒÂTICA"),
            ("Meio de Pagamento", False, "CRÃƒÂTICA"),

            ("LinkedIn Corporativo", False, "ALTA"),
            ("Portal Institucional", False, "ALTA"),
            ("CatÃƒÂ¡logo Comercial", False, "ALTA"),

            ("Google Business", False, "MÃƒâ€°DIA"),
            ("Tabela Comercial", False, "MÃƒâ€°DIA")

        ]

    # =====================================================

    def executar(self):

        print()
        print("="*70)
        print("IOTEC MISSION CONTROL ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O PRINCIPAL")
        print()
        print(self.meta)
        print()

        concluidas = 0

        print("="*70)
        print("MISSÃƒâ€¢ES")
        print()

        for numero,(nome,status,prioridade) in enumerate(self.missoes,1):

            if status:

                simbolo="Ã¢Å"â€œ"
                concluidas+=1

            else:

                simbolo=" "

            print(f"[{simbolo}] {numero:02d}. {nome}")
            print(f"     Prioridade.... {prioridade}")
            print()

        percentual=(concluidas/len(self.missoes))*100

        print("="*70)
        print("PROGRESSO")
        print()
        print(f"{percentual:.1f}%")
        print()

        print("="*70)
        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")
        print()
        print("Implantar WhatsApp Business")
        print()

        print("="*70)
        print("REGRA DO KERNEL")
        print()
        print("Nenhuma nova funcionalidade")
        print("serÃƒÂ¡ priorizada")
        print("enquanto existir")
        print("um bloqueador crÃƒÂ­tico")
        print("para geraÃƒÂ§ÃƒÂ£o de receita.")
        print()

        print("="*70)
        print("MISSION CONTROL ONLINE")
        print("="*70)


if __name__ == "__main__":

    MissionControlEngine().executar()



