import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC DIGITAL STORM ENGINE
# NÃƒÂºcleo Inteligente de AdaptaÃƒÂ§ÃƒÂ£o e OrquestraÃƒÂ§ÃƒÂ£o EcossistÃƒÂªmica
#
# FunÃƒÂ§ÃƒÂ£o:
# Monitorar ambientes digitais, analisar mudanÃƒÂ§as,
# prever cenÃƒÂ¡rios e executar respostas estratÃƒÂ©gicas.
#
# Desenvolvido para arquitetura IoTec
# ============================================================

import datetime
import random


class DigitalStormEngine:

    def __init__(self, nome="IOTEC DIGITAL STORM"):
        self.nome = nome
        self.estado_ecossistema = {}
        self.alertas = []
        self.acoes = []


    # --------------------------------------------------------
    # SENSOR DIGITAL
    # Coleta informaÃƒÂ§ÃƒÂµes do ambiente
    # --------------------------------------------------------

    def coletar_dados(self):

        dados = {
            "mercado": random.randint(0, 100),
            "risco": random.randint(0, 100),
            "oportunidade": random.randint(0, 100),
            "energia_computacional": random.randint(0,100),
            "clima_operacional": random.randint(0,100)
        }

        self.estado_ecossistema = dados

        return dados


    # --------------------------------------------------------
    # MOTOR DE INTELIGÃƒÅ NCIA
    # Analisa o ambiente
    # --------------------------------------------------------

    def analisar_ambiente(self):

        dados = self.estado_ecossistema

        resultado = {}

        for elemento, valor in dados.items():

            if valor >= 70:
                resultado[elemento] = "ALTA ATIVIDADE"

            elif valor >= 40:
                resultado[elemento] = "ESTABILIDADE"

            else:
                resultado[elemento] = "BAIXA ATIVIDADE"

        return resultado



    # --------------------------------------------------------
    # PREVISÃƒÆ'O DE CENÃƒÂRIOS
    # --------------------------------------------------------

    def prever_cenarios(self):

        dados = self.estado_ecossistema

        previsao = {}

        if dados["oportunidade"] > 70:
            previsao["mercado"] = "EXPANSÃƒÆ'O IDENTIFICADA"
        else:
            previsao["mercado"] = "MONITORAMENTO CONTÃƒÂNUO"


        if dados["risco"] > 70:
            previsao["seguranca"] = "ATIVAR DEFESA DIGITAL"
        else:
            previsao["seguranca"] = "SISTEMA NORMAL"


        return previsao



    # --------------------------------------------------------
    # ORQUESTRADOR DE DECISÃƒâ€¢ES
    # Transforma anÃƒÂ¡lise em aÃƒÂ§ÃƒÂ£o
    # --------------------------------------------------------

    def executar_resposta(self):

        analise = self.analisar_ambiente()
        previsao = self.prever_cenarios()


        if "EXPANSÃƒÆ'O IDENTIFICADA" in previsao.values():

            self.acoes.append(
                "Ativar mÃƒÂ³dulo comercial e gerar oportunidades"
            )


        if "ATIVAR DEFESA DIGITAL" in previsao.values():

            self.acoes.append(
                "Executar protocolo de proteÃƒÂ§ÃƒÂ£o"
            )


        return self.acoes



    # --------------------------------------------------------
    # RELATÃƒâ€œRIO DO SISTEMA
    # --------------------------------------------------------

    def relatorio(self):

        return {

            "Sistema": self.nome,

            "Data":
            datetime.datetime.now(),

            "Ambiente":
            self.estado_ecossistema,

            "AnÃƒÂ¡lise":
            self.analisar_ambiente(),

            "PrevisÃƒÂ£o":
            self.prever_cenarios(),

            "AÃƒÂ§ÃƒÂµes":
            self.acoes
        }



# ============================================================
# EXECUÃƒâ€¡ÃƒÆ'O DO NÃƒÅ¡CLEO
# ============================================================

IOTEC_STORM = DigitalStormEngine()


IOTEC_STORM.coletar_dados()

IOTEC_STORM.executar_resposta()


print("\n===== RELATÃƒâ€œRIO IOTEC DIGITAL STORM =====")

for chave, valor in IOTEC_STORM.relatorio().items():

    print(f"\n{chave}:")
    print(valor)



