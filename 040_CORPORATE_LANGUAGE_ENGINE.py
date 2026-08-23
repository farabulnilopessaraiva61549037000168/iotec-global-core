import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE LANGUAGE ENGINE
FASE 06
ETAPA 006

VersÃƒÂ£o 7.0

Biblioteca Oficial da Linguagem Corporativa

======================================================================
"""

from datetime import datetime


class CorporateLanguageEngine:

    VERSION = "7.0"

    def __init__(self):

        self.capitulos = {

            "apresentacao":{

                "titulo":"Como apresentar a IOTEC",

                "texto":"""

A IOTEC ÃƒÂ© uma empresa especializada em
inteligÃƒÂªncia de dados, automaÃƒÂ§ÃƒÂ£o,
Business Intelligence e consultoria.

Nosso trabalho consiste em compreender
organizaÃƒÂ§ÃƒÂµes, transformar informaÃƒÂ§ÃƒÂµes
em conhecimento ÃƒÂºtil
e apoiar decisÃƒÂµes estratÃƒÂ©gicas.

NÃƒÂ£o comeÃƒÂ§amos oferecendo produtos.

ComeÃƒÂ§amos compreendendo a realidade
de cada organizaÃƒÂ§ÃƒÂ£o.

"""

            },

            "valor":{

                "titulo":"Como explicar o valor",

                "texto":"""

A tecnologia por si sÃƒÂ³ nÃƒÂ£o gera valor.

O valor surge quando informaÃƒÂ§ÃƒÂµes
sÃƒÂ£o organizadas,
transformadas em inteligÃƒÂªncia
e utilizadas para apoiar decisÃƒÂµes.

Ãƒâ€° exatamente nesse ponto
que a IOTEC atua.

"""

            },

            "dados":{

                "titulo":"Como falar sobre dados",

                "texto":"""

Toda empresa produz informaÃƒÂ§ÃƒÂµes.

Essas informaÃƒÂ§ÃƒÂµes representam
um patrimÃƒÂ´nio estratÃƒÂ©gico.

Quando organizadas,
elas permitem identificar tendÃƒÂªncias,
acompanhar indicadores,
reduzir desperdÃƒÂ­cios
e melhorar decisÃƒÂµes.

"""

            },

            "ia":{

                "titulo":"Como explicar InteligÃƒÂªncia Artificial",

                "texto":"""

A InteligÃƒÂªncia Artificial
nÃƒÂ£o substitui pessoas.

Ela amplia a capacidade
de compreender informaÃƒÂ§ÃƒÂµes,
automatizar tarefas
e apoiar decisÃƒÂµes.

A decisÃƒÂ£o continua sendo humana.

"""

            },

            "consultoria":{

                "titulo":"Como explicar consultoria",

                "texto":"""

Consultoria significa compreender
uma organizaÃƒÂ§ÃƒÂ£o antes
de recomendar mudanÃƒÂ§as.

Cada empresa possui
uma realidade diferente.

Por isso,
as recomendaÃƒÂ§ÃƒÂµes
devem ser personalizadas.

"""

            },

            "fechamento":{

                "titulo":"Como encerrar uma reuniÃƒÂ£o",

                "texto":"""

Agradecemos pela oportunidade
de compreender sua organizaÃƒÂ§ÃƒÂ£o.

O prÃƒÂ³ximo passo
ÃƒÂ© transformar o que aprendemos
em uma proposta objetiva,
alinhada ÃƒÂ s necessidades
identificadas durante a conversa.

"""

            }

        }

    # =====================================================

    def mostrar(self,chave):

        print()

        print("="*70)

        print("IOTEC CORPORATE LANGUAGE ENGINE")

        print("="*70)

        print(datetime.now())

        print("="*70)

        print()

        if chave not in self.capitulos:

            print("CapÃƒÂ­tulo nÃƒÂ£o encontrado.")

            return

        cap=self.capitulos[chave]

        print(cap["titulo"])

        print()

        print(cap["texto"])

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Toda comunicaÃƒÂ§ÃƒÂ£o")

        print("deve gerar")

        print("clareza,")

        print("confianÃƒÂ§a")

        print("e compreensÃƒÂ£o.")

        print()

        print("="*70)

        print("CORPORATE LANGUAGE ONLINE")

        print("="*70)


# =======================================================

if __name__=="__main__":

    engine=CorporateLanguageEngine()

    print()

    print("CAPÃƒÂTULOS")

    print()

    for chave in engine.capitulos:

        print("-",chave)

    print()

    escolha=input("CapÃƒÂ­tulo: ").strip()

    engine.mostrar(escolha)



