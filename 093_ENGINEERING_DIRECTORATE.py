# ==========================================================
# 093_ENGINEERING_DIRECTORATE.py
# IOTEC ENGINEERING DIRECTORATE
# ==========================================================

from datetime import datetime

print("=" * 80)
print("IOTEC ENGINEERING DIRECTORATE")
print("=" * 80)
print()

print("Inicializando Diretoria de Engenharia...")
print()

ENGENHARIAS = [

("Engenharia de ProduÃƒÂ§ÃƒÂ£o",
 "Projeta linhas de produÃƒÂ§ÃƒÂ£o digitais.",
 "ONLINE"),

("Engenharia do Conhecimento",
 "Transforma cÃƒÂ³digo em conhecimento organizado.",
 "ONLINE"),

("Engenharia Comercial",
 "Transforma capacidades em produtos.",
 "ONLINE"),

("Engenharia de Ecossistemas",
 "Projeta novos ambientes digitais.",
 "ONLINE"),

("Engenharia de InteligÃƒÂªncia",
 "Pesquisa melhorias continuamente.",
 "ONLINE"),

("Engenharia de Infraestrutura",
 "Coordena servidores e integraÃƒÂ§ÃƒÂµes.",
 "ONLINE"),

("Engenharia de Qualidade",
 "Valida produtos antes da entrega.",
 "ONLINE"),

("Engenharia de ImplantaÃƒÂ§ÃƒÂ£o",
 "Entrega sistemas ao ambiente produtivo.",
 "ONLINE"),

("Engenharia Financeira",
 "Conecta capacidades ÃƒÂ  geraÃƒÂ§ÃƒÂ£o de receita.",
 "EM IMPLANTAÃƒâ€¡ÃƒÆ'O")

]

print("=" * 80)
print("DEPARTAMENTOS DE ENGENHARIA")
print("=" * 80)
print()

online = 0

for nome,missao,status in ENGENHARIAS:

    if status == "ONLINE":
        simbolo = "Ã°Å¸Å¸Â¢"
        online += 1
    elif status == "EM IMPLANTAÃƒâ€¡ÃƒÆ'O":
        simbolo = "Ã°Å¸Å¸Â¡"
    else:
        simbolo = "Ã°Å¸â€Â´"

    print(f"{simbolo} {nome}")
    print(f"    MissÃƒÂ£o : {missao}")
    print(f"    Status : {status}")
    print()

print("=" * 80)
print("CICLO DE ENGENHARIA")
print("=" * 80)
print()

ciclo = [

"ObservaÃƒÂ§ÃƒÂ£o",

"CompreensÃƒÂ£o",

"Projeto",

"Planejamento",

"ProduÃƒÂ§ÃƒÂ£o",

"IntegraÃƒÂ§ÃƒÂ£o",

"ValidaÃƒÂ§ÃƒÂ£o",

"ImplantaÃƒÂ§ÃƒÂ£o",

"OperaÃƒÂ§ÃƒÂ£o",

"Aprendizado"

]

for etapa in ciclo:

    print("Ã¢â€ â€œ")
    print(etapa)

print()

print("=" * 80)
print("ENGENHO")
print("=" * 80)
print()

print("Engenho ÃƒÂ© a capacidade")
print("de transformar")
print("conhecimento organizado")
print("em soluÃƒÂ§ÃƒÂµes digitais")
print("de alto valor.")
print()

print("=" * 80)
print("ENGENHOSIDADE")
print("=" * 80)
print()

principios = [

"Selecionar os melhores algoritmos.",

"Eliminar redundÃƒÂ¢ncias.",

"Projetar antes de construir.",

"Organizar antes de executar.",

"Automatizar sempre que possÃƒÂ­vel.",

"Aprender continuamente.",

"Criar soluÃƒÂ§ÃƒÂµes reutilizÃƒÂ¡veis.",

"Produzir valor para o cliente.",

"Melhorar continuamente."

]

for p in principios:

    print("Ã¢â‚¬Â¢", p)

print()

print("=" * 80)
print("PAPEL DA ENGENHARIA")
print("=" * 80)
print()

print("A Engenharia nÃƒÂ£o produz")
print("apenas cÃƒÂ³digos.")
print()

print("Ela projeta")
print("a organizaÃƒÂ§ÃƒÂ£o")
print("de toda a empresa.")
print()

print("Cada algoritmo")
print("ÃƒÂ© escolhido")
print("pela sua capacidade")
print("de gerar valor.")
print()

print("=" * 80)
print("CHEFE DE GABINETE")
print("=" * 80)
print()

print("Bom dia, Presidente.")
print()

print("A Diretoria de Engenharia")
print("encontra-se operacional.")
print()

print("Os projetos estÃƒÂ£o")
print("sendo organizados")
print("antes da produÃƒÂ§ÃƒÂ£o.")
print()

print("As equipes utilizam")
print("algoritmos previamente")
print("selecionados e validados.")
print()

print("=" * 80)
print("STATUS")
print("=" * 80)
print()

print(f"Engenharias Online.......... {online}")
print(f"Total de Engenharias........ {len(ENGENHARIAS)}")
print(f"Data........................ {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print()

print("DIRETORIA DE ENGENHARIA ATIVA.")


