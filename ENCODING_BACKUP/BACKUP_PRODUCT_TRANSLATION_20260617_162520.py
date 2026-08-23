import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC PRODUCT TRANSLATION ENGINE
# ============================================================
# OBJETIVO:
# ensinar o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo a:
#
# 1. entender o que o produto faz
# 2. traduzir linguagem tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnica
# 3. converter em linguagem humana
# 4. criar narrativa de venda
# 5. explicar benefÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cios reais
# 6. gerar percepÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor
# 7. auxiliar conversÃƒÆ'Ã†â€™o comercial
#
# ============================================================

import json
import random

print("")
print("================================================")
print(" IOTEC PRODUCT TRANSLATION ENGINE")
print("================================================")
print("")

# ============================================================
# PRODUTOS TECNICOS
# ============================================================

products = [

    {
        "name":"IOTEC SATELLITE TRACKING",
        "technical":"rastreamento multimodal de cargas",
        "human":"acompanhe cargas importantes em tempo real e reduza riscos operacionais",
        "benefits":[
            "mais seguranÃƒÆ'Ã†â€™a",
            "menos perdas",
            "monitoramento continuo",
            "controle operacional"
        ],
        "sector":"logistica"
    },

    {
        "name":"IOTEC ANALYTICS",
        "technical":"analise automatizada de dados empresariais",
        "human":"o sistema organiza dados e ajuda sua empresa a tomar decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes mais inteligentes",
        "benefits":[
            "mais organizacao",
            "menos desperdicio",
            "visao operacional",
            "mais produtividade"
        ],
        "sector":"empresarial"
    },

    {
        "name":"IOTEC MEDIA NETWORK",
        "technical":"streaming corporativo inteligente",
        "human":"transforme sua empresa em um ambiente moderno com programacao audiovisual premium",
        "benefits":[
            "presenca premium",
            "ambiente sofisticado",
            "comunicacao visual forte",
            "engajamento"
        ],
        "sector":"midia"
    },

    {
        "name":"IOTEC AUTOMATION CORE",
        "technical":"automacao empresarial integrada",
        "human":"o sistema automatiza tarefas repetitivas e reduz tempo operacional",
        "benefits":[
            "economia de tempo",
            "menos trabalho manual",
            "mais velocidade",
            "mais eficiencia"
        ],
        "sector":"automacao"
    },

    {
        "name":"IOTEC LEGAL OPS",
        "technical":"gestao juridica automatizada",
        "human":"organize documentos juridicos e acompanhe processos de forma inteligente",
        "benefits":[
            "organizacao juridica",
            "menos falhas",
            "mais controle",
            "mais produtividade"
        ],
        "sector":"juridico"
    }

]

# ============================================================
# FRASES DE VENDA
# ============================================================

openers = [

    "Sua empresa pode operar com mais inteligencia.",
    "Transforme sua operacao em uma estrutura moderna.",
    "Automatize processos e aumente eficiencia.",
    "Ganhe presenca digital premium.",
    "Centralize sua operacao em um unico ambiente."
]

closers = [

    "Tudo funcionando em uma estrutura organizada e inteligente.",
    "Tecnologia pensada para empresas modernas.",
    "Uma operacao preparada para escala e crescimento.",
    "Infraestrutura digital pronta para uso.",
    "Mais organizacao, mais eficiencia e mais resultado."
]

# ============================================================
# GERADOR DE APRESENTACAO
# ============================================================

def generate_sales_text(product):
    pass

    opener = random.choice(openers)
    closer = random.choice(closers)

    text = f"""

================================================
PRODUTO
================================================

{product['name']}

================================================
O QUE ISSO FAZ
================================================

{product['human']}

================================================
BENEFICIOS
================================================

"""

    for b in product["benefits"]:
        text += f"- {b}\n"

    text += f"""

================================================
LINGUAGEM TECNICA
================================================

{product['technical']}

================================================
EXPLICACAO SIMPLIFICADA
================================================

{opener}

{product['human']}.

{closer}

================================================
SETOR
================================================

{product['sector']}

"""

    return text

# ============================================================
# GERACAO
# ============================================================

print("[BUILD] criando linguagem de venda...")
print("")

all_products = []

for p in products:
    pass

    sales_text = generate_sales_text(p)

    print(f"[OK] produto traduzido: {p['name']}")

    all_products.append({

        "product":p["name"],
        "sales_text":sales_text

    })

# ============================================================
# EXPORT
# ============================================================

with open("IOTEC_SALES_LANGUAGE.json","w",encoding="utf-8") as f:
    pass

    json.dump(all_products,f,indent=4,ensure_ascii=False)

print("")
print("================================================")
print(" SALES LANGUAGE ENGINE COMPLETE")
print("================================================")
print("")
print("[OK] linguagem humana criada")
print("[OK] narrativa comercial criada")
print("[OK] beneficios organizados")
print("[OK] traducao tecnica criada")
print("[OK] explicacao simplificada criada")
print("")
print("ARQUIVO:")
print("")
print("IOTEC_SALES_LANGUAGE.json")
print("")



