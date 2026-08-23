import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE KNOWLEDGE SCORE
FASE 07
ETAPA 005

VersÃƒÂ£o 8.0

Capital Intelectual Corporativo

======================================================================
"""

from datetime import datetime


class CorporateKnowledgeScore:

    VERSION = "8.0"

    def __init__(self):

        self.campos = [

            ("RazÃƒÂ£o Social",5,False),
            ("Nome Fantasia",3,False),
            ("CNPJ / Registro",5,False),
            ("Status",2,False),

            ("PaÃƒÂ­s",2,True),
            ("Estado",2,False),
            ("Cidade",2,False),

            ("Website Oficial",5,False),
            ("LinkedIn Oficial",5,False),
            ("Telefone Comercial",5,False),
            ("E-mail Comercial",5,False),

            ("Segmento",5,True),
            ("Subsegmento",3,False),

            ("Produtos",10,False),
            ("ServiÃƒÂ§os",10,False),
            ("Mercados",8,False),
            ("Tecnologias",8,False),

            ("Executivos",5,False),
            ("Parceiros",5,False),

            ("Potencial Comercial",5,False),

            ("Prioridade",3,False),

            ("Origem dos Dados",3,False),

            ("ÃƒÅ¡ltima AtualizaÃƒÂ§ÃƒÂ£o",4,False)

        ]

    # ========================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC CORPORATE KNOWLEDGE SCORE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        total=0
        obtido=0

        print()

        print("CAPITAL INTELECTUAL")

        print()

        for campo,peso,status in self.campos:

            total+=peso

            if status:

                obtido+=peso
                icone="Ã¢Å"â€œ"

            else:

                icone=" "

            print(f"[{icone}] {campo:<30} {peso:>2} pontos")

        print()

        print("="*70)

        percentual=(obtido/total)*100

        print("PONTUAÃƒâ€¡ÃƒÆ'O")

        print()

        print("Conhecimento Obtido.....",obtido)

        print("Conhecimento Total......",total)

        print(f"Capital Intelectual..... {percentual:.1f}%")

        print()

        print("="*70)

        if percentual<20:

            nivel="INICIAL"

        elif percentual<40:

            nivel="BÃƒÂSICO"

        elif percentual<60:

            nivel="INTERMEDIÃƒÂRIO"

        elif percentual<80:

            nivel="AVANÃƒâ€¡ADO"

        elif percentual<95:

            nivel="PREMIUM"

        else:

            nivel="EXCELÃƒÅ NCIA"

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        print(nivel)

        print()

        print("="*70)

        print("CAPACIDADE DO KERNEL")

        print()

        if percentual<20:

            print("Conhecimento insuficiente.")
            print("NÃƒÂ£o recomendar abordagem comercial.")

        elif percentual<40:

            print("Conhecimento limitado.")
            print("Priorizar enriquecimento dos dados.")

        elif percentual<60:

            print("Conhecimento moderado.")
            print("Permite anÃƒÂ¡lise preliminar.")

        elif percentual<80:

            print("Conhecimento elevado.")
            print("Permite estratÃƒÂ©gia personalizada.")

        else:

            print("Conhecimento profundo.")
            print("Permite proposta altamente personalizada.")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("A qualidade das decisÃƒÂµes")

        print("depende da qualidade")

        print("do conhecimento.")

        print()

        print("Quanto maior")

        print("o Capital Intelectual,")

        print("maior a capacidade")

        print("estratÃƒÂ©gica da IOTEC.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Transformar dados")

        print("em patrimÃƒÂ´nio")

        print("intelectual permanente.")

        print()

        print("="*70)

        print("CORPORATE KNOWLEDGE SCORE ONLINE")

        print("="*70)


# ============================================================

if __name__=="__main__":

    CorporateKnowledgeScore().executar()



