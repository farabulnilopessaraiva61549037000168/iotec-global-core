import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===================================
# IOTEC STRATEGIC CORE LOGIC
# ===================================

from datetime import datetime

CORE_IDENTITY = {

    "nome": "IOTEC",
    "modo": "REAL",
    "simulacao": False,

    "missao":

        "Transformar problemas reais "
        "em produtos, servicos e receita.",

    "objetivo":

        "Captar demanda, gerar valor, "
        "entregar solucoes e monetizar."
}

# ===================================
# PRINCIPIOS
# ===================================

PRINCIPIOS = [

    "OBSERVAR",
    "REPORTAR",
    "ANALISAR",
    "DECIDIR",
    "EXECUTAR",
    "VALIDAR",
    "APRENDER"

]

# ===================================
# O NUCLEO NAO VENDE TECNOLOGIA
# VENDE SOLUCAO
# ===================================

PRODUTOS_ESTRATEGICOS = [

    "ANALISE_DE_DADOS",
    "MODELAGEM_MATEMATICA",
    "ANALISE_DE_CENARIOS",
    "AUDITORIA_TECNICA",
    "PERICIA_DIGITAL",
    "AUTOMACAO",
    "PAINEIS_EXECUTIVOS",
    "INTELIGENCIA_DE_MERCADO"

]

# ===================================
# SENSORES
# ===================================

SENSORES = {

    "formularios": True,
    "portais": True,
    "sites": True,
    "war_room": True,
    "financeiro": True,
    "paypal": True,
    "sentinel": True

}

# ===================================
# O QUE O NUCLEO PROCURA
# ===================================

DEMANDAS = [

    "REDUCAO_DE_CUSTOS",
    "AUMENTO_DE_RECEITA",
    "OTIMIZACAO",
    "PREVISAO",
    "RISCO",
    "AUDITORIA",
    "AUTOMACAO",
    "GESTAO"

]

# ===================================
# JORNADA DO CLIENTE
# ===================================

CLIENT_JOURNEY = [

    "CAPTACAO",
    "IDENTIFICACAO_DO_PROBLEMA",
    "ANALISE",
    "ORCAMENTO",
    "FATURA",
    "PAGAMENTO",
    "CONFIRMACAO",
    "EXECUCAO",
    "ENTREGA",
    "POS_VENDA"

]

# ===================================
# REGRA DO CAIXA
# ===================================

CAIXA = {

    "responsabilidade":

        "Receber pagamentos "
        "e informar ao nucleo.",

    "banco":

        "PAYPAL",

    "acao_pos_pagamento":

        "LIBERAR_EXECUCAO"
}

# ===================================
# CONCIERGE
# ===================================

CONCIERGE = {

    "funcao":

        "Monitorar trafego, "
        "formularios, leads, "
        "oportunidades e receita.",

    "relatorio":

        True,

    "sinal_de_vida":

        True
}

# ===================================
# ANALISE DE CENARIOS
# ===================================

SCENARIO_ENGINE = {

    "objetivo":

        "Calcular cenarios, "
        "riscos e oportunidades.",

    "inspiraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o":

        "Modelagem matematica "
        "e simulacao computacional."
}

# ===================================
# PILOTO AUTOMATICO
# ===================================

AUTOPILOT = {

    "ativo": True,

    "missao":

        "Manter operacao, "
        "receber pagamentos, "
        "registrar eventos "
        "e preservar continuidade."
}

# ===================================
# SINAL DE VIDA
# ===================================

print("")
print("===================================")
print("IOTEC STRATEGIC CORE")
print("===================================")

print("")
print("DATA:")
print(datetime.now())

print("")
print("MISSAO:")
print(CORE_IDENTITY["missao"])

print("")
print("OBJETIVO:")
print(CORE_IDENTITY["objetivo"])

print("")
print("JORNADA DO CLIENTE:")

for etapa in CLIENT_JOURNEY:
    print("-", etapa)

print("")
print("NUCLEO ESTRATEGICO CARREGADO")


