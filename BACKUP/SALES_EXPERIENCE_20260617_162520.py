import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC SALES EXPERIENCE CORE

# ============================================================

# OBJETIVO:

#

# ensinar o nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo a:

#

# 1. entender produtos

# 2. traduzir linguagem tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnica

# 3. criar atmosfera audiovisual

# 4. montar narrativa de venda

# 5. criar imersÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o empresarial

# 6. explicar benefÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­cios

# 7. facilitar aquisiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o

# 8. aumentar conversÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o

# 9. organizar experiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia comercial

# 10. transformar telas em canais vivos

#

# ============================================================



import json

from datetime import datetime



print("")

print("================================================")

print(" IOTEC SALES EXPERIENCE CORE")

print("================================================")

print("")



# ============================================================

# PRODUCT DATABASE

# ============================================================



products = [



    {



        "name":"IOTEC AUTOMATION CORE",



        "technical":"automacao operacional inteligente",



        "human":"automatize tarefas, reduza custos e opere continuamente",



        "impact":"aumenta velocidade operacional e reduz gargalos",



        "audience":"empresas, escritorios, operacoes",



        "videos":[



            "executivos trabalhando",

            "analistas em operacao",

            "ambientes corporativos",

            "dashboards vivos",

            "equipes reunidas"



        ],



        "narrative":[



            "Sua empresa pode operar continuamente.",

            "Automatize processos e aumente produtividade.",

            "Reduza perdas operacionais.",

            "Transforme tarefas em fluxos inteligentes."



        ],



        "acquisition":[



            "assinatura",

            "licenciamento",

            "setup premium",

            "operacao dedicada"



        ]



    },



    {



        "name":"IOTEC MEDIA NETWORK",



        "technical":"ecossistema audiovisual corporativo",



        "human":"transforme sua marca em uma presenca digital viva",



        "impact":"aumenta visibilidade e autoridade empresarial",



        "audience":"midia, empresas, publicidade, marcas",



        "videos":[



            "centros empresariais",

            "urbanismo premium",

            "executivos",

            "streaming corporativo",

            "eventos globais"



        ],



        "narrative":[



            "Sua empresa ganha presenca visual premium.",

            "Transforme telas em canais empresariais vivos.",

            "Crie programacoes corporativas automatizadas.",

            "Conecte sua marca ao mundo."



        ],



        "acquisition":[



            "pacote empresarial",

            "streaming premium",

            "licenciamento",

            "infraestrutura audiovisual"



        ]



    },



    {



        "name":"IOTEC ANALYTICS",



        "technical":"analise operacional inteligente",



        "human":"visualize gargalos e tome decisoes estrategicas",



        "impact":"melhora eficiencia e aumenta controle",



        "audience":"gestores, empresas, command centers",



        "videos":[



            "salas de controle",

            "analistas",

            "graficos",

            "financeiro",

            "painel operacional"



        ],



        "narrative":[



            "Acompanhe indicadores em tempo real.",

            "Descubra gargalos ocultos.",

            "Organize operacoes empresariais.",

            "Tome decisoes com inteligencia."



        ],



        "acquisition":[



            "assinatura",

            "analytics premium",

            "command center",

            "infraestrutura dedicada"



        ]



    }



]



# ============================================================

# SALES ENGINE

# ============================================================



sales_engine = []



print("[BUILD] criando estrutura comercial...")

print("")



for product in products:
    pass



    print("[OK] produto:", product["name"])



    structure = {



        "product":product["name"],



        "technical_language":product["technical"],



        "human_translation":product["human"],



        "financial_impact":product["impact"],



        "target_audience":product["audience"],



        "immersive_environment":{



            "recommended_videos":product["videos"],



            "visual_goal":"empresa viva e operacional",



            "atmosphere":"premium corporativo"



        },



        "sales_narrative":product["narrative"],



        "commercial_flow":{



            "step_1":"mostrar atmosfera",



            "step_2":"explicar produto",



            "step_3":"mostrar beneficio",



            "step_4":"demonstrar funcionamento",



            "step_5":"abrir formulario",



            "step_6":"gerar proposta",



            "step_7":"contrato",



            "step_8":"pagamento",



            "step_9":"implantacao"



        },



        "acquisition_models":product["acquisition"],



        "conversion_strategy":[



            "linguagem humana",

            "imersao audiovisual",

            "presenca corporativa",

            "demonstracao viva",

            "facilidade de aquisicao"



        ],



        "portal_behavior":{



            "videos_rotating":True,



            "human_presence":True,



            "immersive_narration":True,



            "commercial_assistance":True,



            "proposal_generation":True



        }



    }



    sales_engine.append(structure)



# ============================================================

# SAVE

# ============================================================



filename = "IOTEC_SALES_EXPERIENCE_CORE.json"



with open(filename,"w",encoding="utf-8") as f:
    pass



    json.dump(

        sales_engine,

        f,

        indent=4,

        ensure_ascii=False

    )



# ============================================================

# FINAL REPORT

# ============================================================



print("")

print("================================================")

print(" SALES EXPERIENCE REPORT")

print("================================================")

print("")



print("[OK] linguagem humana criada")

print("[OK] narrativa comercial criada")

print("[OK] experiencia audiovisual criada")

print("[OK] atmosfera empresarial criada")

print("[OK] estrategia de conversao criada")

print("[OK] fluxo comercial criado")

print("[OK] comportamento do portal definido")

print("[OK] nucleo instruido")

print("[OK] experiencia comercial organizada")



print("")

print("ARQUIVO:")

print("")

print(filename)



print("")

print("================================================")

print(" IOTEC SALES EXPERIENCE ONLINE")

print("================================================")

print("")





