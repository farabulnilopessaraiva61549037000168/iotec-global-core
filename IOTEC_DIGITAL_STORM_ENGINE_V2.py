import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM ENGINE V2.0
# NÃƒÂºcleo Inteligente de AdaptaÃƒÂ§ÃƒÂ£o EcossistÃƒÂªmica
#
# FunÃƒÂ§ÃƒÂ£o:
# Monitorar variÃƒÂ¡veis do ambiente digital,
# calcular pressÃƒÂ£o de mudanÃƒÂ§a,
# identificar oportunidades e riscos,
# executar respostas estratÃƒÂ©gicas.
#
# Arquitetura IoTec
# ============================================================


import datetime
import random


class IOTEC_DigitalStorm:


    def __init__(self):

        self.nome = "IOTEC DIGITAL STORM ENGINE V2.0"

        self.sensores = {}

        self.analise = {}

        self.previsao = {}

        self.acoes = []



    # ========================================================
    # CAMADA SENSOR
    # Coleta sinais do ecossistema
    # ========================================================

    def coletar_sinais(self):

        self.sensores = {

            "mercado": random.randint(0,100),

            "demanda_cliente": random.randint(0,100),

            "risco_cibernetico": random.randint(0,100),

            "tendencia_tecnologica": random.randint(0,100),

            "capacidade_computacional": random.randint(0,100),

            "recursos_financeiros": random.randint(0,100),

            "clima_operacional": random.randint(0,100)

        }


        return self.sensores




    # ========================================================
    # CAMADA PRESSÃƒÆ'O DIGITAL
    # Mede intensidade das mudanÃƒÂ§as
    # ========================================================

    def calcular_pressao(self):


        s = self.sensores


        pressao = (

            s["mercado"] +

            s["demanda_cliente"] +

            s["tendencia_tecnologica"]

        ) / 3



        self.analise["pressao_ecossistema"] = round(
            pressao,2
        )


        if pressao >= 75:

            self.analise["estado"] = "TEMPESTADE DE OPORTUNIDADE"


        elif pressao >= 45:

            self.analise["estado"] = "MUDANÃƒâ€¡A MODERADA"


        else:

            self.analise["estado"] = "AMBIENTE ESTÃƒÂVEL"



        return self.analise




    # ========================================================
    # CAMADA INTELIGÃƒÅ NCIA
    # InterpretaÃƒÂ§ÃƒÂ£o estratÃƒÂ©gica
    # ========================================================

    def inteligencia(self):


        s = self.sensores


        if (

            s["mercado"] > 80 and

            s["demanda_cliente"] > 60 and

            s["risco_cibernetico"] < 40

        ):

            self.previsao["cenÃƒÂ¡rio"] = (
                "EXPANSÃƒÆ'O COM BAIXO RISCO"
            )



        elif s["risco_cibernetico"] > 70:


            self.previsao["cenÃƒÂ¡rio"] = (
                "AMEAÃƒâ€¡A DIGITAL DETECTADA"
            )


        else:


            self.previsao["cenÃƒÂ¡rio"] = (
                "MONITORAMENTO CONTÃƒÂNUO"
            )



        return self.previsao




    # ========================================================
    # CAMADA ORQUESTRADOR
    # Decide aÃƒÂ§ÃƒÂµes
    # ========================================================

    def executar_acoes(self):


        self.acoes.clear()


        cenario = self.previsao["cenÃƒÂ¡rio"]



        if cenario == "EXPANSÃƒÆ'O COM BAIXO RISCO":


            self.acoes.extend([

                "Gerar relatÃƒÂ³rio comercial",

                "Ativar mÃƒÂ³dulo de oportunidades",

                "Priorizar anÃƒÂ¡lise de mercado",

                "Criar estratÃƒÂ©gia de crescimento"

            ])




        elif cenario == "AMEAÃƒâ€¡A DIGITAL DETECTADA":


            self.acoes.extend([

                "Ativar defesa cibernÃƒÂ©tica",

                "Bloquear comportamento suspeito",

                "Gerar alerta de seguranÃƒÂ§a"

            ])




        else:


            self.acoes.append(

                "Continuar monitoramento inteligente"

            )


        return self.acoes





    # ========================================================
    # RELATÃƒâ€œRIO FINAL
    # ========================================================

    def relatorio(self):


        return {


            "SISTEMA":
            self.nome,


            "DATA":
            datetime.datetime.now(),


            "SENSORES":
            self.sensores,


            "ANÃƒÂLISE":
            self.analise,


            "PREVISÃƒÆ'O":
            self.previsao,


            "AÃƒâ€¡Ãƒâ€¢ES":
            self.acoes

        }





# ============================================================
# INICIALIZAÃƒâ€¡ÃƒÆ'O DO SISTEMA
# ============================================================


STORM = IOTEC_DigitalStorm()


STORM.coletar_sinais()

STORM.calcular_pressao()

STORM.inteligencia()

STORM.executar_acoes()



print("\n")
print("="*60)
print(" IOTEC DIGITAL STORM ENGINE V2.0 ")
print("="*60)



relatorio = STORM.relatorio()


for chave, valor in relatorio.items():

    print("\n", chave)

    print(valor)



