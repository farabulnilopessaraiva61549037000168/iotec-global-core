import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM STRATEGIC BRAIN ENGINE V5.0
#
# Motor de InteligÃƒÂªncia EstratÃƒÂ©gica IoTec
#
# FunÃƒÂ§ÃƒÂµes:
# - DiagnÃƒÂ³stico empresarial
# - ÃƒÂrvore de decisÃƒÂ£o
# - SimulaÃƒÂ§ÃƒÂ£o de cenÃƒÂ¡rios
# - ROI estratÃƒÂ©gico
# - Plano de aÃƒÂ§ÃƒÂ£o automÃƒÂ¡tico
#
# ============================================================


import random
import datetime
import json
import os



class IOTEC_StrategicBrain:


    def __init__(self):

        self.nome = (
            "IOTEC DIGITAL STORM STRATEGIC BRAIN V5.0"
        )

        self.dados = {}

        self.indices = {}

        self.diagnostico = ""

        self.arvore_decisao = []

        self.cenarios = {}

        self.roi = {}

        self.plano = []

        self.memoria = "IOTEC_STRATEGIC_MEMORY.json"



    # ========================================================
    # COLETA DE DADOS DO ECOSSISTEMA
    # ========================================================

    def coletar_dados(self):


        self.dados = {


            "mercado":
            random.randint(0,100),


            "clientes":
            random.randint(0,100),


            "inovacao":
            random.randint(0,100),


            "seguranca":
            random.randint(0,100),


            "infraestrutura":
            random.randint(0,100),


            "capital":
            random.randint(0,100),


            "processos":
            random.randint(0,100)

        }


        return self.dados




    # ========================================================
    # CÃƒÂLCULO DOS INDICADORES
    # ========================================================

    def calcular_inteligencia(self):


        d = self.dados


        oportunidade = (

            d["mercado"] * 0.25 +

            d["clientes"] * 0.25 +

            d["inovacao"] * 0.20 +

            d["infraestrutura"] * 0.15 +

            d["capital"] * 0.15

        )



        risco = (

            (100 - d["seguranca"]) * 0.40 +

            (100 - d["processos"]) * 0.30 +

            (100 - d["capital"]) * 0.30

        )



        self.indices = {


            "oportunidade":
            round(oportunidade,2),


            "risco":
            round(risco,2)

        }


        return self.indices




    # ========================================================
    # ÃƒÂRVORE DE DECISÃƒÆ'O
    # ========================================================

    def arvore_estrategica(self):


        d = self.dados



        self.arvore_decisao.clear()



        if d["mercado"] > 70:


            self.arvore_decisao.append(

                "Mercado favorÃƒÂ¡vel identificado"

            )


            if d["clientes"] < 40:

                self.arvore_decisao.append(

                    "Problema comercial detectado"

                )



        if d["capital"] < 40:


            self.arvore_decisao.append(

                "Capital insuficiente para expansÃƒÂ£o"

            )



        if d["inovacao"] < 40:


            self.arvore_decisao.append(

                "Necessidade de inovaÃƒÂ§ÃƒÂ£o tecnolÃƒÂ³gica"

            )



        if len(self.arvore_decisao)==0:


            self.arvore_decisao.append(

                "Nenhum gargalo crÃƒÂ­tico"

            )



        return self.arvore_decisao




    # ========================================================
    # SIMULADOR DE CENÃƒÂRIOS
    # ========================================================

    def simular_cenarios(self):


        atual = self.indices["oportunidade"]



        self.cenarios = {


            "cenÃƒÂ¡rio_atual":

            atual,



            "aumento_clientes_30%":

            round(atual * 1.30,2),



            "melhoria_inovacao_40%":

            round(atual * 1.20,2),



            "expansao_completa":

            round(atual * 1.60,2)

        }



        return self.cenarios




    # ========================================================
    # CALCULO DE ROI
    # ========================================================

    def calcular_roi(self):


        investimento = random.randint(
            5000,20000
        )


        retorno = investimento * (
            1 + self.indices["oportunidade"]/50
        )



        roi_percentual = (

            (retorno-investimento)
            /
            investimento
        )*100



        self.roi = {


            "investimento_estimado":
            investimento,


            "retorno_estimado":
            round(retorno,2),


            "ROI":
            round(roi_percentual,2)

        }



        return self.roi




    # ========================================================
    # PLANO ESTRATÃƒâ€°GICO AUTOMÃƒÂTICO
    # ========================================================

    def gerar_plano(self):


        self.plano.clear()



        if self.indices["oportunidade"] < 50:


            self.plano.append(

                "Fortalecer aquisiÃƒÂ§ÃƒÂ£o de clientes"

            )


        if self.indices["risco"] > 60:


            self.plano.append(

                "Aumentar proteÃƒÂ§ÃƒÂ£o operacional"

            )


        if self.dados["inovacao"] < 50:


            self.plano.append(

                "Investir em tecnologia"

            )


        if self.dados["capital"] < 40:


            self.plano.append(

                "Buscar novas fontes de financiamento"

            )



        if len(self.plano)==0:


            self.plano.append(

                "Executar expansÃƒÂ£o estratÃƒÂ©gica"

            )



        return self.plano




    # ========================================================
    # MEMÃƒâ€œRIA
    # ========================================================

    def salvar(self):


        registro = {


            "data":
            str(datetime.datetime.now()),


            "dados":
            self.dados,


            "indices":
            self.indices,


            "arvore":
            self.arvore_decisao,


            "cenarios":
            self.cenarios,


            "roi":
            self.roi,


            "plano":
            self.plano

        }



        memoria=[]



        if os.path.exists(self.memoria):

            with open(self.memoria,"r") as f:

                memoria=json.load(f)



        memoria.append(registro)



        with open(self.memoria,"w") as f:

            json.dump(
                memoria,
                f,
                indent=4,
                ensure_ascii=False
            )




    # ========================================================
    # RELATÃƒâ€œRIO
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


            "ÃƒÂRVORE":
            self.arvore_decisao,


            "CENÃƒÂRIOS":
            self.cenarios,


            "ROI":
            self.roi,


            "PLANO":
            self.plano

        }




# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ============================================================


BRAIN = IOTEC_StrategicBrain()


BRAIN.coletar_dados()

BRAIN.calcular_inteligencia()

BRAIN.arvore_estrategica()

BRAIN.simular_cenarios()

BRAIN.calcular_roi()

BRAIN.gerar_plano()

BRAIN.salvar()



print("\n")
print("="*70)
print(" IOTEC DIGITAL STORM STRATEGIC BRAIN V5.0 ")
print("="*70)



for chave, valor in BRAIN.relatorio().items():

    print("\n"+chave)

    print(valor)



