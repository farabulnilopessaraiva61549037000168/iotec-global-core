import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC DISCOVERY CONVERSATION ENGINE
FASE 06
ETAPA 007

VersÃƒÂ£o 7.0

A IOTEC aprende a descobrir
antes de recomendar.

======================================================================
"""

from datetime import datetime


class DiscoveryConversationEngine:

    def __init__(self):

        self.etapas = [

            {
                "titulo":"1. COMPREENDER A EMPRESA",
                "perguntas":[
                    "O que a empresa faz?",
                    "Quais sÃƒÂ£o seus principais produtos ou serviÃƒÂ§os?",
                    "Quais mercados atende?",
                    "Quais sÃƒÂ£o seus principais objetivos atualmente?"
                ]
            },

            {
                "titulo":"2. COMPREENDER O CENÃƒÂRIO",
                "perguntas":[
                    "Quais sÃƒÂ£o os maiores desafios hoje?",
                    "Existe algum processo que consome muito tempo?",
                    "Quais informaÃƒÂ§ÃƒÂµes sÃƒÂ£o mais importantes para a gestÃƒÂ£o?",
                    "Como as decisÃƒÂµes sÃƒÂ£o tomadas atualmente?"
                ]
            },

            {
                "titulo":"3. COMPREENDER OS DADOS",
                "perguntas":[
                    "Onde estÃƒÂ£o armazenadas as informaÃƒÂ§ÃƒÂµes da empresa?",
                    "Existem planilhas, sistemas ou bancos de dados?",
                    "HÃƒÂ¡ indicadores acompanhados regularmente?",
                    "Os dados sÃƒÂ£o confiÃƒÂ¡veis e organizados?"
                ]
            },

            {
                "titulo":"4. IDENTIFICAR OPORTUNIDADES",
                "perguntas":[
                    "O que poderia ser automatizado?",
                    "Quais informaÃƒÂ§ÃƒÂµes seriam ÃƒÂºteis em um painel executivo?",
                    "Existe interesse em anÃƒÂ¡lises mais avanÃƒÂ§adas?",
                    "HÃƒÂ¡ necessidade de integrar diferentes sistemas?"
                ]
            },

            {
                "titulo":"5. DEFINIR O PRÃƒâ€œXIMO PASSO",
                "perguntas":[
                    "Qual seria a prioridade nÃƒÂºmero um?",
                    "Quais resultados seriam considerados um sucesso?",
                    "Existe um prazo desejado para implantaÃƒÂ§ÃƒÂ£o?",
                    "Quem participarÃƒÂ¡ das prÃƒÂ³ximas reuniÃƒÂµes?"
                ]
            }

        ]

    def executar(self):

        print()
        print("="*70)
        print("IOTEC DISCOVERY CONVERSATION ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        for etapa in self.etapas:

            print()
            print(etapa["titulo"])
            print()

            for pergunta in etapa["perguntas"]:

                print("Ã¢â‚¬Â¢", pergunta)

        print()
        print("="*70)
        print("FILOSOFIA")
        print()

        print("Primeiro compreender.")
        print("Depois analisar.")
        print("Depois recomendar.")
        print("Somente entÃƒÂ£o apresentar uma proposta.")

        print()
        print("="*70)
        print("DISCOVERY CONVERSATION ONLINE")
        print("="*70)


if __name__ == "__main__":

    DiscoveryConversationEngine().executar()



