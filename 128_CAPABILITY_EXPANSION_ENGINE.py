# ==============================================================================
# 128_CAPABILITY_EXPANSION_ENGINE.py
# IOTEC CAPABILITY EXPANSION ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC CAPABILITY EXPANSION ENGINE")
print("MOTOR DE EXPANSÃƒÆ'O DE CAPACIDADES")
print("="*90)
print()

ARQUIVO="IOTEC_CAPABILITY_RADAR.json"

try:

    with open(ARQUIVO,"r",encoding="utf8") as f:
        banco=json.load(f)

except:

    print("Radar nÃƒÂ£o encontrado.")
    raise SystemExit()

capacidades=banco.get("capacidades",[])

MISSOES=[]

print("="*90)
print("MISSÃƒâ€¢ES DE ENGENHARIA")
print("="*90)
print()

contador=1

for item in capacidades:

    if item["cobertura"]>=100:
        continue

    prioridade="CRÃƒÂTICA"

    if item["cobertura"]>=50:
        prioridade="MÃƒâ€°DIA"

    missao={

        "id":contador,

        "capacidade":item["capacidade"],

        "cobertura":item["cobertura"],

        "prioridade":prioridade,

        "status":"AGUARDANDO",

        "acao":"Adicionar novo conector"

    }

    MISSOES.append(missao)

    print("="*70)
    print("MissÃƒÂ£o........",contador)
    print("Capacidade....",item["capacidade"])
    print("Cobertura.....",item["cobertura"],"%")
    print("Prioridade....",prioridade)
    print("AÃƒÂ§ÃƒÂ£o.......... Adicionar novo conector")
    print()

    contador+=1

saida={

    "generated_at":datetime.now().isoformat(),

    "engine":"CAPABILITY_EXPANSION_ENGINE",

    "version":"1.0",

    "total":len(MISSOES),

    "missoes":MISSOES

}

with open(

    "IOTEC_ENGINEERING_QUEUE.json",

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
print("RESUMO")
print("="*90)
print()

print("MissÃƒÂµes criadas......",len(MISSOES))
print("Fila de engenharia... IOTEC_ENGINEERING_QUEUE.json")

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("O Kernel identifica")
print("automaticamente")
print("as capacidades")
print("que precisam")
print("evoluir.")

print()

print("Cada lacuna")
print("gera uma")
print("missÃƒÂ£o")
print("de engenharia.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("CAPABILITY EXPANSION OPERACIONAL.")

