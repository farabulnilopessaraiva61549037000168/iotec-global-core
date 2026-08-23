import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM DATA INTELLIGENCE ENGINE V9.0
#
# NÃƒÂºcleo de InteligÃƒÂªncia Empresarial IoTec
#
# FunÃƒÂ§ÃƒÂµes:
# - SaÃƒÂºde do ecossistema
# - Indicadores estratÃƒÂ©gicos
# - TendÃƒÂªncias
# - PrevisÃƒÂ£o
# - RelatÃƒÂ³rio executivo
#
# ============================================================


import json
import datetime
import os



class IOTEC_DataIntelligence:


    def __init__(self):

        self.nome = (
            "IOTEC DIGITAL STORM DATA INTELLIGENCE V9.0"
        )

        self.arquivo = "IOTEC_REAL_DATA.json"

        self.dados = {}

        self.indicadores = {}

        self.saude = 0

        self.forcas = []

        self.alertas = []

        self.previsao = {}



    # ========================================================
    # CARREGAR DADOS
    # ========================================================

    def carregar_dados(self):

        if not os.path.exists(self.arquivo):

            print("Arquivo de dados nÃƒÂ£o encontrado.")

            return


        with open(
            self.arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:

            self.dados = json.load(arquivo)



    # ========================================================
    # INDICE DE SAÃƒÅ¡DE DO ECOSSISTEMA
    # ========================================================

    def calcular_saude(self):


        d = self.dados


        financeiro = 0


        if d["receita_mensal"] > 0:

            margem = (

                (d["receita_mensal"]
                 -
                 d["despesas_mensais"])

                /

                d["receita_mensal"]

            ) * 100


            financeiro = min(margem,100)



        self.saude = (

            financeiro * 0.30 +

            min(d["clientes"]*5,100) * 0.20 +

            min(d["projetos_ativos"]*10,100) * 0.20 +

            (100-d["risco_cibernetico"]) * 0.15 +

            d["eficiencia_operacional"] * 0.15

        )


        self.saude = round(
            self.saude,
            2
        )




    # ========================================================
    # ANÃƒÂLISE ESTRATÃƒâ€°GICA
    # ========================================================

    def analisar(self):


        d = self.dados


        if d["receita_mensal"] > d["despesas_mensais"]*2:

            self.forcas.append(
                "Boa capacidade financeira"
            )


        if d["clientes"] < 20:

            self.alertas.append(
                "Necessidade de expansÃƒÂ£o comercial"
            )


        if d["projetos_ativos"] < 10:

            self.alertas.append(
                "Aumentar pipeline de projetos"
            )


        if d["risco_cibernetico"] > 50:

            self.alertas.append(
                "Melhorar seguranÃƒÂ§a digital"
            )


        if d["tecnologia"] if "tecnologia" in d else False:

            pass




    # ========================================================
    # PREVISÃƒÆ'O SIMPLES
    # ========================================================

    def prever_crescimento(self):


        receita = self.dados["receita_mensal"]


        crescimento = 1.10


        self.previsao = {


            "receita_atual":

            receita,


            "proxima_estimativa":

            round(
                receita*crescimento,
                2
            ),


            "crescimento_estimado":

            "10%"

        }




    # ========================================================
    # RELATÃƒâ€œRIO
    # ========================================================

    def relatorio(self):


        return {


            "SISTEMA":

            self.nome,


            "DATA":

            str(datetime.datetime.now()),


            "SAUDE_ECOSSISTEMA":

            self.saude,


            "DADOS":

            self.dados,


            "FORCAS":

            self.forcas,


            "ALERTAS":

            self.alertas,


            "PREVISAO":

            self.previsao

        }




# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ============================================================


CORE = IOTEC_DataIntelligence()


CORE.carregar_dados()

CORE.calcular_saude()

CORE.analisar()

CORE.prever_crescimento()



print("\n")
print("="*75)
print(" IOTEC DIGITAL STORM DATA INTELLIGENCE V9.0 ")
print("="*75)



for chave, valor in CORE.relatorio().items():

    print("\n"+chave)

    print(valor)



