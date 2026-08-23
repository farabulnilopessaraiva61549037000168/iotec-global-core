# ==============================================================================
# 113_TERRITORIAL_INTELLIGENCE_CENTER.py
# IOTEC TERRITORIAL INTELLIGENCE CENTER
# ==============================================================================

from datetime import datetime
import json

print("="*90)
print("IOTEC TERRITORIAL INTELLIGENCE CENTER")
print("CENTRO DE INTELIGÃƒÅ NCIA TERRITORIAL")
print("="*90)
print()

REGIOES={

"NORDESTE":{

"CE":[
"Fortaleza","Caucaia","MaracanaÃƒÂº","Sobral","Juazeiro do Norte",
"Crato","QuixadÃƒÂ¡","Iguatu","Limoeiro do Norte","Itapipoca"
],

"PE":[
"Recife","JaboatÃƒÂ£o","Olinda","Caruaru","Petrolina"
],

"BA":[
"Salvador","Feira de Santana","VitÃƒÂ³ria da Conquista","IlhÃƒÂ©us","Juazeiro"
],

"RN":[
"Natal","MossorÃƒÂ³","Parnamirim"
],

"PB":[
"JoÃƒÂ£o Pessoa","Campina Grande","Patos"
],

"PI":[
"Teresina","ParnaÃƒÂ­ba","Picos"
],

"MA":[
"SÃƒÂ£o LuÃƒÂ­s","Imperatriz","Caxias"
],

"AL":[
"MaceiÃƒÂ³","Arapiraca"
],

"SE":[
"Aracaju","Lagarto"

]

}

}

SEGMENTOS=[

"Engenharia",
"Arquitetura",
"ConstruÃƒÂ§ÃƒÂ£o",
"Hospitais",
"ClÃƒÂ­nicas",
"FarmÃƒÂ¡cias",
"IndÃƒÂºstrias",
"Transportes",
"Tecnologia",
"Supermercados",
"Universidades",
"Escolas",
"Advocacia",
"Contabilidade",
"Energia",
"AgronegÃƒÂ³cio",
"Turismo",
"HotÃƒÂ©is"

]

MISSOES=[]

print("="*90)
print("MISSÃƒâ€¢ES TERRITORIAIS")
print("="*90)
print()

ordem=1

for regiao,estados in REGIOES.items():

    print()
    print(regiao)
    print()

    for uf,cidades in estados.items():

        print(f"{uf}  ({len(cidades)} cidades piloto)")

        for cidade in cidades:

            for segmento in SEGMENTOS:

                MISSOES.append({

                    "id":ordem,

                    "uf":uf,

                    "cidade":cidade,

                    "segmento":segmento,

                    "status":"AGUARDANDO"

                })

                ordem+=1

print()

print("="*90)
print("RESUMO")
print("="*90)
print()

print("RegiÃƒÂµes................",len(REGIOES))
print("Estados................",len(REGIOES["NORDESTE"]))
print("Segmentos..............",len(SEGMENTOS))
print("MissÃƒÂµes................",len(MISSOES))

saida={

"generated_at":datetime.now().isoformat(),

"missoes":MISSOES

}

with open(

"IOTEC_TERRITORIAL_MISSIONS.json",

"w",

encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("O Kernel deixa")
print("de procurar")
print("empresas isoladas.")

print()

print("Agora organiza")
print("o territÃƒÂ³rio")
print("econÃƒÂ´mico.")

print()

print("Cada cidade")

print("ÃƒÂ© uma missÃƒÂ£o.")

print()

print("Cada segmento")

print("ÃƒÂ© uma linha")

print("de produÃƒÂ§ÃƒÂ£o.")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_TERRITORIAL_MISSIONS.json")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("TERRITORIAL INTELLIGENCE OPERACIONAL.")


