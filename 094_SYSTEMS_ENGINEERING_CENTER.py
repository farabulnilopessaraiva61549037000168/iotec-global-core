# ==========================================================
# 094_SYSTEMS_ENGINEERING_CENTER.py
# IOTEC SYSTEMS ENGINEERING CENTER
# ==========================================================

from datetime import datetime

print("=" * 80)
print("IOTEC SYSTEMS ENGINEERING CENTER")
print("=" * 80)
print()

print("Inicializando Engenharia de Sistemas...")
print()

CENTROS = [

("Arquitetura Corporativa",
 "Define a arquitetura global da IOTEC.",
 "ONLINE"),

("CoordenaÃƒÂ§ÃƒÂ£o Industrial",
 "Coordena todas as fÃƒÂ¡bricas digitais.",
 "ONLINE"),

("IntegraÃƒÂ§ÃƒÂ£o de Sistemas",
 "Integra departamentos e ecossistemas.",
 "ONLINE"),

("Engenharia de ProduÃƒÂ§ÃƒÂ£o",
 "Projeta linhas de produÃƒÂ§ÃƒÂ£o.",
 "ONLINE"),

("Engenharia do Conhecimento",
 "Transforma cÃƒÂ³digo em conhecimento.",
 "ONLINE"),

("Engenharia Comercial",
 "Transforma capacidades em produtos.",
 "ONLINE"),

("Engenharia de Infraestrutura",
 "Coordena Render, Netlify e servidores.",
 "ONLINE"),

("Engenharia de Qualidade",
 "Valida produtos antes da entrega.",
 "ONLINE"),

("LaboratÃƒÂ³rio de InovaÃƒÂ§ÃƒÂ£o",
 "Pesquisa novas tecnologias.",
 "ONLINE"),

("Controle de Sistemas",
 "Monitora continuamente toda a empresa.",
 "ONLINE")

]

print("="*80)
print("CENTROS DE ENGENHARIA")
print("="*80)
print()

ativos = 0

for nome,missao,status in CENTROS:

    if status == "ONLINE":
        ativos += 1
        icone = "Ã°Å¸Å¸Â¢"
    else:
        icone = "Ã°Å¸Å¸Â¡"

    print(f"{icone} {nome}")
    print(f"    MissÃƒÂ£o : {missao}")
    print(f"    Status : {status}")
    print()

print("="*80)
print("MISSÃƒÆ'O DA ENGENHARIA DE SISTEMAS")
print("="*80)
print()

print("Projetar a organizaÃƒÂ§ÃƒÂ£o")
print("de toda a plataforma.")
print()

print("Garantir que cada")
print("departamento opere")
print("como parte de um")
print("ÃƒÂºnico organismo digital.")
print()

print("="*80)
print("RESPONSABILIDADES")
print("="*80)
print()

responsabilidades = [

"Projetar arquiteturas.",

"Eliminar redundÃƒÂ¢ncias.",

"Coordenar fÃƒÂ¡bricas.",

"Organizar ecossistemas.",

"Planejar implantaÃƒÂ§ÃƒÂµes.",

"Monitorar gargalos.",

"Distribuir recursos.",

"Padronizar tecnologias.",

"Selecionar algoritmos.",

"Melhorar continuamente."

]

for r in responsabilidades:
    print("Ã¢â‚¬Â¢", r)

print()

print("="*80)
print("FLUXO DE ENGENHARIA")
print("="*80)
print()

fluxo = [

"Necessidade",

"AnÃƒÂ¡lise",

"Projeto",

"Planejamento",

"DistribuiÃƒÂ§ÃƒÂ£o",

"ProduÃƒÂ§ÃƒÂ£o",

"IntegraÃƒÂ§ÃƒÂ£o",

"ValidaÃƒÂ§ÃƒÂ£o",

"ImplantaÃƒÂ§ÃƒÂ£o",

"OperaÃƒÂ§ÃƒÂ£o"

]

for etapa in fluxo:
    print("Ã¢â€ â€œ")
    print(etapa)

print()

print("="*80)
print("ENGENHARIA DE SISTEMAS OBSERVA")
print("="*80)
print()

perguntas = [

"Existe gargalo?",

"Existe desperdÃƒÂ­cio?",

"Existe duplicidade?",

"Existe conflito?",

"Existe oportunidade?",

"Existe melhoria?",

"Existe automaÃƒÂ§ÃƒÂ£o possÃƒÂ­vel?",

"Existe capacidade ociosa?"

]

for p in perguntas:
    print("Ã¢Å"â€œ", p)

print()

print("="*80)
print("CHEFE DE GABINETE")
print("="*80)
print()

print("Bom dia, Presidente.")
print()

print("A Engenharia de Sistemas")
print("assumiu a coordenaÃƒÂ§ÃƒÂ£o")
print("global da organizaÃƒÂ§ÃƒÂ£o.")
print()

print("Todas as fÃƒÂ¡bricas")
print("passam a operar")
print("de forma sincronizada.")
print()

print("As decisÃƒÂµes arquitetÃƒÂ´nicas")
print("serÃƒÂ£o tomadas")
print("antes da produÃƒÂ§ÃƒÂ£o.")
print()

print("="*80)
print("STATUS")
print("="*80)
print()

print(f"Centros Ativos.............. {ativos}")
print(f"Total de Centros............ {len(CENTROS)}")
print(f"Data........................ {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print()

print("ENGENHARIA DE SISTEMAS OPERACIONAL.")


