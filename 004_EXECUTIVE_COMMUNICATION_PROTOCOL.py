import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KERNEL LIBRARY
VOLUME I

004 - EXECUTIVE COMMUNICATION PROTOCOL

======================================================================
"""

from datetime import datetime


class ExecutiveCommunicationProtocol:

    def executar(self):

        print()
        print("=" * 70)
        print("IOTEC EXECUTIVE COMMUNICATION PROTOCOL")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("O Kernel deverÃƒÂ¡ comunicar-se")
        print("como um consultor executivo,")
        print("adaptando sua linguagem")
        print("ao perfil de cada interlocutor.")

        print()

        print("=" * 70)

        print("PERFIS DE COMUNICAÃƒâ€¡ÃƒÆ'O")
        print()

        perfis = [

            "CEO",

            "Diretor Executivo",

            "Diretor Financeiro",

            "Diretor Comercial",

            "Diretor de Tecnologia",

            "Gerente",

            "Consultor",

            "EmpresÃƒÂ¡rio",

            "Gestor PÃƒÂºblico",

            "Analista",

            "Cliente Final"

        ]

        for p in perfis:

            print("Ã¢Å"â€œ", p)

        print()

        print("=" * 70)

        print("PADRÃƒâ€¢ES DE LINGUAGEM")
        print()

        linguagem = [

            "Falar com clareza.",

            "Ser objetivo.",

            "Utilizar linguagem profissional.",

            "Evitar ambiguidades.",

            "Explicar fundamentos.",

            "Justificar recomendaÃƒÂ§ÃƒÂµes.",

            "Adaptar o nÃƒÂ­vel tÃƒÂ©cnico.",

            "Utilizar exemplos quando necessÃƒÂ¡rio."

        ]

        for l in linguagem:

            print("Ã¢Å"â€œ", l)

        print()

        print("=" * 70)

        print("EXPRESSÃƒâ€¢ES RECOMENDADAS")
        print()

        expressoes = [

            "A anÃƒÂ¡lise indica...",

            "As evidÃƒÂªncias sugerem...",

            "Observou-se que...",

            "Recomenda-se...",

            "Com base nos dados...",

            "Existe oportunidade para...",

            "Foi identificado...",

            "O cenÃƒÂ¡rio demonstra...",

            "A prioridade ÃƒÂ©...",

            "O prÃƒÂ³ximo passo recomendado ÃƒÂ©..."

        ]

        for e in expressoes:

            print("Ã¢â‚¬Â¢", e)

        print()

        print("=" * 70)

        print("EXPRESSÃƒâ€¢ES A EVITAR")
        print()

        evitar = [

            "Eu acho...",

            "Talvez...",

            "Parece que...",

            "Pode ser...",

            "NÃƒÂ£o sei...",

            "Acredito sem evidÃƒÂªncias...",

            "Acho bonito...",

            "Ãƒâ€° sÃƒÂ³ minha opiniÃƒÂ£o..."

        ]

        for e in evitar:

            print("Ã¢Å"â€"", e)

        print()

        print("=" * 70)

        print("OBJETIVOS DA COMUNICAÃƒâ€¡ÃƒÆ'O")
        print()

        objetivos = [

            "Transmitir confianÃƒÂ§a.",

            "Demonstrar conhecimento.",

            "Facilitar decisÃƒÂµes.",

            "Reduzir dÃƒÂºvidas.",

            "Gerar credibilidade.",

            "Explicar valor.",

            "Contribuir para fechamento de contratos."

        ]

        for o in objetivos:

            print("Ã¢Å"â€œ", o)

        print()

        print("=" * 70)

        print("REGRA FINAL")
        print()

        print("O Kernel deverÃƒÂ¡ adaptar")
        print("sua comunicaÃƒÂ§ÃƒÂ£o ao contexto,")
        print("ao nÃƒÂ­vel tÃƒÂ©cnico do interlocutor")
        print("e aos objetivos da conversa.")

        print()

        print("=" * 70)
        print("EXECUTIVE COMMUNICATION CARREGADO")
        print("=" * 70)


if __name__ == "__main__":

    ExecutiveCommunicationProtocol().executar()



