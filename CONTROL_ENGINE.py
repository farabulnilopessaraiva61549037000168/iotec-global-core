import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==========================================================
IOTEC
NEGOTIATION CONTROL ENGINE
NÃƒÅ¡CLEO DE CONTROLE DE NEGOCIAÃƒâ€¡Ãƒâ€¢ES
==========================================================
"""

NEGOTIATION_ENGINE = {

    "MISSAO":
        "Acompanhar negociaÃƒÂ§ÃƒÂµes comerciais, aumentar a qualidade "
        "do atendimento e transformar oportunidades em contratos.",

    "OBJETIVOS":[

        "Organizar negociaÃƒÂ§ÃƒÂµes.",

        "Nunca perder um cliente por falta de acompanhamento.",

        "Registrar todas as etapas.",

        "Sugerir prÃƒÂ³ximos passos.",

        "Melhorar continuamente a estratÃƒÂ©gia comercial.",

        "Gerar receita recorrente."

    ],

    "PAINEL":[

        "Cliente",

        "Empresa",

        "Contato principal",

        "Segmento",

        "Valor estimado",

        "Etapa da negociaÃƒÂ§ÃƒÂ£o",

        "Documentos compartilhados",

        "Proposta enviada",

        "ObjeÃƒÂ§ÃƒÂµes registradas",

        "PendÃƒÂªncias",

        "PrÃƒÂ³xima aÃƒÂ§ÃƒÂ£o",

        "ResponsÃƒÂ¡vel",

        "Data prevista",

        "Status",

        "Probabilidade de fechamento"

    ],

    "ETAPAS":[

        "Lead identificado",

        "Primeiro contato",

        "DiagnÃƒÂ³stico",

        "ApresentaÃƒÂ§ÃƒÂ£o da soluÃƒÂ§ÃƒÂ£o",

        "Proposta comercial",

        "NegociaÃƒÂ§ÃƒÂ£o",

        "RevisÃƒÂ£o contratual",

        "AprovaÃƒÂ§ÃƒÂ£o",

        "Contrato fechado",

        "ImplantaÃƒÂ§ÃƒÂ£o",

        "PÃƒÂ³s-venda"

    ],

    "REGRAS":[

        "Toda negociaÃƒÂ§ÃƒÂ£o deve possuir histÃƒÂ³rico.",

        "Toda proposta deve possuir acompanhamento.",

        "Toda objeÃƒÂ§ÃƒÂ£o deve ser registrada.",

        "Toda resposta deve agregar valor ao cliente.",

        "Nunca prometer o que a empresa nÃƒÂ£o pode entregar.",

        "Sempre agir com ÃƒÂ©tica, transparÃƒÂªncia e profissionalismo.",

        "ApÃƒÂ³s cada interaÃƒÂ§ÃƒÂ£o, definir automaticamente o prÃƒÂ³ximo passo."

    ],

    "PERGUNTAS_DO_KERNEL":[

        "Qual problema do cliente estamos resolvendo?",

        "O cliente compreendeu a proposta?",

        "Existe alguma dÃƒÂºvida pendente?",

        "Existe alguma adaptaÃƒÂ§ÃƒÂ£o que aumente o valor entregue?",

        "Qual ÃƒÂ© a prÃƒÂ³xima aÃƒÂ§ÃƒÂ£o para avanÃƒÂ§ar a negociaÃƒÂ§ÃƒÂ£o?"

    ],

    "OBJETIVO_FINAL":

        "Conduzir negociaÃƒÂ§ÃƒÂµes organizadas, gerar confianÃƒÂ§a, "
        "fortalecer relacionamentos e aumentar a taxa de contratos "
        "fechados de forma sustentÃƒÂ¡vel."
}

print("NEGOTIATION CONTROL ENGINE CARREGADO.")



