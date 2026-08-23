import json
from datetime import datetime

OUTPUT_FILE = "IOTEC_PRODUCT_MARKET_MATRIX.json"

# ==========================================================
# PRODUTOS DA IOTEC
# ==========================================================

products = [

    {
        "name":"Dashboard Executivo",
        "category":"Business Intelligence"
    },

    {
        "name":"Portal Corporativo",
        "category":"Web"
    },

    {
        "name":"Business Intelligence",
        "category":"Analytics"
    },

    {
        "name":"DiagnÃƒÂ³stico Digital",
        "category":"Consultoria"
    },

    {
        "name":"Auditoria TecnolÃƒÂ³gica",
        "category":"Auditoria"
    },

    {
        "name":"Monitoramento EstratÃƒÂ©gico",
        "category":"InteligÃƒÂªncia"
    }

]

# ==========================================================
# MERCADOS
# ==========================================================

markets = {

    "ConstruÃƒÂ§ÃƒÂ£o":[
        "Dashboard Executivo",
        "Business Intelligence",
        "Portal Corporativo",
        "DiagnÃƒÂ³stico Digital"
    ],

    "EducaÃƒÂ§ÃƒÂ£o":[
        "Portal Corporativo",
        "Dashboard Executivo",
        "Business Intelligence"
    ],

    "SaÃƒÂºde":[
        "Dashboard Executivo",
        "Monitoramento EstratÃƒÂ©gico",
        "Business Intelligence"
    ],

    "IndÃƒÂºstria":[
        "Business Intelligence",
        "Dashboard Executivo",
        "Auditoria TecnolÃƒÂ³gica",
        "Monitoramento EstratÃƒÂ©gico"
    ],

    "Technology":[
        "Auditoria TecnolÃƒÂ³gica",
        "Business Intelligence",
        "Portal Corporativo"
    ],

    "Healthcare":[
        "Business Intelligence",
        "Monitoramento EstratÃƒÂ©gico"
    ],

    "Tecnologia":[
        "Portal Corporativo",
        "Business Intelligence",
        "Auditoria TecnolÃƒÂ³gica"
    ]

}

# ==========================================================

matrix = []

for market, compatibles in markets.items():

    for product in products:

        compatibility = 95 if product["name"] in compatibles else 35

        priority = "ALTA" if compatibility >= 90 else "MÃƒâ€°DIA"

        matrix.append({

            "market": market,

            "product": product["name"],

            "category": product["category"],

            "compatibility": compatibility,

            "priority": priority,

            "status": "AVAILABLE"

        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        matrix,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 90)
print("IOTEC PRODUCT MARKET MATCH ENGINE")
print("=" * 90)
print()

print("Produtos :", len(products))
print("Mercados :", len(markets))
print("CombinaÃƒÂ§ÃƒÂµes :", len(matrix))
print()

print("=" * 90)
print("MERCADOS E PRODUTOS")
print("=" * 90)
print()

for market, compatibles in markets.items():

    print(market)

    for p in compatibles:

        print("   >", p)

    print()

print("=" * 90)
print("MISSÃƒÆ'O")
print("=" * 90)
print()

print("Cada mercado")
print("passa a possuir")
print("produtos")
print("priorizados.")
print()

print("Cada produto")
print("passa a conhecer")
print("os mercados")
print("mais compatÃƒÂ­veis.")
print()

print("=" * 90)
print("CHEFE DE GABINETE")
print("=" * 90)
print()

print("Boa noite, Presidente.")
print()

print("O Kernel")
print("comeÃƒÂ§a a")
print("relacionar")
print("automaticamente")
print("mercados")
print("e produtos.")

print()

print("O prÃƒÂ³ximo passo")
print("serÃƒÂ¡ localizar")
print("empresas")
print("dentro de cada")
print("mercado e")
print("calcular")
print("a oportunidade")
print("comercial.")

print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("Matriz Gerada :", len(matrix))
print("Data :", datetime.now())

print()

print("PRODUCT MARKET MATCH OPERACIONAL.")

