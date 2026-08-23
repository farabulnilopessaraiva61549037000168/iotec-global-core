# ==============================================================================
# 107_ENTITY_CLASSIFIER_ENGINE.py
# IOTEC ENTITY CLASSIFIER ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC ENTITY CLASSIFIER ENGINE")
print("CLASSIFICADOR DE ENTIDADES")
print("="*90)
print()

ARQUIVO="IOTEC_OPENSTREETMAP_RESULTS.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:

        dados=json.load(f)

except Exception:

    print("Arquivo nÃƒÂ£o encontrado.")
    raise SystemExit()

entidades=[]

print("Analisando entidades...")
print()

for item in dados["resultados"]:

    nome=item["nome"]

    texto=nome.lower()

    categoria="OUTROS"

    prioridade=1

    if "engenharia" in texto:

        categoria="EMPRESA"

        prioridade=5

    if "departamento" in texto:

        categoria="UNIVERSIDADE"

        prioridade=2

    if "laboratÃƒÂ³rio" in texto or "laboratorio" in texto:

        categoria="LABORATÃƒâ€œRIO"

        prioridade=2

    if "centro acadÃƒÂªmico" in texto:

        categoria="CENTRO ACADÃƒÅ MICO"

        prioridade=1

    if "grupo" in texto:

        categoria="GRUPO DE PESQUISA"

        prioridade=1

    entidade={

        "nome":nome,

        "categoria":categoria,

        "prioridade":prioridade,

        "latitude":item["latitude"],

        "longitude":item["longitude"],

        "origem":item["origem"]

    }

    entidades.append(entidade)

entidades.sort(

    key=lambda x:(

        -x["prioridade"],

        x["nome"]

    )

)

saida={

    "generated_at":datetime.now().isoformat(),

    "total":len(entidades),

    "entidades":entidades

}

with open(

    "IOTEC_ENTITY_DATABASE.json",

    "w",

    encoding="utf8"

) as f:

    json.dump(

        saida,

        f,

        indent=4,

        ensure_ascii=False

    )

print("="*90)
print("ENTIDADES")
print("="*90)
print()

for e in entidades:

    estrelas="Ã¢Ëœâ€¦"*e["prioridade"]

    print(f"{estrelas:5} {e['categoria']:20} {e['nome']}")

print()

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_ENTITY_DATABASE.json")

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("O Kernel deixa")
print("de enxergar")
print("apenas nomes.")

print()

print("Agora o Kernel")
print("compreende")
print("a natureza")
print("das entidades.")

print()

print("Empresas.")

print("Universidades.")

print("LaboratÃƒÂ³rios.")

print("Grupos.")

print("Centros.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Entidades........",len(entidades))
print("Data.............",datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("ENTITY CLASSIFIER OPERACIONAL.")


