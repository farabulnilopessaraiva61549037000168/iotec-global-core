# ==========================================================
# 090_INTERNAL_PRODUCTION_DIRECTORATE.py
# IOTEC INTERNAL PRODUCTION DIRECTORATE
# ==========================================================

from datetime import datetime

print("="*80)
print("IOTEC INTERNAL PRODUCTION DIRECTORATE")
print("="*80)
print()

print("Inicializando Diretoria de ProduÃƒÂ§ÃƒÂ£o Interna...")
print()

equipes = [

("Arquitetura do Kernel",
 "Estuda todos os mÃƒÂ³dulos do nÃƒÂºcleo.",
 "ONLINE"),

("Produtores de Interfaces",
 "Criam e modernizam HTML.",
 "ONLINE"),

("Produtores de Produtos",
 "Transformam capacidades em produtos.",
 "ONLINE"),

("Produtores de Conhecimento",
 "LÃƒÂªem cÃƒÂ³digos e escrevem livros tÃƒÂ©cnicos.",
 "ONLINE"),

("Produtores de DocumentaÃƒÂ§ÃƒÂ£o",
 "Documentam automaticamente o sistema.",
 "ONLINE"),

("Produtores Comerciais",
 "Criam portfÃƒÂ³lios e apresentaÃƒÂ§ÃƒÂµes.",
 "ONLINE"),

("Produtores de APIs",
 "Integram novos conectores.",
 "EM IMPLANTAÃƒâ€¡ÃƒÆ'O"),

("Produtores de Ecossistemas",
 "Constroem novos ecossistemas digitais.",
 "ONLINE"),

("Produtores de Qualidade",
 "Executam auditorias e testes.",
 "ONLINE"),

("Produtores de Monitoramento",
 "Observam continuamente toda a plataforma.",
 "ONLINE")

]

print("="*80)
print("LINHAS DE PRODUÃƒâ€¡ÃƒÆ'O")
print("="*80)
print()

online = 0

for nome,funcao,status in equipes:

    if status == "ONLINE":
        icone = "Ã°Å¸Å¸Â¢"
        online += 1
    else:
        icone = "Ã°Å¸Å¸Â¡"

    print(f"{icone} {nome}")
    print(f"    MissÃƒÂ£o : {funcao}")
    print(f"    Status : {status}")
    print()

print("="*80)
print("HIERARQUIA PROGRAMACIONAL")
print("="*80)
print()

hierarquia = [

"PresidÃƒÂªncia",

"Chief of Staff",

"Diretorias",

"GerÃƒÂªncias",

"Linhas de ProduÃƒÂ§ÃƒÂ£o",

"OperÃƒÂ¡rias",

"ServiÃƒÂ§os",

"Motores",

"Algoritmos"

]

for nivel in hierarquia:

    print("Ã¢â€ â€œ")
    print(nivel)

print()

print("="*80)
print("FILOSOFIA")
print("="*80)
print()

print("Nenhum portal poderÃƒÂ¡ existir")
print("sem que uma equipe tenha")
print("construÃƒÂ­do o ecossistema")
print("que existe atrÃƒÂ¡s dele.")
print()

print("Todo botÃƒÂ£o 'Entrar'")
print("representa um ambiente")
print("verdadeiramente operacional.")
print()

print("="*80)
print("PRODUTORES")
print("="*80)
print()

produtores = [

"Estudam cÃƒÂ³digos.",

"Escrevem documentaÃƒÂ§ÃƒÂ£o.",

"Criam livros internos.",

"Criam novos produtos.",

"Criam HTML.",

"Criam APIs.",

"Modernizam interfaces.",

"Descobrem melhorias.",

"Produzem conhecimento.",

"Fortalecem continuamente a empresa."

]

for item in produtores:

    print("Ã¢â‚¬Â¢",item)

print()

print("="*80)
print("CHEFE DE GABINETE")
print("="*80)
print()

print("Bom dia, Presidente.")
print()

print("As linhas internas de produÃƒÂ§ÃƒÂ£o")
print("encontram-se operacionais.")
print()

print("As equipes trabalham")
print("continuamente em seus")
print("respectivos setores,")
print("sem interferÃƒÂªncia")
print("entre departamentos.")
print()

print("="*80)
print("STATUS")
print("="*80)
print()

print(f"Equipes Online............... {online}")
print(f"Total de Diretorias.......... {len(equipes)}")
print(f"Data......................... {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print()

print("DIRETORIA DE PRODUÃƒâ€¡ÃƒÆ'O INTERNA ATIVA.")


