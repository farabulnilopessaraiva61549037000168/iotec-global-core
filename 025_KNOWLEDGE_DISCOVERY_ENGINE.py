"""
======================================================================
IOTEC
KNOWLEDGE DISCOVERY ENGINE

Descobre automaticamente o conhecimento existente
na plataforma.

======================================================================
"""

import os
from pathlib import Path
from collections import Counter

PASTA = r"C:\IOTEC"

PALAVRAS = {

    "KERNEL":"ARQUITETURA",

    "MISSÃƒÆ'O":"ESTRATÃƒâ€°GIA",

    "MISSAO":"ESTRATÃƒâ€°GIA",

    "OBJETIVO":"PLANEJAMENTO",

    "COMERCIAL":"COMERCIAL",

    "CLIENTE":"COMERCIAL",

    "CONTRATO":"JURÃƒÂDICO",

    "JURIDICO":"JURÃƒÂDICO",

    "FINANCEIRO":"FINANCEIRO",

    "RECEITA":"FINANCEIRO",

    "AUDITORIA":"AUDITORIA",

    "DASHBOARD":"DASHBOARD",

    "LOGISTICA":"LOGÃƒÂSTICA",

    "LOGÃƒÂSTICA":"LOGÃƒÂSTICA",

    "AGENTE":"AGENTES",

    "PRODUTO":"PRODUTOS",

    "CATALOGO":"PRODUTOS",

    "CATÃƒÂLOGO":"PRODUTOS",

    "CRM":"CRM",

    "IA":"INTELIGÃƒÅ NCIA",

    "INTELIGENCIA":"INTELIGÃƒÅ NCIA",

    "INTELIGÃƒÅ NCIA":"INTELIGÃƒÅ NCIA"

}


contador = Counter()

print("="*70)
print("IOTEC KNOWLEDGE DISCOVERY ENGINE")
print("="*70)
print()

arquivos = 0

for raiz, _, lista in os.walk(PASTA):

    for nome in lista:

        if not nome.endswith(".py"):
            continue

        arquivos += 1

        caminho = os.path.join(raiz,nome)

        try:

            texto = Path(caminho).read_text(
                encoding="utf-8",
                errors="ignore"
            ).upper()

        except:

            continue

        categorias = set()

        for palavra,categoria in PALAVRAS.items():

            if palavra in texto:

                categorias.add(categoria)

        if not categorias:

            categorias.add("GERAL")

        for c in categorias:

            contador[c]+=1

print("Arquivos analisados :",arquivos)

print()

print("="*70)
print("MAPA DO CONHECIMENTO")
print("="*70)
print()

for categoria,quantidade in contador.most_common():

    print(f"{categoria:<25}{quantidade}")

print()

print("="*70)

print("ÃƒÂREAS MAIS FORTES")

print("="*70)
print()

for categoria,quantidade in contador.most_common(10):

    barras="Ã¢â€"Ë†"*min(quantidade//5+1,40)

    print(f"{categoria:<20} {barras}")

print()

print("="*70)
print("MISSÃƒÆ'O DO KERNEL")
print("="*70)
print()

print("O Kernel deverÃƒÂ¡ agora descobrir:")

print()

print("Ã¢â‚¬Â¢ O que jÃƒÂ¡ existe.")

print("Ã¢â‚¬Â¢ O que pode virar produto.")

print("Ã¢â‚¬Â¢ O que ainda estÃƒÂ¡ incompleto.")

print("Ã¢â‚¬Â¢ O que pode gerar receita.")

print("Ã¢â‚¬Â¢ O que pode ser integrado.")

print()

print("="*70)


