import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC EXECUTIVE DIALOG ENGINE
FASE 06
ETAPA 005

VersÃƒÂ£o 7.0

O Kernel aprende a conversar
como um consultor executivo.

======================================================================
"""

from datetime import datetime


class ExecutiveDialogEngine:

    VERSION = "7.0"

    def __init__(self):

        self.respostas = {

            "por_que":"""

A IOTEC nÃƒÂ£o oferece apenas tecnologia.

Ela ajuda organizaÃƒÂ§ÃƒÂµes a organizar informaÃƒÂ§ÃƒÂµes,
transformar dados em inteligÃƒÂªncia
e apoiar decisÃƒÂµes estratÃƒÂ©gicas.

Nosso objetivo ÃƒÂ© compreender
a realidade da empresa
antes de recomendar qualquer soluÃƒÂ§ÃƒÂ£o.

""",

            "valor":"""

O valor entregue pela IOTEC estÃƒÂ¡ em:

Ã¢â‚¬Â¢ OrganizaÃƒÂ§ÃƒÂ£o da informaÃƒÂ§ÃƒÂ£o

Ã¢â‚¬Â¢ Business Intelligence

Ã¢â‚¬Â¢ Dashboards Executivos

Ã¢â‚¬Â¢ AutomaÃƒÂ§ÃƒÂ£o

Ã¢â‚¬Â¢ Apoio ÃƒÂ  decisÃƒÂ£o

Ã¢â‚¬Â¢ InteligÃƒÂªncia de Mercado

Ã¢â‚¬Â¢ Consultoria baseada em dados

""",

            "abordagem":"""

A abordagem recomendada ÃƒÂ©:

1. Demonstrar conhecimento do segmento.

2. Compreender os desafios da organizaÃƒÂ§ÃƒÂ£o.

3. Identificar oportunidades.

4. Relacionar capacidades da IOTEC.

5. Propor uma soluÃƒÂ§ÃƒÂ£o personalizada.

Nunca iniciar oferecendo produtos.

Primeiro compreender.

""",

            "objecoes":"""

Caso existam objeÃƒÂ§ÃƒÂµes:

Ã¢â‚¬Â¢ Escutar.

Ã¢â‚¬Â¢ Compreender.

Ã¢â‚¬Â¢ Esclarecer.

Ã¢â‚¬Â¢ Demonstrar valor.

Ã¢â‚¬Â¢ Nunca discutir.

Ã¢â‚¬Â¢ Sempre buscar entendimento.

""",

            "contrato":"""

Um contrato deve representar
uma soluÃƒÂ§ÃƒÂ£o para um problema real.

A negociaÃƒÂ§ÃƒÂ£o deve demonstrar:

Ã¢â‚¬Â¢ Valor entregue

Ã¢â‚¬Â¢ Clareza

Ã¢â‚¬Â¢ ConfianÃƒÂ§a

Ã¢â‚¬Â¢ BenefÃƒÂ­cios

Ã¢â‚¬Â¢ Resultado esperado

""",

            "missao":"""

A missÃƒÂ£o comercial da IOTEC ÃƒÂ©:

Compreender.

Organizar.

Analisar.

Recomendar.

Resolver.

Gerar valor.

Construir relacionamentos duradouros.

"""

        }

    # ===========================================================

    def responder(self,chave):

        print()

        print("="*70)

        print("IOTEC EXECUTIVE DIALOG ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        if chave not in self.respostas:

            print("Pergunta ainda nÃƒÂ£o cadastrada.")

            return

        print(self.respostas[chave])

        print()

        print("="*70)

        print("EXECUTIVE DIALOG ONLINE")

        print("="*70)


# ===============================================================

if __name__=="__main__":

    engine=ExecutiveDialogEngine()

    print()

    print("PERGUNTAS DISPONÃƒÂVEIS")

    print()

    print("por_que")

    print("valor")

    print("abordagem")

    print("objecoes")

    print("contrato")

    print("missao")

    print()

    pergunta=input("Pergunta: ").strip()

    engine.responder(pergunta)



