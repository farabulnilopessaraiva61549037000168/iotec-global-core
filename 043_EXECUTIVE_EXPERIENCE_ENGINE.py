import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EXECUTIVE EXPERIENCE ENGINE
FASE 06
ETAPA 009

VersÃƒÂ£o 7.0

A experiÃƒÂªncia passa a ser patrimÃƒÂ´nio
permanente da IOTEC.

======================================================================
"""

from datetime import datetime


class ExecutiveExperienceEngine:

    def __init__(self):

        self.experiencias = [

            {

                "empresa":"Microsoft",

                "segmento":"Tecnologia",

                "estrategia":"Abordagem consultiva.",

                "resultado":"Aguardando contato.",

                "licao":"Empresas maduras exigem preparaÃƒÂ§ÃƒÂ£o profunda."

            },

            {

                "empresa":"Midea",

                "segmento":"EletrodomÃƒÂ©sticos",

                "estrategia":"Demonstrar conhecimento industrial.",

                "resultado":"Em estudo.",

                "licao":"Conhecer a operaÃƒÂ§ÃƒÂ£o aumenta a credibilidade."

            }

        ]

    # =======================================================

    def executar(self):

        print()

        print("="*70)

        print("IOTEC EXECUTIVE EXPERIENCE ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        for numero,item in enumerate(self.experiencias,1):

            print(f"CASO {numero}")

            print()

            print("Empresa..........",item["empresa"])

            print("Segmento.........",item["segmento"])

            print("EstratÃƒÂ©gia.......",item["estrategia"])

            print("Resultado........",item["resultado"])

            print("LiÃƒÂ§ÃƒÂ£o Aprendida..",item["licao"])

            print()

            print("-"*70)

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Toda interaÃƒÂ§ÃƒÂ£o")

        print("deve produzir")

        print("conhecimento.")

        print()

        print("Toda reuniÃƒÂ£o")

        print("deve enriquecer")

        print("o patrimÃƒÂ´nio")

        print("intelectual")

        print("da IOTEC.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Aprender continuamente.")

        print("Evoluir continuamente.")

        print("Nunca repetir")

        print("o mesmo erro.")

        print()

        print("="*70)

        print("EXECUTIVE EXPERIENCE ONLINE")

        print("="*70)


# ============================================================

if __name__=="__main__":

    ExecutiveExperienceEngine().executar()



