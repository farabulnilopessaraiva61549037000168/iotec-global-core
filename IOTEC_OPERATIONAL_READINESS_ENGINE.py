import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===========================================================================
IOTEC OPERATIONAL READINESS ENGINE V1.0
===========================================================================

MISSÃƒÆ'O

Descobrir automaticamente:

Ã¢â‚¬Â¢ O que existe
Ã¢â‚¬Â¢ O que funciona
Ã¢â‚¬Â¢ O que estÃƒÂ¡ quebrado
Ã¢â‚¬Â¢ O que impede vendas
Ã¢â‚¬Â¢ O que falta integrar
Ã¢â‚¬Â¢ O prÃƒÂ³ximo passo de maior impacto

Autor: IOTEC
"""

from pathlib import Path
from datetime import datetime
import json

ROOT = Path(r"C:\IOTEC")

# ============================================================
# SETORES OPERACIONAIS
# ============================================================

SETORES = {

    "LANDING_PAGE":[
        "*.html",
        "*landing*",
        "*home*",
        "*index*"
    ],

    "FORMULARIOS":[
        "*form*",
        "*lead*",
        "*register*"
    ],

    "PAGAMENTO":[
        "*payment*",
        "*paypal*",
        "*checkout*",
        "*pix*",
        "*mercadopago*"
    ],

    "EMAIL":[
        "*email*",
        "*smtp*"
    ],

    "WHATSAPP":[
        "*whatsapp*"
    ],

    "API":[
        "*api*",
        "*gateway*"
    ],

    "BANCO":[
        "*database*",
        "*sqlite*",
        "*postgres*"
    ],

    "PRODUTOS":[
        "*product*",
        "*catalog*",
        "*service*"
    ]

}

# ============================================================
# SCANNER
# ============================================================

resultado = {}

print("="*70)
print(" IOTEC OPERATIONAL READINESS ENGINE")
print("="*70)

print()
print("Iniciando auditoria operacional...")
print()

for setor, filtros in SETORES.items():

    encontrados = []

    for filtro in filtros:

        encontrados.extend(ROOT.rglob(filtro))

    encontrados = list(set(encontrados))

    resultado[setor] = {

        "quantidade": len(encontrados),

        "arquivos": [str(x) for x in encontrados[:20]]

    }

# ============================================================
# EXIBIÃƒâ€¡ÃƒÆ'O
# ============================================================

for setor in resultado:

    print("-"*60)
    print(setor)

    print("Arquivos:", resultado[setor]["quantidade"])

    for arq in resultado[setor]["arquivos"]:

        print(arq)

# ============================================================
# DIAGNÃƒâ€œSTICO
# ============================================================

print()
print("="*70)
print("DIAGNÃƒâ€œSTICO EXECUTIVO")
print("="*70)

diagnostico=[]

if resultado["LANDING_PAGE"]["quantidade"]==0:
    diagnostico.append("Landing Page inexistente.")

if resultado["FORMULARIOS"]["quantidade"]==0:
    diagnostico.append("Nenhum formulÃƒÂ¡rio encontrado.")

if resultado["PAGAMENTO"]["quantidade"]==0:
    diagnostico.append("Sistema de pagamento inexistente.")

if resultado["EMAIL"]["quantidade"]==0:
    diagnostico.append("Email operacional inexistente.")

if resultado["API"]["quantidade"]==0:
    diagnostico.append("API principal nÃƒÂ£o localizada.")

if resultado["PRODUTOS"]["quantidade"]==0:
    diagnostico.append("Nenhum produto localizado.")

if len(diagnostico)==0:

    print("Arquitetura mÃƒÂ­nima localizada.")

else:

    for d in diagnostico:

        print("Ã¢â‚¬Â¢",d)

# ============================================================
# PRONTIDÃƒÆ'O
# ============================================================

total = len(SETORES)

ativos = 0

for setor in resultado:

    if resultado[setor]["quantidade"]>0:

        ativos += 1

indice = round((ativos/total)*100,2)

print()
print("="*70)
print("PRONTIDÃƒÆ'O OPERACIONAL")
print("="*70)

print(indice,"%")

# ============================================================
# SALVAR
# ============================================================

relatorio={

    "data":str(datetime.now()),

    "indice":indice,

    "setores":resultado,

    "diagnostico":diagnostico

}

with open(
    "IOTEC_OPERATIONAL_READINESS_REPORT.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("RelatÃƒÂ³rio salvo.")

print("IOTEC_OPERATIONAL_READINESS_REPORT.json")

print()

print("="*70)
print("PRÃƒâ€œXIMA ETAPA")
print("="*70)

print("""
Na V2 este motor deixarÃƒÂ¡ de apenas contar arquivos.

Ele descobrirÃƒÂ¡:

Ã¢Å"â€ qual landing estÃƒÂ¡ publicada

Ã¢Å"â€ qual formulÃƒÂ¡rio realmente funciona

Ã¢Å"â€ qual API responde

Ã¢Å"â€ qual botÃƒÂ£o Comprar estÃƒÂ¡ ativo

Ã¢Å"â€ qual PayPal responde

Ã¢Å"â€ qual Webhook estÃƒÂ¡ ativo

Ã¢Å"â€ qual produto realmente pode ser vendido

Ã¢Å"â€ onde exatamente o fluxo comercial estÃƒÂ¡ interrompido

Ã¢Å"â€ qual integraÃƒÂ§ÃƒÂ£o destrava a prÃƒÂ³xima venda

""")



