import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM DATA CORE V8.0
#
# NÃƒÂºcleo Real de InteligÃƒÂªncia de Dados
#
# ============================================================

import json
import datetime
import os


class IOTEC_DataCore:


    def __init__(self):

        self.nome = "IOTEC DIGITAL STORM DATA CORE V8.0"

        self.arquivo = "IOTEC_REAL_DATA.json"

        self.dados = {}

        self.indicadores = {}

        self.diagnostico = []

        self.recomendacoes = []


    def carregar_dados(self):

        if not os.path.exists(self.arquivo):

            print("Banco de dados nÃƒÂ£o encontrado.")

            return


        with open(self.arquivo, "r", encoding="utf-8") as arquivo:

            self.dados = json.load(arquivo)



    def analisar(self):

        receita = self.dados["receita_mensal"]

        despesas = self.dados["despesas_mensais"]


        lucro = receita - despesas


        margem = 0


        if receita > 0:

            margem = (lucro / receita) * 100



        self.indicadores = {

            "lucro_mensal":
            lucro,

            "margem_percentual":
            round(margem,2),

            "clientes":
            self.dados["clientes"],

            "projetos":
            self.dados["projetos_ativos"]

        }



    def diagnosticar(self):


        if self.dados["clientes"] < 10:

            self.diagnostico.append(
                "Baixa base comercial"
            )

            self.recomendacoes.append(
                "Aumentar aquisiÃƒÂ§ÃƒÂ£o de clientes"
            )


        if self.dados["risco_cibernetico"] > 70:

            self.diagnostico.append(
                "Risco cibernÃƒÂ©tico elevado"
            )

            self.recomendacoes.append(
                "Executar auditoria de seguranÃƒÂ§a"
            )


        if self.dados["eficiencia_operacional"] < 50:

            self.diagnostico.append(
                "Baixa eficiÃƒÂªncia operacional"
            )

            self.recomendacoes.append(
                "Otimizar processos"
            )


        if len(self.diagnostico) == 0:

            self.diagnostico.append(
                "Ecossistema saudÃƒÂ¡vel"
            )



    def relatorio(self):

        return {


            "SISTEMA":
            self.nome,


            "DATA":
            str(datetime.datetime.now()),


            "DADOS":
            self.dados,


            "INDICADORES":
            self.indicadores,


            "DIAGNOSTICO":
            self.diagnostico,


            "RECOMENDACOES":
            self.recomendacoes

        }



# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O DO NÃƒÅ¡CLEO
# ============================================================


CORE = IOTEC_DataCore()


CORE.carregar_dados()

CORE.analisar()

CORE.diagnosticar()


print("\n")
print("="*70)
print(" IOTEC DIGITAL STORM DATA CORE V8.0 ")
print("="*70)



for chave, valor in CORE.relatorio().items():

    print("\n" + chave)

    print(valor)



