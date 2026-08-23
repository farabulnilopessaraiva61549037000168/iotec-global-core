import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM COGNITIVE ENGINE V3.0
#
# Motor Cognitivo de InteligÃƒÂªncia EstratÃƒÂ©gica
# Arquitetura IoTec
#
# FunÃƒÂ§ÃƒÂµes:
# - AnÃƒÂ¡lise do ambiente digital
# - CÃƒÂ¡lculo de oportunidade
# - AvaliaÃƒÂ§ÃƒÂ£o de risco
# - RecomendaÃƒÂ§ÃƒÂ£o estratÃƒÂ©gica
# - MemÃƒÂ³ria histÃƒÂ³rica
#
# ============================================================


import datetime
import random
import json
import os



class IOTEC_CognitiveStorm:


    def __init__(self):

        self.nome = "IOTEC DIGITAL STORM COGNITIVE ENGINE V3.0"

        self.dados = {}

        self.indices = {}

        self.diagnostico = {}

        self.recomendacoes = []

        self.historico = "IOTEC_STORM_MEMORY.json"



    # ========================================================
    # SENSOR DIGITAL
    # ========================================================

    def coletar_dados(self):


        self.dados = {


            "mercado":
            random.randint(0,100),


            "demanda_cliente":
            random.randint(0,100),


            "tendencia_tecnologica":
            random.randint(0,100),


            "risco_cibernetico":
            random.randint(0,100),


            "capacidade_computacional":
            random.randint(0,100),


            "recursos_financeiros":
            random.randint(0,100),


            "eficiencia_operacional":
            random.randint(0,100)

        }


        return self.dados



    # ========================================================
    # CÃƒÂLCULO DE INTELIGÃƒÅ NCIA
    # ========================================================

    def calcular_indices(self):


        d = self.dados



        oportunidade = (

            d["demanda_cliente"] * 0.30 +

            d["mercado"] * 0.20 +

            d["tendencia_tecnologica"] * 0.20 +

            d["capacidade_computacional"] * 0.15 +

            d["recursos_financeiros"] * 0.15

        )



        risco = (

            d["risco_cibernetico"] * 0.60 +

            (100 - d["eficiencia_operacional"]) * 0.40

        )



        self.indices = {


            "indice_oportunidade":
            round(oportunidade,2),


            "indice_risco":
            round(risco,2)

        }



        return self.indices




    # ========================================================
    # CÃƒâ€°REBRO ESTRATÃƒâ€°GICO
    # ========================================================

    def analisar_cenario(self):


        oportunidade = self.indices["indice_oportunidade"]

        risco = self.indices["indice_risco"]



        if oportunidade >= 75 and risco < 40:


            self.diagnostico["estado"] = (

                "EXPANSÃƒÆ'O ESTRATÃƒâ€°GICA"

            )



        elif oportunidade >= 60:


            self.diagnostico["estado"] = (

                "OPORTUNIDADE IDENTIFICADA"

            )



        elif risco >= 70:


            self.diagnostico["estado"] = (

                "AMBIENTE DE RISCO"

            )



        else:


            self.diagnostico["estado"] = (

                "ESTABILIDADE OPERACIONAL"

            )



        return self.diagnostico




    # ========================================================
    # MOTOR DE RECOMENDAÃƒâ€¡ÃƒÆ'O
    # ========================================================

    def gerar_recomendacoes(self):


        self.recomendacoes.clear()



        estado = self.diagnostico["estado"]



        if estado == "EXPANSÃƒÆ'O ESTRATÃƒâ€°GICA":


            self.recomendacoes.extend([

                "Aumentar prospecÃƒÂ§ÃƒÂ£o comercial",

                "Criar novos projetos",

                "Ativar parceiros estratÃƒÂ©gicos",

                "Expandir inteligÃƒÂªncia de mercado"

            ])




        elif estado == "OPORTUNIDADE IDENTIFICADA":


            self.recomendacoes.extend([

                "Monitorar clientes potenciais",

                "Preparar propostas comerciais",

                "Analisar investimentos"

            ])




        elif estado == "AMBIENTE DE RISCO":


            self.recomendacoes.extend([

                "ReforÃƒÂ§ar seguranÃƒÂ§a digital",

                "Auditar sistemas",

                "Reduzir exposiÃƒÂ§ÃƒÂ£o operacional"

            ])




        else:


            self.recomendacoes.append(

                "Manter monitoramento contÃƒÂ­nuo"

            )


        return self.recomendacoes





    # ========================================================
    # MEMÃƒâ€œRIA DO SISTEMA
    # ========================================================

    def salvar_memoria(self):


        registro = {


            "data":
            str(datetime.datetime.now()),


            "dados":
            self.dados,


            "indices":
            self.indices,


            "diagnostico":
            self.diagnostico,


            "recomendacoes":
            self.recomendacoes

        }



        memoria = []



        if os.path.exists(self.historico):

            with open(self.historico,"r") as arquivo:

                memoria = json.load(arquivo)



        memoria.append(registro)



        with open(self.historico,"w") as arquivo:

            json.dump(

                memoria,

                arquivo,

                indent=4,

                ensure_ascii=False

            )





    # ========================================================
    # RELATÃƒâ€œRIO EXECUTIVO
    # ========================================================

    def relatorio(self):


        return {


            "SISTEMA":

            self.nome,


            "DATA":

            datetime.datetime.now(),


            "DADOS":

            self.dados,


            "ÃƒÂNDICES":

            self.indices,


            "DIAGNÃƒâ€œSTICO":

            self.diagnostico,


            "RECOMENDAÃƒâ€¡Ãƒâ€¢ES":

            self.recomendacoes

        }





# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O DO NÃƒÅ¡CLEO
# ============================================================


STORM = IOTEC_CognitiveStorm()


STORM.coletar_dados()

STORM.calcular_indices()

STORM.analisar_cenario()

STORM.gerar_recomendacoes()

STORM.salvar_memoria()



print("\n")
print("="*65)
print(" IOTEC DIGITAL STORM COGNITIVE ENGINE V3.0 ")
print("="*65)



relatorio = STORM.relatorio()



for item, valor in relatorio.items():

    print("\n"+item)

    print(valor)



