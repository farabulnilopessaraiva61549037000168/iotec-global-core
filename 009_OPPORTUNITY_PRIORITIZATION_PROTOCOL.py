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

009 - OPPORTUNITY PRIORITIZATION PROTOCOL

======================================================================
"""

from datetime import datetime


class OpportunityPrioritizationProtocol:

    VERSION = "3.0"

    def executar(self):

        print()
        print("="*70)
        print("IOTEC OPPORTUNITY PRIORITIZATION PROTOCOL")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()
        print("MISSÃƒÆ'O")
        print()

        print("Priorizar continuamente")
        print("as oportunidades com maior")
        print("potencial de geraÃƒÂ§ÃƒÂ£o de valor")
        print("para clientes e para a IOTEC.")

        print()

        print("="*70)

        print("FILOSOFIA")

        filosofia=[

        "Nem toda oportunidade possui a mesma prioridade.",

        "Nem todo cliente possui o mesmo potencial.",

        "Tempo ÃƒÂ© recurso estratÃƒÂ©gico.",

        "O Kernel deverÃƒÂ¡ concentrar esforÃƒÂ§os onde existe maior retorno.",

        "Priorizar ÃƒÂ© mais importante que acumular oportunidades."

        ]

        for f in filosofia:

            print("Ã¢Å"â€œ",f)

        print()

        print("="*70)

        print("CRITÃƒâ€°RIOS DE PRIORIZAÃƒâ€¡ÃƒÆ'O")

        criterios=[

        "AderÃƒÂªncia ao portfÃƒÂ³lio",

        "Potencial financeiro",

        "UrgÃƒÂªncia",

        "Complexidade",

        "Probabilidade de fechamento",

        "Capacidade de implantaÃƒÂ§ÃƒÂ£o",

        "Relacionamento existente",

        "Potencial de recorrÃƒÂªncia",

        "Potencial de expansÃƒÂ£o",

        "Valor estratÃƒÂ©gico"

        ]

        for c in criterios:

            print("Ã¢â‚¬Â¢",c)

        print()

        print("="*70)

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        niveis=[

        "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ PRIORIDADE MÃƒÂXIMA",

        "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ ALTA",

        "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦ MÃƒâ€°DIA",

        "Ã¢Ëœâ€¦Ã¢Ëœâ€¦ BAIXA",

        "Ã¢Ëœâ€¦ MONITORAMENTO"

        ]

        for n in niveis:

            print(n)

        print()

        print("="*70)

        print("PERGUNTAS DO KERNEL")

        perguntas=[

        "Esta oportunidade gera receita?",

        "Existe necessidade comprovada?",

        "O cliente possui orÃƒÂ§amento?",

        "Existe decisor identificado?",

        "O produto estÃƒÂ¡ pronto?",

        "A campanha estÃƒÂ¡ pronta?",

        "Existe concorrÃƒÂªncia?",

        "Qual a chance de fechamento?",

        "Qual serÃƒÂ¡ o prÃƒÂ³ximo passo?",

        "Vale investir tempo agora?"

        ]

        for p in perguntas:

            print("Ã¢Å"â€œ",p)

        print()

        print("="*70)

        print("REGRAS")

        regras=[

        "Nunca abandonar uma oportunidade sem justificativa.",

        "Reavaliar prioridades continuamente.",

        "Registrar toda decisÃƒÂ£o.",

        "Aprender com contratos ganhos.",

        "Aprender com contratos perdidos.",

        "Atualizar o ranking automaticamente."

        ]

        for r in regras:

            print("Ã¢Å"â€œ",r)

        print()

        print("="*70)

        print("OBJETIVO")

        print()

        print("Concentrar energia")
        print("nas oportunidades")
        print("com maior potencial")
        print("de geraÃƒÂ§ÃƒÂ£o de receita.")

        print()

        print("="*70)
        print("OPPORTUNITY PRIORITIZATION CARREGADO")
        print("="*70)


if __name__=="__main__":

    OpportunityPrioritizationProtocol().executar()



