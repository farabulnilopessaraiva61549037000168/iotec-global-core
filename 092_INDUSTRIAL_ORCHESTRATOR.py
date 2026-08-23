# ==========================================================
# 092_INDUSTRIAL_ORCHESTRATOR.py
# IOTEC INDUSTRIAL ORCHESTRATOR
# ==========================================================

from datetime import datetime

print("="*80)
print("IOTEC INDUSTRIAL ORCHESTRATOR")
print("="*80)
print()

print("Inicializando Complexo Industrial...")
print()

LINHAS = [

("Knowledge Factory",
 "CÃƒÂ³digo Python",
 "Livros TÃƒÂ©cnicos",
 "ONLINE"),

("HTML Factory",
 "Componentes HTML",
 "Portais",
 "ONLINE"),

("API Factory",
 "IntegraÃƒÂ§ÃƒÂµes",
 "APIs",
 "EM IMPLANTAÃƒâ€¡ÃƒÆ'O"),

("Discovery Factory",
 "Empresas",
 "Leads",
 "ONLINE"),

("Commercial Factory",
 "Capacidades",
 "Produtos",
 "ONLINE"),

("Campaign Factory",
 "Produtos",
 "Campanhas",
 "ONLINE"),

("Documentation Factory",
 "CÃƒÂ³digo",
 "DocumentaÃƒÂ§ÃƒÂ£o",
 "ONLINE"),

("Quality Factory",
 "Produtos",
 "ValidaÃƒÂ§ÃƒÂ£o",
 "ONLINE"),

("Deployment Factory",
 "Produtos",
 "Render / Netlify",
 "ONLINE"),

("Revenue Factory",
 "Clientes",
 "Receita",
 "AGUARDANDO")

]

print("="*80)
print("LINHAS DE PRODUÃƒâ€¡ÃƒÆ'O")
print("="*80)
print()

online = 0

for nome,entrada,saida,status in LINHAS:

    if status == "ONLINE":
        icone = "Ã°Å¸Å¸Â¢"
        online += 1
    elif status == "EM IMPLANTAÃƒâ€¡ÃƒÆ'O":
        icone = "Ã°Å¸Å¸Â¡"
    else:
        icone = "Ã°Å¸â€Â´"

    print(f"{icone} {nome}")
    print(f"    Entrada : {entrada}")
    print(f"    Produto : {saida}")
    print(f"    Status  : {status}")
    print()

print("="*80)
print("ESTEIRA INDUSTRIAL")
print("="*80)
print()

fluxo = [

"MatÃƒÂ©ria-Prima",

"Triagem",

"PreparaÃƒÂ§ÃƒÂ£o",

"Linhas de ProduÃƒÂ§ÃƒÂ£o",

"Montagem",

"InspeÃƒÂ§ÃƒÂ£o",

"Controle de Qualidade",

"ImplantaÃƒÂ§ÃƒÂ£o",

"Cliente",

"Receita"

]

for etapa in fluxo:
    print("Ã¢â€ â€œ")
    print(etapa)

print()

print("="*80)
print("MÃƒÂQUINAS INDUSTRIAIS")
print("="*80)
print()

maquinas = [

"Kernel",

"Executive Skin",

"Discovery Center",

"Campaign Center",

"Experience Warehouse",

"Visual Genome",

"Official Assets",

"Infrastructure",

"PayPal",

"Render",

"Netlify"

]

for maq in maquinas:
    print("Ã¢Å¡â„¢", maq)

print()

print("="*80)
print("MATÃƒâ€°RIA-PRIMA")
print("="*80)
print()

materia = [

"CÃƒÂ³digos Python",

"Interfaces HTML",

"JavaScript",

"CSS",

"JSON",

"APIs",

"Empresas",

"Clientes",

"Conhecimento",

"ExperiÃƒÂªncia"

]

for item in materia:
    print("Ã¢â‚¬Â¢", item)

print()

print("="*80)
print("CHEFE DE GABINETE")
print("="*80)
print()

print("Bom dia, Presidente.")
print()

print("Todas as linhas industriais")
print("estÃƒÂ£o sincronizadas.")
print()

print("Cada equipe trabalha")
print("somente na sua")
print("linha de produÃƒÂ§ÃƒÂ£o.")
print()

print("Nenhum setor interfere")
print("diretamente em outro.")
print()

print("="*80)
print("OBJETIVO")
print("="*80)
print()

print("Transformar conhecimento")
print("em produtos digitais.")
print()

print("Transformar produtos")
print("em receita.")
print()

print("="*80)
print("STATUS")
print("="*80)
print()

print(f"Linhas Online............... {online}")
print(f"Linhas Totais............... {len(LINHAS)}")
print(f"Data........................ {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print()

print("COMPLEXO INDUSTRIAL OPERACIONAL.")


