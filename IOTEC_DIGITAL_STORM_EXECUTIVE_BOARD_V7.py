import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM EXECUTIVE BOARD V7.0
#
# Diretoria Virtual de InteligÃƒÂªncia EstratÃƒÂ©gica IoTec
#
# Agentes:
# - CEO AI
# - Market AI
# - Finance AI
# - Security AI
# - Technology AI
# - Operations AI
# - Projects AI
#
# ============================================================


import datetime
import random
import json
import os



class IOTEC_ExecutiveBoard:


    def __init__(self):

        self.nome = (
            "IOTEC DIGITAL STORM EXECUTIVE BOARD V7.0"
        )

        self.dados = {}

        self.indices = {}

        self.pareceres = {}

        self.decisao_ceo = ""

        self.memoria = (
            "IOTEC_EXECUTIVE_BOARD_MEMORY.json"
        )



    # ========================================================
    # SENSOR DO ECOSSISTEMA
    # ========================================================

    def coletar_dados(self):

        self.dados = {


            "mercado":
            random.randint(0,100),


            "clientes":
            random.randint(0,100),


            "financeiro":
            random.randint(0,100),


            "seguranca":
            random.randint(0,100),


            "tecnologia":
            random.randint(0,100),


            "operacao":
            random.randint(0,100),


            "projetos":
            random.randint(0,100)

        }


        return self.dados




    # ========================================================
    # CÃƒÂLCULO DOS INDICADORES
    # ========================================================

    def analisar_indices(self):

        d = self.dados


        oportunidade = (

            d["mercado"] * 0.20 +

            d["clientes"] * 0.20 +

            d["financeiro"] * 0.20 +

            d["tecnologia"] * 0.20 +

            d["projetos"] * 0.20

        )


        risco = (

            (100-d["seguranca"]) * 0.35 +

            (100-d["operacao"]) * 0.40 +

            (100-d["financeiro"]) * 0.25

        )


        self.indices = {

            "oportunidade":
            round(oportunidade,2),

            "risco":
            round(risco,2)

        }




    # ========================================================
    # AGENTES DA DIRETORIA
    # ========================================================


    def market_ai(self):

        if self.dados["mercado"] > 70:

            return "Mercado favorÃƒÂ¡vel para crescimento"

        return "Mercado exige anÃƒÂ¡lise"



    def finance_ai(self):

        if self.dados["financeiro"] > 70:

            return "Capital disponÃƒÂ­vel para investimento"

        return "Controle financeiro necessÃƒÂ¡rio"



    def security_ai(self):

        if self.dados["seguranca"] < 50:

            return "ALERTA: reforÃƒÂ§ar seguranÃƒÂ§a digital"

        return "SeguranÃƒÂ§a adequada"



    def technology_ai(self):

        if self.dados["tecnologia"] < 50:

            return "NecessÃƒÂ¡rio acelerar inovaÃƒÂ§ÃƒÂ£o"

        return "Tecnologia preparada"



    def operations_ai(self):

        if self.dados["operacao"] < 50:

            return "ALERTA: processos operacionais fracos"

        return "OperaÃƒÂ§ÃƒÂ£o estÃƒÂ¡vel"



    def projects_ai(self):

        if self.dados["projetos"] > 70:

            return "Alta capacidade de projetos"

        return "Pipeline moderado"




    # ========================================================
    # REUNIÃƒÆ'O DA DIRETORIA
    # ========================================================

    def reuniao_diretoria(self):


        self.pareceres = {


            "MARKET_AI":
            self.market_ai(),


            "FINANCE_AI":
            self.finance_ai(),


            "SECURITY_AI":
            self.security_ai(),


            "TECHNOLOGY_AI":
            self.technology_ai(),


            "OPERATIONS_AI":
            self.operations_ai(),


            "PROJECTS_AI":
            self.projects_ai()

        }





    # ========================================================
    # CEO ARTIFICIAL
    # DECISÃƒÆ'O FINAL
    # ========================================================

    def decisao_ceo_ai(self):


        risco = self.indices["risco"]

        oportunidade = self.indices["oportunidade"]



        if risco > 70:


            self.decisao_ceo = (

                "DECISÃƒÆ'O CEO AI: "
                "Prioridade mÃƒÂ¡xima em correÃƒÂ§ÃƒÂ£o de riscos."

            )



        elif oportunidade > 75:


            self.decisao_ceo = (

                "DECISÃƒÆ'O CEO AI: "
                "Executar expansÃƒÂ£o estratÃƒÂ©gica."

            )



        else:


            self.decisao_ceo = (

                "DECISÃƒÆ'O CEO AI: "
                "Otimizar estrutura antes de crescer."

            )





    # ========================================================
    # MEMÃƒâ€œRIA
    # ========================================================

    def salvar_memoria(self):


        registro = {


            "data":
            str(datetime.datetime.now()),


            "dados":
            self.dados,


            "indices":
            self.indices,


            "pareceres":
            self.pareceres,


            "decisao":
            self.decisao_ceo

        }



        historico=[]


        if os.path.exists(self.memoria):

            with open(self.memoria,"r") as arquivo:

                historico=json.load(arquivo)



        historico.append(registro)



        with open(self.memoria,"w") as arquivo:

            json.dump(

                historico,

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


            "DIRETORIA":
            self.pareceres,


            "CEO_AI":
            self.decisao_ceo

        }





# ============================================================
# INICIALIZAÃƒâ€¡ÃƒÆ'O
# ============================================================


BOARD = IOTEC_ExecutiveBoard()


BOARD.coletar_dados()

BOARD.analisar_indices()

BOARD.reuniao_diretoria()

BOARD.decisao_ceo_ai()

BOARD.salvar_memoria()



print("\n")
print("="*75)
print(" IOTEC DIGITAL STORM EXECUTIVE BOARD V7.0 ")
print("="*75)



for chave, valor in BOARD.relatorio().items():

    print("\n"+chave)

    print(valor)



