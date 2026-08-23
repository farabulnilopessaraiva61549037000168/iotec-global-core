# ==============================================================
# 096_RESOURCE_ORCHESTRATOR.py
# IOTEC RESOURCE ORCHESTRATOR
# ==============================================================

from datetime import datetime

print("="*90)
print("IOTEC RESOURCE ORCHESTRATOR")
print("ORQUESTRADOR INDUSTRIAL DE RECURSOS")
print("="*90)
print()

print("Inicializando Sistema Nervoso Industrial...")
print()

# ==============================================================
# FÃƒÂBRICAS
# ==============================================================

fabricas = [

("Knowledge Factory",95,148,137,18),

("HTML Factory",100,126,126,0),

("API Factory",48,41,19,22),

("Commercial Factory",74,63,51,12),

("Campaign Factory",69,44,31,13),

("Quality Factory",82,29,24,5),

("Deployment Factory",63,18,11,7),

("Revenue Factory",22,17,4,13)

]

print("="*90)
print("FÃƒÂBRICAS")
print("="*90)
print()

for nome,cap,operarios,ativos,fila in fabricas:

    barra="Ã¢â€"Ë†"*int(cap/5)+"Ã¢â€"â€˜"*(20-int(cap/5))

    print(nome)
    print("Capacidade :",barra,cap,"%")
    print("OperÃƒÂ¡rios..",operarios)
    print("Produzindo.",ativos)
    print("Fila.......",fila)
    print()

# ==============================================================
# ESTOQUE
# ==============================================================

print("="*90)
print("ESTOQUE INDUSTRIAL")
print("="*90)
print()

estoque=[

("Python",1177),

("HTML",42250),

("JavaScript",8453),

("CSS",567),

("JSON",312),

("Produtos",61),

("APIs",38),

("Campanhas",19),

("Ecossistemas",12)

]

for nome,total in estoque:

    print(nome.ljust(20),total)

print()

# ==============================================================
# ALMOXARIFADO
# ==============================================================

print("="*90)
print("ALMOXARIFADO")
print("="*90)
print()

componentes=[

"Templates HTML",

"Componentes CSS",

"JavaScript",

"Bootstrap",

"ÃƒÂcones",

"Logotipos",

"VÃƒÂ­deos",

"Planos de Fundo",

"AnimaÃƒÂ§ÃƒÂµes",

"Biblioteca Visual"

]

for c in componentes:

    print("Ã¢Å"â€œ",c)

print()

# ==============================================================
# FERRAMENTARIA
# ==============================================================

print("="*90)
print("FERRAMENTARIA")
print("="*90)
print()

ferramentas=[

"Python",

"PowerShell",

"Flask",

"FastAPI",

"Render",

"Netlify",

"GitHub",

"PayPal",

"Proton Mail",

"OpenAI",

"Google Maps",

"LinkedIn",

"WhatsApp Business"

]

for f in ferramentas:

    print("Ã¢Å¡â„¢",f)

print()

# ==============================================================
# ORDENS
# ==============================================================

print("="*90)
print("DISTRIBUIÃƒâ€¡ÃƒÆ'O DE ORDENS")
print("="*90)
print()

ops=[

("OP-001","Executive Skin",
["Knowledge","HTML","Deployment"]),

("OP-002","Google Maps",
["API","Infrastructure"]),

("OP-003","Portal Comercial",
["HTML","Commercial","Campaign"]),

("OP-004","Knowledge Library",
["Knowledge","Documentation"])

]

for numero,produto,setores in ops:

    print(numero)

    print("Produto :",produto)

    print("Fluxo :")

    for s in setores:

        print("   Ã¢â€ â€œ",s)

    print()

# ==============================================================
# SUPERVISORES
# ==============================================================

print("="*90)
print("SUPERVISORES INDUSTRIAIS")
print("="*90)
print()

supervisores=[

("Knowledge","NORMAL"),

("HTML","NORMAL"),

("API","GARGALO"),

("Commercial","NORMAL"),

("Campaign","NORMAL"),

("Deployment","NORMAL"),

("Revenue","SEM CLIENTES")

]

for nome,status in supervisores:

    if status=="NORMAL":

        cor="Ã°Å¸Å¸Â¢"

    elif status=="GARGALO":

        cor="Ã°Å¸Å¸Â¡"

    else:

        cor="Ã°Å¸â€Â´"

    print(cor,nome.ljust(15),status)

print()

# ==============================================================
# CHEFE DE GABINETE
# ==============================================================

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("O Sistema Nervoso Industrial")
print("assumiu a distribuiÃƒÂ§ÃƒÂ£o")
print("automÃƒÂ¡tica dos recursos.")
print()

print("Cada ordem de produÃƒÂ§ÃƒÂ£o")
print("ÃƒÂ© encaminhada")
print("automaticamente")
print("ÃƒÂ s fÃƒÂ¡bricas competentes.")
print()

print("Os supervisores")
print("acompanham continuamente")
print("gargalos, filas")
print("e capacidade operacional.")
print()

print("As linhas trabalham")
print("em paralelo")
print("mantendo a estabilidade")
print("da plataforma.")
print()

# ==============================================================
# MISSÃƒÆ'O
# ==============================================================

print()
print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print("Nenhum recurso")
print("permanece sem destino.")
print()

print("Nenhuma fÃƒÂ¡brica")
print("permanece isolada.")
print()

print("Todo conhecimento")
print("deve alimentar")
print("a produÃƒÂ§ÃƒÂ£o.")
print()

print("Toda produÃƒÂ§ÃƒÂ£o")
print("deve gerar")
print("capacidades.")
print()

print("Toda capacidade")
print("deve poder")
print("gerar receita.")
print()

# ==============================================================
# STATUS
# ==============================================================

print()
print("="*90)
print("STATUS")
print("="*90)
print()

print("FÃƒÂ¡bricas................",len(fabricas))
print("Ordens..................",len(ops))
print("Supervisores............",len(supervisores))
print("Ferramentas.............",len(ferramentas))
print("Data....................",datetime.now().strftime("%d/%m/%Y %H:%M"))
print()

print("RESOURCE ORCHESTRATOR OPERACIONAL.")


