import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===========================================================================
 IOTEC PRODUCT CURATOR AI V1.0
===========================================================================

MissÃƒÂ£o

Transformar capacidades tÃƒÂ©cnicas existentes em produtos vendÃƒÂ¡veis.

O agente NÃƒÆ'O programa novos mÃƒÂ³dulos.

Ele:

Ã¢â‚¬Â¢ descobre capacidades
Ã¢â‚¬Â¢ organiza produtos
Ã¢â‚¬Â¢ avalia qualidade
Ã¢â‚¬Â¢ prepara publicaÃƒÂ§ÃƒÂ£o
Ã¢â‚¬Â¢ solicita integraÃƒÂ§ÃƒÂµes faltantes
Ã¢â‚¬Â¢ aprova ou bloqueia publicaÃƒÂ§ÃƒÂ£o

Autor:
IOTEC
"""

from pathlib import Path
import json
import re

ROOT = Path(r"C:\IOTEC")

KEYWORDS = {

    "AUDITORIA":[
        "audit",
        "auditoria",
        "inspection"
    ],

    "IA":[
        "ai",
        "intelligence",
        "reasoning"
    ],

    "PAGAMENTO":[
        "paypal",
        "payment",
        "checkout",
        "mercadopago",
        "stripe",
        "pix"
    ],

    "FORMULARIOS":[
        "form",
        "lead",
        "register"
    ],

    "EMAIL":[
        "email",
        "smtp"
    ],

    "WHATSAPP":[
        "whatsapp"
    ],

    "API":[
        "api",
        "gateway"
    ],

    "BANCO":[
        "database",
        "sqlite",
        "postgres"
    ]

}

CATALOGO = {}

print("="*70)
print(" IOTEC PRODUCT CURATOR AI")
print("="*70)

for categoria in KEYWORDS:

    CATALOGO[categoria]=[]

for arquivo in ROOT.rglob("*"):

    if not arquivo.is_file():
        continue

    nome = arquivo.name.lower()

    for categoria, palavras in KEYWORDS.items():

        for palavra in palavras:

            if palavra in nome:

                CATALOGO[categoria].append(str(arquivo))
                break

print()

print("CAPACIDADES ENCONTRADAS\n")

for categoria in CATALOGO:

    print("-"*60)
    print(categoria)

    print("Quantidade:",
          len(CATALOGO[categoria]))

    for arq in CATALOGO[categoria][:10]:

        print(arq)

print()

print("="*70)
print("ANÃƒÂLISE COMERCIAL")
print("="*70)

produtos=[]

if len(CATALOGO["AUDITORIA"])>0:

    produtos.append({

        "produto":"Consultoria em Auditoria de Dados",

        "status":"PRONTO PARA CURADORIA"

    })

if len(CATALOGO["IA"])>0:

    produtos.append({

        "produto":"Assistente Executivo com IA",

        "status":"PRONTO PARA CURADORIA"

    })

if len(CATALOGO["PAGAMENTO"])>0:

    produtos.append({

        "produto":"Sistema de Pagamentos",

        "status":"VALIDAR CHECKOUT"

    })

if len(CATALOGO["FORMULARIOS"])>0:

    produtos.append({

        "produto":"Portal Comercial",

        "status":"VALIDAR FLUXO"

    })

for produto in produtos:

    print()

    print("Produto:",produto["produto"])
    print("Status :",produto["status"])

print()

print("="*70)
print("CHECKLIST PREMIUM")
print("="*70)

checklist=[

"DescriÃƒÂ§ÃƒÂ£o",

"PÃƒÂ¡gina",

"VÃƒÂ­deo",

"BotÃƒÂ£o Comprar",

"Pagamento",

"Entrega",

"E-mail",

"WhatsApp",

"API",

"Teste Final"

]

for item in checklist:

    print("[ ]",item)

print()

print("="*70)
print("PRÃƒâ€œXIMA MISSÃƒÆ'O")
print("="*70)

print("""
O prÃƒÂ³ximo agente deverÃƒÂ¡:

1. Escolher um produto.

2. Reunir automaticamente
todos os mÃƒÂ³dulos relacionados.

3. Criar uma landing page.

4. Criar descriÃƒÂ§ÃƒÂ£o comercial.

5. Validar checkout.

6. Validar entrega.

7. Publicar.

8. Monitorar vendas.

""")

with open(
    "IOTEC_PRODUCT_CATALOG.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        CATALOGO,
        f,
        indent=4,
        ensure_ascii=False
    )

print()

print("CatÃƒÂ¡logo salvo em:")
print("IOTEC_PRODUCT_CATALOG.json")



