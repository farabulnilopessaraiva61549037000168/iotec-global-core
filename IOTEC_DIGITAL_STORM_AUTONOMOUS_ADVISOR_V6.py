import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM AUTONOMOUS ADVISOR ENGINE V6.0
#
# Conselheiro Digital EstratÃƒÂ©gico IoTec
#
# MÃƒÂ³dulos:
# - Market AI
# - Commercial AI
# - Security AI
# - Finance AI
# - Technology AI
# - Project AI
#
# ============================================================


import datetime
import random
import json
import os



class IOTEC_AutonomousAdvisor:


    def __init__(self):

        self.nome = (
            "IOTEC DIGITAL STORM AUTONOMOUS ADVISOR V6.0"
        )

        self.dados = {}

        self.indices = {}

        self.agentes = {}

        self.relatorio = {}

        self.memoria = (
            "IOTEC_AUTONOMOUS_MEMORY.json"
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


            "seguranca":
            random.randint(0,100),


            "tecnologia":
            random.randint(0,100),


            "financeiro":
            random.randint(0,100),


            "projetos":
            random.randint(0,100),


            "operacao":
            random.randint(0,100)

        }


        return self.dados




    # ========================================================
    # MOTOR DE ÃƒÂNDICES
    # ========================================================

    def calcular_indices(self):


        d = self.dados



        oportunidade = (

            d["mercado"] * 0.25 +

            d["clientes"] * 0.20 +

            d["tecnologia"] * 0.20 +

            d["projetos"] * 0.20 +

            d["financeiro"] * 0.15

        )



        risco = (

            (100-d["seguranca"]) * 0.40 +

            (100-d["operacao"]) * 0.30 +

            (100-d["financeiro"]) * 0.30

        )



        self.indices = {


            "oportunidade":
            round(min(oportunidade,100),2),


            "risco":
            round(min(risco,100),2)

        }




    # ========================================================
    # AGENTE DE MERCADO
    # ========================================================

    def market_ai(self):


        if self.dados["mercado"] > 70:

            return (
                "Mercado favorÃƒÂ¡vel para expansÃƒÂ£o"
            )

        else:

            return (
                "Mercado necessita monitoramento"
            )




    # ========================================================
    # AGENTE COMERCIAL
    # ========================================================

    def commercial_ai(self):


        if self.dados["clientes"] < 40:

            return (
                "Criar estratÃƒÂ©gia de aquisiÃƒÂ§ÃƒÂ£o de clientes"
            )


        return (
            "Base comercial saudÃƒÂ¡vel"
        )




    # ========================================================
    # AGENTE DE SEGURANÃƒâ€¡A
    # ========================================================

    def security_ai(self):


        if self.dados["seguranca"] < 50:

            return (
                "Prioridade: fortalecer seguranÃƒÂ§a digital"
            )


        return (
            "SeguranÃƒÂ§a operacional adequada"
        )




    # ========================================================
    # AGENTE FINANCEIRO
    # ========================================================

    def finance_ai(self):


        if self.dados["financeiro"] < 40:

            return (
                "NecessÃƒÂ¡rio aumentar capacidade financeira"
            )


        return (
            "SaÃƒÂºde financeira aceitÃƒÂ¡vel"
        )




    # ========================================================
    # AGENTE TECNOLÃƒâ€œGICO
    # ========================================================

    def technology_ai(self):


        if self.dados["tecnologia"] < 50:

            return (
                "Investir em inovaÃƒÂ§ÃƒÂ£o tecnolÃƒÂ³gica"
            )


        return (
            "Tecnologia em nÃƒÂ­vel adequado"
        )




    # ========================================================
    # AGENTE DE PROJETOS
    # ========================================================

    def project_ai(self):


        if self.dados["projetos"] > 70:

            return (
                "Grande potencial de novos projetos"
            )


        return (
            "Pipeline de projetos moderado"
        )




    # ========================================================
    # CONSELHEIRO CENTRAL
    # ========================================================

    def gerar_conselho(self):


        recomendacoes = []


        recomendacoes.append(
            self.market_ai()
        )

        recomendacoes.append(
            self.commercial_ai()
        )

        recomendacoes.append(
            self.security_ai()
        )

        recomendacoes.append(
            self.finance_ai()
        )

        recomendacoes.append(
            self.technology_ai()
        )

        recomendacoes.append(
            self.project_ai()
        )



        prioridade = "MÃƒâ€°DIA"



        if self.indices["oportunidade"] > 75:

            prioridade = "ALTA"



        if self.indices["risco"] > 70:

            prioridade = "CRÃƒÂTICA"



        self.agentes = {


            "prioridade":
            prioridade,


            "recomendaÃƒÂ§ÃƒÂµes":
            recomendacoes

        }




    # ========================================================
    # RELATÃƒâ€œRIO EXECUTIVO
    # ========================================================

    def gerar_relatorio(self):


        self.relatorio = {


            "SISTEMA":
            self.nome,


            "DATA":
            str(datetime.datetime.now()),


            "DADOS":
            self.dados,


            "INDICES":
            self.indices,


            "DECISÃƒÆ'O":
            self.agentes

        }


        return self.relatorio




    # ========================================================
    # MEMÃƒâ€œRIA
    # ========================================================

    def salvar_memoria(self):


        historico=[]


        if os.path.exists(self.memoria):

            with open(self.memoria,"r") as f:

                historico=json.load(f)



        historico.append(
            self.relatorio
        )



        with open(self.memoria,"w") as f:

            json.dump(
                historico,
                f,
                indent=4,
                ensure_ascii=False
            )





# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ============================================================


ADVISOR = IOTEC_AutonomousAdvisor()


ADVISOR.coletar_dados()

ADVISOR.calcular_indices()

ADVISOR.gerar_conselho()

ADVISOR.gerar_relatorio()

ADVISOR.salvar_memoria()



print("\n")
print("="*75)
print(" IOTEC DIGITAL STORM AUTONOMOUS ADVISOR V6.0 ")
print("="*75)



for chave, valor in ADVISOR.relatorio.items():

    print("\n"+chave)

    print(valor)



