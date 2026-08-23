# ==========================================================
# 097_OPERATIONAL_INTELLIGENCE_CENTER.py
# IOTEC OPERATIONAL INTELLIGENCE CENTER
# ==========================================================

import os
import json
from datetime import datetime

print("="*90)
print("IOTEC OPERATIONAL INTELLIGENCE CENTER")
print("CENTRO DE INTELIGÃƒÅ NCIA OPERACIONAL")
print("="*90)
print()

ARQUIVOS = {

    "Warehouse":"IOTEC_EXPERIENCE_WAREHOUSE.json",

    "Visual Genome":"IOTEC_VISUAL_GENOME.json",

    "Official Assets":"IOTEC_OFFICIAL_ASSETS.json",

    "Code Library":"IOTEC_CODE_LIBRARY.json"

}

print("Carregando patrimÃƒÂ´nio operacional...")
print()

patrimonio={}

for nome,arquivo in ARQUIVOS.items():

    if os.path.exists(arquivo):

        try:

            with open(arquivo,"r",encoding="utf-8") as f:

                dados=json.load(f)

            patrimonio[nome]=dados

            print("Ã°Å¸Å¸Â¢",nome.ljust(25),"ONLINE")

        except Exception:

            patrimonio[nome]=None

            print("Ã°Å¸Å¸Â¡",nome.ljust(25),"ERRO")

    else:

        patrimonio[nome]=None

        print("Ã°Å¸â€Â´",nome.ljust(25),"NÃƒÆ'O ENCONTRADO")

print()

print("="*90)
print("PATRIMÃƒâ€NIO")
print("="*90)
print()

warehouse=0
code=0
ativos=0

# EXPERIENCE WAREHOUSE

try:

    warehouse=patrimonio["Warehouse"]["arquivos"]

except:

    pass

# CODE LIBRARY

try:

    code=patrimonio["Code Library"]["arquivos_estudados"]

except:

    pass

# OFFICIAL ASSETS

try:

    ativos=patrimonio["Official Assets"]["patrimonio_oficial"]

except:

    pass

print("MÃƒÂ³dulos Python................",code)
print("Interfaces HTML...............",warehouse)
print("Ativos Oficiais...............",ativos)
print()

print("="*90)
print("MATURIDADE OPERACIONAL")
print("="*90)
print()

indices=[

("Conhecimento",96),

("Arquitetura",95),

("ProduÃƒÂ§ÃƒÂ£o",88),

("Infraestrutura",82),

("AutomaÃƒÂ§ÃƒÂ£o",86),

("Receita",22)

]

soma=0

for nome,valor in indices:

    barra="Ã¢â€"Ë†"*int(valor/5)+"Ã¢â€"â€˜"*(20-int(valor/5))

    print(nome.ljust(22),barra,f"{valor}%")

    soma+=valor

media=soma/len(indices)

print()

print("MATURIDADE GERAL............. %.1f%%"%media)

print()

print("="*90)
print("RADAR EXECUTIVO")
print("="*90)
print()

radar=[

("Revenue Factory","CRÃƒÂTICO"),

("Google Maps","PENDENTE"),

("LinkedIn","PENDENTE"),

("WhatsApp Business","IMPLANTAÃƒâ€¡ÃƒÆ'O"),

("Executive Skin","ESTÃƒÂVEL"),

("Knowledge Factory","ESTÃƒÂVEL"),

("Experience Warehouse","ESTÃƒÂVEL"),

("Visual Genome","ESTÃƒÂVEL")

]

for nome,status in radar:

    if status=="ESTÃƒÂVEL":

        cor="Ã°Å¸Å¸Â¢"

    elif status=="IMPLANTAÃƒâ€¡ÃƒÆ'O":

        cor="Ã°Å¸Å¸Â¡"

    else:

        cor="Ã°Å¸â€Â´"

    print(cor,nome.ljust(30),status)

print()

print("="*90)
print("PERGUNTAS DO KERNEL")
print("="*90)
print()

perguntas=[

"Existe tecnologia parada?",

"Existe produto reutilizÃƒÂ¡vel?",

"Existe HTML nÃƒÂ£o utilizado?",

"Existe integraÃƒÂ§ÃƒÂ£o pendente?",

"Existe capacidade ociosa?",

"Existe oportunidade comercial?",

"Existe cliente aguardando?",

"Existe receita bloqueada?"

]

for p in perguntas:

    print("Ã¢â‚¬Â¢",p)

print()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print()

print("Boa noite, Presidente.")
print()

print("O Centro de InteligÃƒÂªncia")
print("estÃƒÂ¡ observando")
print("toda a organizaÃƒÂ§ÃƒÂ£o.")
print()

print("As prioridades atuais sÃƒÂ£o:")

print()

print("1. Concluir Google Maps")

print("2. Finalizar WhatsApp Business")

print("3. Implantar LinkedIn")

print("4. Aumentar a Revenue Factory")

print("5. Atrair clientes reais")

print()

print("="*90)
print("MISSÃƒÆ'O")
print("="*90)
print()

print()

print("Transformar dados")

print("em conhecimento.")

print()

print("Transformar conhecimento")

print("em decisÃƒÂµes.")

print()

print("Transformar decisÃƒÂµes")

print("em crescimento.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print()

print("Centro de InteligÃƒÂªncia....... ONLINE")

print("Data.........................",datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("OPERATIONAL INTELLIGENCE CENTER ATIVO.")


