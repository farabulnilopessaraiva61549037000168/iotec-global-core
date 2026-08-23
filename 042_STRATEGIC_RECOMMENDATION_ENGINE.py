import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC STRATEGIC RECOMMENDATION ENGINE
FASE 06
ETAPA 008

VersÃƒÂ£o 7.0

O Kernel aprende a construir
estratÃƒÂ©gias comerciais.

======================================================================
"""

from datetime import datetime


class StrategicRecommendationEngine:

    VERSION = "7.0"

    def __init__(self):

        self.segmentos = {

            "Tecnologia":{

                "maturidade":"ALTA",

                "competicao":"ALTA",

                "potencial":"MUITO ALTO",

                "estrategia":[

                    "Demonstrar profundo conhecimento do setor.",

                    "Evitar abordagem comercial direta.",

                    "Focar em necessidades especÃƒÂ­ficas.",

                    "Apresentar inteligÃƒÂªncia como diferencial.",

                    "Construir relacionamento antes da proposta."

                ],

                "riscos":[

                    "Alta concorrÃƒÂªncia.",

                    "Cliente jÃƒÂ¡ possui fornecedores.",

                    "Processo decisÃƒÂ³rio complexo."

                ],

                "primeiro_passo":"Agendar uma conversa exploratÃƒÂ³ria para compreender o contexto da organizaÃƒÂ§ÃƒÂ£o."

            },

            "Energia":{

                "maturidade":"ALTA",

                "competicao":"MÃƒâ€°DIA",

                "potencial":"ALTO",

                "estrategia":[

                    "Priorizar indicadores operacionais.",

                    "Mostrar ganhos de integraÃƒÂ§ÃƒÂ£o.",

                    "Apresentar dashboards executivos.",

                    "Destacar apoio ÃƒÂ  decisÃƒÂ£o."

                ],

                "riscos":[

                    "Projetos de longa duraÃƒÂ§ÃƒÂ£o.",

                    "Ambiente regulatÃƒÂ³rio complexo."

                ],

                "primeiro_passo":"Compreender processos crÃƒÂ­ticos e fluxos de informaÃƒÂ§ÃƒÂ£o."

            },

            "Financeiro":{

                "maturidade":"ALTA",

                "competicao":"ALTA",

                "potencial":"ALTO",

                "estrategia":[

                    "Focar em indicadores.",

                    "Apresentar Business Intelligence.",

                    "Demonstrar organizaÃƒÂ§ÃƒÂ£o da informaÃƒÂ§ÃƒÂ£o.",

                    "Valorizar seguranÃƒÂ§a e governanÃƒÂ§a."

                ],

                "riscos":[

                    "Alto rigor regulatÃƒÂ³rio.",

                    "Grande exigÃƒÂªncia por confiabilidade."

                ],

                "primeiro_passo":"Mapear necessidades de gestÃƒÂ£o e anÃƒÂ¡lise."

            }

        }

    # ==========================================================

    def recomendar(self, empresa, segmento):

        print()

        print("="*70)
        print("IOTEC STRATEGIC RECOMMENDATION ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("EMPRESA")

        print(empresa)

        print()

        print("SEGMENTO")

        print(segmento)

        print()

        if segmento not in self.segmentos:

            print("Segmento ainda nÃƒÂ£o modelado.")

            return

        dados = self.segmentos[segmento]

        print("="*70)

        print("DIAGNÃƒâ€œSTICO")

        print()

        print("Maturidade........", dados["maturidade"])

        print("CompetiÃƒÂ§ÃƒÂ£o........", dados["competicao"])

        print("Potencial.........", dados["potencial"])

        print()

        print("="*70)

        print("ESTRATÃƒâ€°GIA RECOMENDADA")

        print()

        for item in dados["estrategia"]:

            print("Ã¢Å"â€œ", item)

        print()

        print("="*70)

        print("RISCOS")

        print()

        for risco in dados["riscos"]:

            print("Ã¢â‚¬Â¢", risco)

        print()

        print("="*70)

        print("PRÃƒâ€œXIMO PASSO")

        print()

        print(dados["primeiro_passo"])

        print()

        print("="*70)

        print("PLANO EXECUTIVO")

        print()

        print("1. Compreender profundamente a organizaÃƒÂ§ÃƒÂ£o.")

        print("2. Identificar necessidades reais.")

        print("3. Relacionar capacidades da IOTEC.")

        print("4. Construir uma proposta personalizada.")

        print("5. Demonstrar o valor esperado.")

        print("6. Agendar a prÃƒÂ³xima interaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Toda recomendaÃƒÂ§ÃƒÂ£o")

        print("deve nascer")

        print("da compreensÃƒÂ£o")

        print("da organizaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("STRATEGIC RECOMMENDATION ONLINE")

        print("="*70)


# ===============================================================

if __name__ == "__main__":

    engine = StrategicRecommendationEngine()

    engine.recomendar(

        empresa="Microsoft",

        segmento="Tecnologia"

    )



