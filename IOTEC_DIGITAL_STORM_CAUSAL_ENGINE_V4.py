import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM CAUSAL ENGINE V4.0
#
# Motor Cognitivo ExplicÃƒÂ¡vel IoTec
#
# FunÃƒÂ§ÃƒÂµes:
# - Monitoramento do ecossistema
# - AnÃƒÂ¡lise causal
# - ExplicaÃƒÂ§ÃƒÂ£o das decisÃƒÂµes
# - AvaliaÃƒÂ§ÃƒÂ£o de impacto
# - RecomendaÃƒÂ§ÃƒÂµes estratÃƒÂ©gicas
#
# ============================================================


import datetime
import random
import json
import os



class IOTEC_CausalStorm:


    def __init__(self):

        self.nome = (
            "IOTEC DIGITAL STORM CAUSAL ENGINE V4.0"
        )

        self.dados = {}

        self.indices = {}

        self.diagnostico = {}

        self.causas = []

        self.impactos = []

        self.recomendacoes = []

        self.memoria = "IOTEC_CAUSAL_MEMORY.json"



    # ========================================================
    # SENSOR DO ECOSSISTEMA
    # ========================================================

    def coletar_dados(self):


        self.dados = {


            "mercado":
            random.randint(0,100),


            "demanda_cliente":
            random.randint(0,100),


            "inovacao_tecnologica":
            random.randint(0,100),


            "risco_cibernetico":
            random.randint(0,100),


            "infraestrutura":
            random.randint(0,100),


            "capital_disponivel":
            random.randint(0,100),


            "eficiencia_processos":
            random.randint(0,100)

        }


        return self.dados



    # ========================================================
    # MOTOR MATEMÃƒÂTICO
    # ========================================================

    def calcular_indices(self):


        d = self.dados



        oportunidade = (

            d["mercado"] * 0.25 +

            d["demanda_cliente"] * 0.30 +

            d["inovacao_tecnologica"] * 0.20 +

            d["infraestrutura"] * 0.15 +

            d["capital_disponivel"] * 0.10

        )



        risco = (

            d["risco_cibernetico"] * 0.45 +

            (100 - d["eficiencia_processos"]) * 0.35 +

            (100 - d["capital_disponivel"]) * 0.20

        )



        self.indices = {


            "oportunidade":

            round(oportunidade,2),



            "risco":

            round(risco,2)

        }


        return self.indices




    # ========================================================
    # ANÃƒÂLISE CAUSAL
    # ========================================================

    def analisar_causas(self):


        d = self.dados


        self.causas.clear()



        if d["risco_cibernetico"] > 70:

            self.causas.append(

                "Alta exposiÃƒÂ§ÃƒÂ£o a ameaÃƒÂ§as digitais"

            )


        if d["eficiencia_processos"] < 50:

            self.causas.append(

                "Baixa eficiÃƒÂªncia operacional"

            )


        if d["capital_disponivel"] < 40:

            self.causas.append(

                "RestriÃƒÂ§ÃƒÂ£o financeira"

            )


        if d["demanda_cliente"] < 40:

            self.causas.append(

                "Baixa geraÃƒÂ§ÃƒÂ£o de demanda comercial"

            )


        if d["infraestrutura"] < 50:

            self.causas.append(

                "Infraestrutura insuficiente"

            )



        if len(self.causas) == 0:

            self.causas.append(

                "Nenhum fator crÃƒÂ­tico identificado"

            )



        return self.causas




    # ========================================================
    # MOTOR DE IMPACTO
    # ========================================================

    def analisar_impacto(self):


        self.impactos.clear()



        if self.indices["risco"] > 70:


            self.impactos.append(

                "PossÃƒÂ­vel perda operacional"

            )


            self.impactos.append(

                "Necessidade de reforÃƒÂ§o de seguranÃƒÂ§a"

            )



        elif self.indices["oportunidade"] > 70:


            self.impactos.append(

                "Possibilidade de expansÃƒÂ£o comercial"

            )


            self.impactos.append(

                "Aumento de mercado"

            )


        else:


            self.impactos.append(

                "Manter acompanhamento estratÃƒÂ©gico"

            )



        return self.impactos




    # ========================================================
    # DIAGNÃƒâ€œSTICO FINAL
    # ========================================================

    def diagnosticar(self):


        risco = self.indices["risco"]

        oportunidade = self.indices["oportunidade"]



        if risco > 70:


            estado = "ECOSSISTEMA EM ALERTA"



        elif oportunidade > 70:


            estado = "JANELA DE EXPANSÃƒÆ'O"



        else:


            estado = "EQUILÃƒÂBRIO OPERACIONAL"



        self.diagnostico = {


            "estado":

            estado,


            "explicacao":

            "DecisÃƒÂ£o baseada em anÃƒÂ¡lise causal dos indicadores."

        }


        return self.diagnostico




    # ========================================================
    # RECOMENDAÃƒâ€¡ÃƒÆ'O ESTRATÃƒâ€°GICA
    # ========================================================

    def gerar_recomendacoes(self):


        self.recomendacoes.clear()



        if self.indices["risco"] > 70:


            self.recomendacoes.extend([

                "Executar auditoria de seguranÃƒÂ§a",

                "Fortalecer infraestrutura",

                "Criar plano de contingÃƒÂªncia"

            ])



        elif self.indices["oportunidade"] > 70:


            self.recomendacoes.extend([

                "Expandir vendas",

                "Criar novos projetos",

                "Buscar parceiros"

            ])



        else:


            self.recomendacoes.extend([

                "Continuar monitoramento",

                "Otimizar processos"

            ])



        return self.recomendacoes




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


            "diagnostico":
            self.diagnostico,


            "causas":
            self.causas,


            "impactos":
            self.impactos,


            "recomendacoes":
            self.recomendacoes

        }



        historico = []



        if os.path.exists(self.memoria):

            with open(self.memoria,"r") as arquivo:

                historico = json.load(arquivo)



        historico.append(registro)



        with open(self.memoria,"w") as arquivo:

            json.dump(

                historico,

                arquivo,

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


            "DIAGNÃƒâ€œSTICO":
            self.diagnostico,


            "CAUSAS":
            self.causas,


            "IMPACTOS":
            self.impactos,


            "RECOMENDAÃƒâ€¡Ãƒâ€¢ES":
            self.recomendacoes

        }




# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O DO IOTEC DIGITAL STORM V4
# ============================================================


STORM = IOTEC_CausalStorm()


STORM.coletar_dados()

STORM.calcular_indices()

STORM.analisar_causas()

STORM.analisar_impacto()

STORM.diagnosticar()

STORM.gerar_recomendacoes()

STORM.salvar_memoria()



print("\n")
print("="*70)
print(" IOTEC DIGITAL STORM CAUSAL ENGINE V4.0 ")
print("="*70)



relatorio = STORM.relatorio()



for chave, valor in relatorio.items():

    print("\n"+chave)

    print(valor)



