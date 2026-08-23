import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC OPERATION CENTER

016 - COMMERCIAL SCORE ENGINE

VersÃƒÂ£o 3.0

======================================================================
"""

from datetime import datetime


class CommercialScoreEngine:

    def __init__(self):

        self.metricas = {

            "Portal":80,
            "CRM":95,
            "Kernel":100,
            "Revenue":100,
            "Opportunity":95,

            "LinkedIn":20,
            "Instagram":0,
            "YouTube":0,
            "WhatsApp Business":10,

            "Landing Pages":30,
            "Produtos":60,
            "Tabela Comercial":20,

            "Campanhas":0,
            "Leads":5,
            "Propostas":0,
            "Contratos":0,

            "Pagamentos":5,
            "Receita":0,

            "Marketing":15,

            "Marca":40

        }

    # --------------------------------------------------------

    def media(self):

        return round(

            sum(self.metricas.values())

            /

            len(self.metricas),

            2

        )

    # --------------------------------------------------------

    def classificar(self,nota):

        if nota>=90:

            return "EXCELENTE"

        elif nota>=75:

            return "MUITO BOA"

        elif nota>=60:

            return "BOA"

        elif nota>=40:

            return "EM EVOLUÃƒâ€¡ÃƒÆ'O"

        elif nota>=20:

            return "ESTRUTURA INICIAL"

        else:

            return "CRÃƒÂTICA"

    # --------------------------------------------------------

    def prioridades(self):

        lista=[]

        for nome,valor in self.metricas.items():

            if valor<50:

                lista.append((nome,valor))

        lista.sort(key=lambda x:x[1])

        return lista

    # --------------------------------------------------------

    def executar(self):

        print()

        print("="*70)

        print("IOTEC COMMERCIAL SCORE ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        print("INDICADORES")

        print()

        for nome,valor in self.metricas.items():

            print(f"{nome:30} {valor:>3}%")

        print()

        print("="*70)

        nota=self.media()

        print("MATURIDADE COMERCIAL")

        print()

        print(f"{nota}%")

        print()

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        print(self.classificar(nota))

        print()

        print("="*70)

        print("PRIORIDADES")

        print()

        for nome,valor in self.prioridades():

            print(f"{nome:30} {valor}%")

        print()

        print("="*70)

        print("MISSÃƒÆ'O DO DIA")

        print()

        print("Elevar os indicadores")

        print("com menor maturidade.")

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Atingir maturidade")

        print("comercial superior")

        print("a 90%.")

        print()

        print("="*70)

        print("ENGINE FINALIZADA")

        print("="*70)


if __name__=="__main__":

    CommercialScoreEngine().executar()



