import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC GLOBAL STATUS ENGINE
FASE 03
ETAPA 002

VersÃƒÂ£o 4.0

======================================================================
"""

from datetime import datetime


class GlobalStatusEngine:

    VERSION = "4.0"

    def __init__(self):

        self.departamentos = {

            "Executive Orchestrator":100,

            "Commercial Center":75,

            "Marketing Center":0,

            "Financial Center":82,

            "Intelligence Center":98,

            "Kernel":100

        }

    # ------------------------------------------------------------

    def media(self):

        return round(

            sum(self.departamentos.values())

            /

            len(self.departamentos),

            2

        )

    # ------------------------------------------------------------

    def classificar(self):

        nota=self.media()

        if nota>=90:

            return "EMPRESA OPERACIONAL"

        elif nota>=75:

            return "PRONTA PARA EXPANSÃƒÆ'O"

        elif nota>=50:

            return "EM CONSOLIDAÃƒâ€¡ÃƒÆ'O"

        else:

            return "EM IMPLANTAÃƒâ€¡ÃƒÆ'O"

    # ------------------------------------------------------------

    def executar(self):

        print()

        print("="*70)

        print("IOTEC GLOBAL STATUS ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("SAÃƒÅ¡DE CORPORATIVA")

        print()

        for nome,valor in self.departamentos.items():

            print(f"{nome:30} {valor:>3}%")

        print()

        print("="*70)

        print("ÃƒÂNDICE GLOBAL")

        print()

        print(f"{self.media()} %")

        print()

        print("="*70)

        print("STATUS")

        print()

        print(self.classificar())

        print()

        print("="*70)

        print("PONTOS FORTES")

        print()

        fortes=[

            nome

            for nome,valor in self.departamentos.items()

            if valor>=90

        ]

        for item in fortes:

            print("Ã¢Å"â€œ",item)

        print()

        print("="*70)

        print("PONTOS PRIORITÃƒÂRIOS")

        print()

        fracos=sorted(

            self.departamentos.items(),

            key=lambda x:x[1]

        )

        for nome,valor in fracos:

            if valor<80:

                print(f"{nome:30} {valor}%")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Elevar continuamente")

        print("todos os departamentos")

        print("atÃƒÂ© maturidade superior")

        print("a 90%.")

        print()

        print("="*70)

        print("GLOBAL STATUS ENGINE ONLINE")

        print("="*70)


if __name__=="__main__":

    GlobalStatusEngine().executar()



