import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 NODE ENGINE
# ============================================================
#
# IOTEC ECOSYSTEM
#
# X27
# Agentes Operacionais DistribuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dos
#
# ============================================================

from datetime import datetime

# ============================================================
# NODES
# ============================================================

NODES = {

    "NODE_LOGISTICA": {

        "descricao":
            "Transporte e Suprimentos",

        "tarefas": [

            "Verificar rotas",

            "Verificar veÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­culos",

            "Verificar combustÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel",

            "Verificar centros de distribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

            "Verificar pontos de entrega"

        ]
    },

    "NODE_AGUA": {

        "descricao":
            "Recursos HÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dricos",

        "tarefas": [

            "Verificar reservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios",

            "Verificar caminhÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes-pipa",

            "Verificar estaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes de tratamento",

            "Verificar distribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

            "Verificar comunidades isoladas"

        ]
    },

    "NODE_ENERGIA": {

        "descricao":
            "Energia",

        "tarefas": [

            "Verificar rede elÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©trica",

            "Verificar geradores",

            "Verificar subestaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",

            "Verificar hospitais",

            "Verificar infraestrutura crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica"

        ]
    },

    "NODE_SAUDE": {

        "descricao":
            "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde",

        "tarefas": [

            "Verificar hospitais",

            "Verificar leitos",

            "Verificar ambulÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncias",

            "Verificar medicamentos",

            "Verificar equipes mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dicas"

        ]
    },

    "NODE_ASSISTENCIA": {

        "descricao":
            "AssistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Social",

        "tarefas": [

            "Identificar famÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias",

            "Verificar benefÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cios",

            "Verificar vulnerabilidades",

            "Mapear necessidades",

            "Acionar equipes"

        ]
    },

    "NODE_ABRIGOS": {

        "descricao":
            "Abrigos",

        "tarefas": [

            "Verificar capacidade",

            "Verificar ocupaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

            "Verificar colchÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",

            "Verificar cobertores",

            "Verificar alimentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"

        ]
    },

    "NODE_INFRA": {

        "descricao":
            "Infraestrutura",

        "tarefas": [

            "Verificar pontes",

            "Verificar estradas",

            "Verificar barragens",

            "Verificar prÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dios pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblicos",

            "Verificar acessos"

        ]
    },

    "NODE_COMUNICACAO": {

        "descricao":
            "ComunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

        "tarefas": [

            "Verificar internet",

            "Verificar telefonia",

            "Verificar rÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡dios",

            "Verificar alertas",

            "Verificar comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºblica"

        ]
    }

}

# ============================================================
# EVENTOS
# ============================================================

EVENTOS = {

    "SECA": [
        "NODE_AGUA",
        "NODE_ASSISTENCIA",
        "NODE_LOGISTICA"
    ],

    "ENCHENTE": [
        "NODE_AGUA",
        "NODE_SAUDE",
        "NODE_ABRIGOS",
        "NODE_LOGISTICA"
    ],

    "ROMPIMENTO_BARRAGEM": [
        "NODE_AGUA",
        "NODE_LOGISTICA",
        "NODE_SAUDE",
        "NODE_INFRA",
        "NODE_ABRIGOS",
        "NODE_COMUNICACAO"
    ],

    "INCENDIO_FLORESTAL": [
        "NODE_LOGISTICA",
        "NODE_SAUDE",
        "NODE_COMUNICACAO"
    ],

    "TERREMOTO": [
        "NODE_INFRA",
        "NODE_SAUDE",
        "NODE_ABRIGOS",
        "NODE_LOGISTICA"
    ]
}

# ============================================================
# EXECUTAR NÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ
# ============================================================

def executar_node(nome):
    pass

    node = NODES[nome]

    print("\n------------------------------------------------")

    print(nome)

    print(f"FUNCAO: {node['descricao']}")

    print("------------------------------------------------")

    for tarefa in node["tarefas"]:
        pass

        print(f"[EXECUTANDO] {tarefa}")

# ============================================================
# ATIVAR EVENTO
# ============================================================

def ativar_evento(evento):
    pass

    print("\n================================================")

    print("X27 NODE ENGINE")

    print("================================================")

    print(f"EVENTO : {evento}")

    print(f"DATA   : {datetime.now()}")

    print("================================================")

    if evento not in EVENTOS:
        pass

        print("[ERRO] Evento desconhecido")

        return

    nodes_necessarios = EVENTOS[evento]

    print("\nNODES MOBILIZADOS:\n")

    for node in nodes_necessarios:
        pass

        executar_node(node)

    print("\n================================================")

    print("OPERACAO X27 CONCLUIDA")

    print("================================================")

# ============================================================
# TESTE
# ============================================================

if __name__ == "__main__":
    pass

    ativar_evento("ROMPIMENTO_BARRAGEM")


